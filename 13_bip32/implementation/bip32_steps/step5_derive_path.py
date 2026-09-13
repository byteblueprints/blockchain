import os
import sys
import io
import contextlib

_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "06_ecc", "implementation",
))
sys.path.append(_ECC_IMPLEMENTATION_DIR)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from ecc_constants.curve_parameters import GX, GY
from ecc_steps.step3_scalar_multiplication import scalar_multiply
from bip32_constants import HARDENED_OFFSET
from bip32_steps.step1_master_key import generate_master_key
from bip32_steps.step2_ckd_private import ckd_private
from bip32_steps.step4_serialization import fingerprint


def parse_path(path: str) -> list:
    """
    Parses a derivation path like "m/44'/0'/0'/0/0" into a list of raw
    indices, where a trailing "'" or "h"/"H" marks a hardened index
    (adds HARDENED_OFFSET = 2**31).
    """
    segments = path.split('/')
    if segments[0] != 'm':
        raise ValueError("path must start with 'm'")

    indices = []
    for segment in segments[1:]:
        if segment.endswith("'") or segment.endswith(("h", "H")):
            indices.append(int(segment[:-1]) + HARDENED_OFFSET)
        else:
            indices.append(int(segment))
    return indices


def derive_path(seed: bytes, path: str):
    """
    Step 5: Walk a full derivation path from a seed, applying CKDpriv
    (step 2) once per path segment, starting from the master key (step 1).
    Returns the final (private_key, chain_code, depth, parent_fingerprint,
    child_number) - everything needed to serialize the resulting key
    (step 4).
    """
    with contextlib.redirect_stdout(io.StringIO()):
        key, chain_code = generate_master_key(seed)

    indices = parse_path(path)
    depth = 0
    parent_fingerprint = b'\x00\x00\x00\x00'
    child_number = 0

    for index in indices:
        with contextlib.redirect_stdout(io.StringIO()):
            parent_public_key = scalar_multiply(key, (GX, GY))
            parent_fingerprint = fingerprint(parent_public_key)
            key, chain_code = ckd_private(key, chain_code, index)
        depth += 1
        child_number = index

    print(f"5. Derived {path}: depth={depth}, key={hex(key)}")
    return key, chain_code, depth, parent_fingerprint, child_number


if __name__ == "__main__":
    derive_path(bytes.fromhex("000102030405060708090a0b0c0d0e0f"), "m/0'/1/2'/2/1000000000")
