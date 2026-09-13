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

BLOCK_SIZE = 64   # SHA-256 processes messages in 64-byte (512-bit) blocks
DIGEST_SIZE = 32  # SHA-256 produces a 32-byte (256-bit) digest


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


def prepare_key(key: bytes) -> bytes:
    """
    Step 1: Prepare the key for HMAC by adjusting it to the hash's block
    size (64 bytes for SHA-256).
      - Key longer than the block size: hash it down first (a key that big
        gains nothing from being used raw, and HMAC's security proof
        assumes a block-sized key).
      - Key shorter than the block size: right-pad with zero bytes.
    """
    if len(key) > BLOCK_SIZE:
        key = sha256_bytes(key)
    padded_key = key + b'\x00' * (BLOCK_SIZE - len(key))

    print(f"1. Prepared key: {padded_key.hex()}")
    return padded_key


if __name__ == "__main__":
    prepare_key(b"key")
