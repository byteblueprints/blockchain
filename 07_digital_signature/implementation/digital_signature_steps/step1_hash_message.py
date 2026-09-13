import os
import sys

# Reuses this project's own from-scratch SHA-256 (02_sha256), not hashlib -
# ECDSA signs the hash of a message, never the raw message itself, both so
# messages of any length reduce to a fixed-size number and so an attacker
# can't exploit the algebraic structure of the raw message.
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

import io
import contextlib


def sha256_hex(message: str) -> str:
    """Runs this project's own SHA-256 pipeline over a message, returns hex digest."""
    bits = ''.join(format(ord(char), '08b') for char in message)

    with contextlib.redirect_stdout(io.StringIO()):
        padded_bits = pad_message(bits)
        blocks = get_message_blocks(padded_bits)

        hash_values = get_initial_hash_values()
        for block in blocks:
            words = create_message_schedule(block)
            schedule = expand_message_schedule(words)
            compressed = compress_block(hash_values, schedule)
            hash_values = get_next_hash(hash_values, compressed)

    return ''.join(format(value, '08x') for value in hash_values)


def hash_message(message: str) -> int:
    """
    Step 1: Hash the message and interpret the digest as an integer z.
    secp256k1's order n is 256 bits, same as SHA-256's output, so per the
    ECDSA spec the full digest is used directly (no truncation needed).
    """
    digest_hex = sha256_hex(message)
    z = int(digest_hex, 16)

    print(f"1. Message:      {message}")
    print(f"   SHA-256:      {digest_hex}")
    print(f"   z (integer):  {hex(z)}")
    return z


if __name__ == "__main__":
    hash_message("abc")
