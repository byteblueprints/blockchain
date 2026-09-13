import os
import sys

_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "06_ecc", "implementation"))
sys.path.append(_ECC_IMPLEMENTATION_DIR)

from ecc_constants.curve_parameters import GX, GY
from ecc_steps.step3_scalar_multiplication import scalar_multiply
from bip32_steps.step5_derive_path import derive_path
from bip32_steps.step4_serialization import serialize_private_key, serialize_public_key


def derive_extended_keys(seed: bytes, path: str):
    """
    Full BIP32 pipeline: seed + path -> (xprv, xpub) extended key strings.
    """
    key, chain_code, depth, parent_fingerprint, child_number = derive_path(seed, path)
    public_key = scalar_multiply(key, (GX, GY))

    xprv = serialize_private_key(key, chain_code, depth, parent_fingerprint, child_number)
    xpub = serialize_public_key(public_key, chain_code, depth, parent_fingerprint, child_number)
    return xprv, xpub


def main():
    seed = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    path = "m/0'/1/2'/2/1000000000"

    xprv, xpub = derive_extended_keys(seed, path)
    print()
    print(f"Path: {path}")
    print(f"xprv: {xprv}")
    print(f"xpub: {xpub}")


if __name__ == "__main__":
    main()
