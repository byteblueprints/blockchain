import os
import sys
import io
import contextlib

_SHA256_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "02_sha256", "implementation",
))
sys.path.append(_SHA256_IMPLEMENTATION_DIR)

from sha256_steps.step2_padding import pad_message
from sha256_steps.step3_message_block import get_message_blocks
from sha256_steps.step4_message_schedule import create_message_schedule
from sha256_steps.step5_expand_message_schedule import expand_message_schedule
from sha256_steps.step6_initial_hash_values import get_initial_hash_values
from sha256_steps.step8_final_block_output import compress_block
from sha256_steps.step9_h1 import get_next_hash


def sha256_bytes(data: bytes) -> bytes:
    """Runs this project's own SHA-256 pipeline (02_sha256) over raw bytes, returns raw digest bytes."""
    bits = ''.join(format(byte, '08b') for byte in data)

    with contextlib.redirect_stdout(io.StringIO()):
        padded_bits = pad_message(bits)
        blocks = get_message_blocks(padded_bits)

        hash_values = get_initial_hash_values()
        for block in blocks:
            words = create_message_schedule(block)
            schedule = expand_message_schedule(words)
            compressed = compress_block(hash_values, schedule)
            hash_values = get_next_hash(hash_values, compressed)

    return b''.join(value.to_bytes(4, 'big') for value in hash_values)


def checksum_bits(entropy: bytes) -> str:
    """
    Step 2: Compute the BIP39 checksum - the first (entropy_bits / 32)
    bits of SHA256(entropy), as a bit string.

    WHY: this is what lets a wallet detect a mistyped or corrupted
    mnemonic BEFORE using it - if you transpose two words or fat-finger
    one, the checksum almost certainly won't match, so the wallet can
    reject it immediately instead of silently deriving the wrong keys.
    """
    entropy_bits = len(entropy) * 8
    checksum_length = entropy_bits // 32

    digest = sha256_bytes(entropy)
    digest_bits = ''.join(format(byte, '08b') for byte in digest)
    check_bits = digest_bits[:checksum_length]

    print(f"2. Checksum ({checksum_length} bits): {check_bits}")
    return check_bits


if __name__ == "__main__":
    checksum_bits(bytes(16))
