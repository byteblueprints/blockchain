import os
import sys
import io
import contextlib

_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "06_ecc", "implementation",
))
sys.path.append(_ECC_IMPLEMENTATION_DIR)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from ecc_constants.curve_parameters import N, GX, GY
from ecc_steps.step1_point_addition import point_add
from ecc_steps.step2_point_doubling import point_double
from ecc_steps.step3_scalar_multiplication import scalar_multiply
from ecc_steps.step6_key_encoding import encode_public_key_compressed
from bip32_constants import HARDENED_OFFSET
from bip32_steps.step1_master_key import hmac_sha512


def ckd_public(parent_public_key, parent_chain_code: bytes, index: int):
    """
    Step 3: Derive a child PUBLIC key from a parent PUBLIC key alone
    (CKDpub - "Child Key Derivation, public"), no private key needed.
    Only defined for normal (non-hardened) indices.

        data = compressed(parent_public_key) || index (4 bytes)
        I = HMAC-SHA512(key=parent_chain_code, message=data)
        child_public_key = (left 32 bytes of I, as int) * G + parent_public_key
        child_chain_code = right 32 bytes of I

    This is what lets, say, an online store's server generate a fresh
    receiving address for every order without ever holding a private key
    on that server - it only needs the public key and chain code, watches
    the blockchain for payments, and the actual spending key stays
    offline.
    """
    if index >= HARDENED_OFFSET:
        raise ValueError("cannot derive a hardened child from a public key alone - the private key is required")

    with contextlib.redirect_stdout(io.StringIO()):
        parent_pubkey_hex = encode_public_key_compressed(parent_public_key)
    data = bytes.fromhex(parent_pubkey_hex) + index.to_bytes(4, byteorder='big')

    digest = hmac_sha512(parent_chain_code, data)
    left, child_chain_code = digest[:32], digest[32:]
    left_int = int.from_bytes(left, byteorder='big')

    if left_int >= N:
        raise ValueError("Invalid child index (astronomically unlikely - try the next index)")

    with contextlib.redirect_stdout(io.StringIO()):
        point_from_left = scalar_multiply(left_int, (GX, GY))
        if point_from_left == parent_public_key:
            child_public_key = point_double(point_from_left)
        else:
            child_public_key = point_add(point_from_left, parent_public_key)

    print(f"3. CKDpub(index={hex(index)}): child public key = {child_public_key}")
    return child_public_key, child_chain_code


if __name__ == "__main__":
    from bip32_steps.step1_master_key import generate_master_key

    with contextlib.redirect_stdout(io.StringIO()):
        master_key, master_chain_code = generate_master_key(bytes.fromhex("000102030405060708090a0b0c0d0e0f"))
        master_public_key = scalar_multiply(master_key, (GX, GY))

    ckd_public(master_public_key, master_chain_code, 0)
