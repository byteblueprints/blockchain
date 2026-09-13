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
from ecc_steps.step3_scalar_multiplication import scalar_multiply
from ecc_steps.step6_key_encoding import encode_public_key_compressed
from bip32_constants import HARDENED_OFFSET
from bip32_steps.step1_master_key import hmac_sha512


def _compressed_pubkey_bytes(private_key: int) -> bytes:
    with contextlib.redirect_stdout(io.StringIO()):
        point = scalar_multiply(private_key, (GX, GY))
        hex_str = encode_public_key_compressed(point)
    return bytes.fromhex(hex_str)


def ckd_private(parent_key: int, parent_chain_code: bytes, index: int):
    """
    Step 2: Derive a child PRIVATE key from a parent private key
    (CKDpriv - "Child Key Derivation, private").

    Hardened (index >= 2**31, written as N' in a path):
        data = 0x00 || parent_private_key (32 bytes) || index (4 bytes)
    Normal (index < 2**31):
        data = compressed(parent_public_key) || index (4 bytes)

        I = HMAC-SHA512(key=parent_chain_code, message=data)
        child_private_key = (left 32 bytes of I, as int) + parent_private_key, mod n
        child_chain_code = right 32 bytes of I

    The hardened/normal split is what makes hardened derivation only
    possible from the PRIVATE key: normal derivation's input data only
    needs the parent's PUBLIC key, so it can be computed without the
    private key ever being present - hardened derivation deliberately
    breaks that by requiring the raw private key in the HMAC input.
    """
    if index >= HARDENED_OFFSET:
        data = b'\x00' + parent_key.to_bytes(32, byteorder='big') + index.to_bytes(4, byteorder='big')
    else:
        data = _compressed_pubkey_bytes(parent_key) + index.to_bytes(4, byteorder='big')

    digest = hmac_sha512(parent_chain_code, data)
    left, child_chain_code = digest[:32], digest[32:]
    left_int = int.from_bytes(left, byteorder='big')

    if left_int >= N:
        raise ValueError("Invalid child index (astronomically unlikely - try the next index)")

    child_key = (left_int + parent_key) % N
    if child_key == 0:
        raise ValueError("Invalid child index produced a zero key (astronomically unlikely - try the next index)")

    print(f"2. CKDpriv(index={hex(index)}): child private key = {hex(child_key)}")
    return child_key, child_chain_code


if __name__ == "__main__":
    from bip32_steps.step1_master_key import generate_master_key

    with contextlib.redirect_stdout(io.StringIO()):
        master_key, master_chain_code = generate_master_key(bytes.fromhex("000102030405060708090a0b0c0d0e0f"))

    ckd_private(master_key, master_chain_code, HARDENED_OFFSET)
