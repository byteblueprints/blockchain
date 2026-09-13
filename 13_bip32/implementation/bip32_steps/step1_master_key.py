import os
import sys
import io
import contextlib

_HMAC_SHA512_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "10_hmac_sha512", "implementation",
))
_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "06_ecc", "implementation",
))
sys.path.append(_HMAC_SHA512_IMPLEMENTATION_DIR)
sys.path.append(_ECC_IMPLEMENTATION_DIR)

from hmac_sha512_steps.step3_outer_hash import outer_hash as _hmac_sha512
from ecc_constants.curve_parameters import N

MASTER_KEY_SALT = b"Bitcoin seed"


def hmac_sha512(key: bytes, message: bytes) -> bytes:
    with contextlib.redirect_stdout(io.StringIO()):
        return _hmac_sha512(key, message)


def generate_master_key(seed: bytes):
    """
    Step 1: Turn a BIP39 seed into the master private key + chain code -
    the root of the entire HD wallet tree.
        I = HMAC-SHA512(key="Bitcoin seed", message=seed)
        master_private_key = left 32 bytes of I, as an integer
        master_chain_code  = right 32 bytes of I

    WHY the fixed string "Bitcoin seed" as the HMAC key: it's a domain
    separator - it exists purely so that "HMAC-SHA512 of a BIP39 seed for
    the purpose of making a Bitcoin wallet" produces a completely
    different result than the same seed bytes being used as input to some
    other, unrelated HMAC-based construction. Every BIP32 wallet must use
    this exact string, or it derives a different (still valid-looking,
    but incompatible) tree from the same seed.
    """
    digest = hmac_sha512(MASTER_KEY_SALT, seed)
    master_private_key = int.from_bytes(digest[:32], byteorder='big')
    master_chain_code = digest[32:]

    if master_private_key == 0 or master_private_key >= N:
        raise ValueError("Invalid seed produced an out-of-range master key (astronomically unlikely - try a different seed)")

    print(f"1. Master private key: {hex(master_private_key)}")
    print(f"   Master chain code:  {master_chain_code.hex()}")
    return master_private_key, master_chain_code


if __name__ == "__main__":
    generate_master_key(bytes.fromhex("000102030405060708090a0b0c0d0e0f"))
