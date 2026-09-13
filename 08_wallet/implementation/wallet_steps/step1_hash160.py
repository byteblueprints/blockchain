import os
import sys
import io
import contextlib

_IMPLEMENTATION_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.append(os.path.join(_IMPLEMENTATION_ROOT, "02_sha256", "implementation"))
sys.path.append(os.path.join(_IMPLEMENTATION_ROOT, "03_ripemd160", "implementation"))

from sha256_steps.step2_padding import pad_message as sha256_pad
from sha256_steps.step3_message_block import get_message_blocks as sha256_blocks
from sha256_steps.step4_message_schedule import create_message_schedule as sha256_schedule
from sha256_steps.step5_expand_message_schedule import expand_message_schedule as sha256_expand
from sha256_steps.step6_initial_hash_values import get_initial_hash_values as sha256_initial_hash
from sha256_steps.step8_final_block_output import compress_block as sha256_compress
from sha256_steps.step9_h1 import get_next_hash as sha256_next_hash

from ripemd160_steps.step2_padding import pad_message as ripemd_pad
from ripemd160_steps.step3_message_block import get_message_blocks as ripemd_blocks
from ripemd160_steps.step4_message_schedule import create_message_schedule as ripemd_schedule
from ripemd160_steps.step6_run_all_steps import run_all_steps as ripemd_run_all_steps
from ripemd160_steps.step7_combine import combine as ripemd_combine
from ripemd160_steps.step8_digest import get_digest as ripemd_digest

RIPEMD160_IV = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]


def sha256_bytes(data: bytes) -> bytes:
    """Runs this project's own SHA-256 (02_sha256) over raw bytes, returns raw digest bytes."""
    bits = ''.join(format(byte, '08b') for byte in data)
    with contextlib.redirect_stdout(io.StringIO()):
        padded = sha256_pad(bits)
        blocks = sha256_blocks(padded)
        hash_values = sha256_initial_hash()
        for block in blocks:
            words = sha256_schedule(block)
            schedule = sha256_expand(words)
            compressed = sha256_compress(hash_values, schedule)
            hash_values = sha256_next_hash(hash_values, compressed)
    return b''.join(value.to_bytes(4, 'big') for value in hash_values)


def ripemd160_bytes(data: bytes) -> bytes:
    """Runs this project's own RIPEMD-160 (03_ripemd160) over raw bytes, returns raw digest bytes."""
    bits = ''.join(format(byte, '08b') for byte in data)
    with contextlib.redirect_stdout(io.StringIO()):
        padded = ripemd_pad(bits)
        blocks = ripemd_blocks(padded)
        hash_values = list(RIPEMD160_IV)
        for block in blocks:
            words = [int(word, 2) for word in ripemd_schedule(block)]
            left, right = ripemd_run_all_steps(hash_values, words)
            hash_values = ripemd_combine(hash_values, left, right)
        digest_hex = ripemd_digest(hash_values)
    return bytes.fromhex(digest_hex)


def hash160(public_key_bytes: bytes) -> bytes:
    """
    Step 1: HASH160(x) = RIPEMD160(SHA256(x)).
    This is the standard way Bitcoin shrinks a public key down to a
    20-byte value for use in an address - RIPEMD-160's shorter output
    (160 bits vs SHA-256's 256) makes addresses shorter to write down,
    while still using SHA-256 as the first pass for its stronger, more
    thoroughly analyzed security margin.
    """
    digest = ripemd160_bytes(sha256_bytes(public_key_bytes))

    print(f"1. HASH160: {digest.hex()}")
    return digest


if __name__ == "__main__":
    hash160(bytes.fromhex("0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352"))
