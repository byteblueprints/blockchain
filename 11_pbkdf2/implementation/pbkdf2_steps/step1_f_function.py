import os
import sys

_HMAC_SHA512_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "10_hmac_sha512", "implementation",
))
sys.path.append(_HMAC_SHA512_IMPLEMENTATION_DIR)

from hmac_sha512_steps.step3_outer_hash import outer_hash as _hmac_sha512

import io
import contextlib

DIGEST_SIZE = 64  # SHA-512 output size in bytes


def hmac_sha512(key: bytes, message: bytes) -> bytes:
    with contextlib.redirect_stdout(io.StringIO()):
        return _hmac_sha512(key, message)


def f_function(password: bytes, salt: bytes, iterations: int, block_index: int) -> bytes:
    """
    Step 1: RFC 2898's "F" function - computes one block of PBKDF2 output.
        U1 = HMAC(password, salt || block_index_as_4_bytes)
        U2 = HMAC(password, U1)
        ...
        U_iterations = HMAC(password, U_(iterations-1))
        F = U1 XOR U2 XOR ... XOR U_iterations

    WHY repeat and XOR instead of just hashing once: a single HMAC call is
    fast, which is exactly wrong for a password-derived key - fast means
    cheap to brute-force. Repeating thousands of times deliberately makes
    each guess expensive, and XOR-ing every intermediate result (rather
    than only keeping the last one) means an attacker can't shortcut the
    work by only computing a subset of the rounds.
    """
    u = hmac_sha512(password, salt + block_index.to_bytes(4, byteorder='big'))
    result = bytearray(u)

    for _ in range(iterations - 1):
        u = hmac_sha512(password, u)
        for i in range(DIGEST_SIZE):
            result[i] ^= u[i]

    print(f"1. F(block={block_index}, iterations={iterations}): {bytes(result).hex()}")
    return bytes(result)


if __name__ == "__main__":
    f_function(b"password", b"salt", 1, 1)
