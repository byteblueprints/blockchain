import os
import sys
import io
import contextlib

_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "06_ecc", "implementation",
))
_WALLET_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "08_wallet", "implementation",
))
_BASE58_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "05_base58", "implementation",
))
sys.path.append(_ECC_IMPLEMENTATION_DIR)
sys.path.append(_WALLET_IMPLEMENTATION_DIR)
sys.path.append(_BASE58_IMPLEMENTATION_DIR)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from ecc_constants.curve_parameters import GX, GY
from ecc_steps.step3_scalar_multiplication import scalar_multiply
from ecc_steps.step6_key_encoding import encode_public_key_compressed
from wallet_steps.step1_hash160 import hash160
from base58_steps.step4_encode_check import encode_check
from bip32_constants import VERSION_PRIVATE, VERSION_PUBLIC


def _compressed_pubkey_bytes_from_point(point) -> bytes:
    with contextlib.redirect_stdout(io.StringIO()):
        return bytes.fromhex(encode_public_key_compressed(point))


def fingerprint(public_key_point) -> bytes:
    """The first 4 bytes of HASH160(compressed public key) - identifies a key's PARENT without revealing the full parent key."""
    with contextlib.redirect_stdout(io.StringIO()):
        h160 = hash160(_compressed_pubkey_bytes_from_point(public_key_point))
    return h160[:4]


def serialize_extended_key(version: int, depth: int, parent_fingerprint: bytes, child_number: int,
                            chain_code: bytes, key_data: bytes) -> str:
    """
    Step 4: Pack an HD key into the standard 78-byte extended key format,
    then Base58Check-encode it into an "xprv..."/"xpub..." string.
        version (4 bytes) || depth (1) || parent_fingerprint (4) ||
        child_number (4) || chain_code (32) || key_data (33) = 78 bytes
    key_data is 0x00 + the 32-byte private key for xprv, or the 33-byte
    compressed public key for xpub - both are exactly 33 bytes, which is
    what keeps the two formats a fixed, uniform length.
    """
    payload = (
        version.to_bytes(4, byteorder='big')
        + depth.to_bytes(1, byteorder='big')
        + parent_fingerprint
        + child_number.to_bytes(4, byteorder='big')
        + chain_code
        + key_data
    )
    with contextlib.redirect_stdout(io.StringIO()):
        encoded = encode_check(payload)

    print(f"4. Extended key ({'private' if version == VERSION_PRIVATE else 'public'}): {encoded}")
    return encoded


def serialize_private_key(private_key: int, chain_code: bytes, depth: int, parent_fingerprint: bytes, child_number: int) -> str:
    key_data = b'\x00' + private_key.to_bytes(32, byteorder='big')
    return serialize_extended_key(VERSION_PRIVATE, depth, parent_fingerprint, child_number, chain_code, key_data)


def serialize_public_key(public_key_point, chain_code: bytes, depth: int, parent_fingerprint: bytes, child_number: int) -> str:
    key_data = _compressed_pubkey_bytes_from_point(public_key_point)
    return serialize_extended_key(VERSION_PUBLIC, depth, parent_fingerprint, child_number, chain_code, key_data)


if __name__ == "__main__":
    from bip32_steps.step1_master_key import generate_master_key

    with contextlib.redirect_stdout(io.StringIO()):
        master_key, master_chain_code = generate_master_key(bytes.fromhex("000102030405060708090a0b0c0d0e0f"))
        master_public_key = scalar_multiply(master_key, (GX, GY))

    serialize_private_key(master_key, master_chain_code, 0, b'\x00\x00\x00\x00', 0)
    serialize_public_key(master_public_key, master_chain_code, 0, b'\x00\x00\x00\x00', 0)
