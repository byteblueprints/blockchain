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

CHECKSUM_LENGTH = 4


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


def checksum(payload: bytes) -> bytes:
    """
    Step 3: Base58Check's checksum = first 4 bytes of SHA256(SHA256(payload)).

    WHY hash twice, not once: this is Bitcoin's specific convention
    (sometimes called "double SHA-256"), adopted as defense-in-depth
    against any future weakness discovered in a single round of SHA-256
    that might make partial-preimage or length-extension-style forgery of
    a single hash easier. It doesn't need to be double for the checksum's
    basic error-detection purpose - it's a deliberate margin of safety.
    """
    digest = sha256_bytes(sha256_bytes(payload))
    check = digest[:CHECKSUM_LENGTH]

    print(f"3. Checksum: {check.hex()}")
    return check


if __name__ == "__main__":
    # Known example (Bitcoin wiki): version byte + HASH160, expect checksum D61967F6
    checksum(bytes.fromhex("00010966776006953D5567439E5E39F86A0D273BEE"))
