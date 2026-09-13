import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "05_base58", "implementation")))

from wallet_steps.step1_hash160 import hash160
from base58_steps.step4_encode_check import encode_check

MAINNET_P2PKH_VERSION = 0x00


def generate_address(public_key_bytes: bytes, version: int = MAINNET_P2PKH_VERSION) -> str:
    """
    Step 2: Generate a P2PKH ("Pay to Public Key Hash") Bitcoin address.
    address = Base58Check(version_byte + HASH160(public_key))
    The version byte (0x00 for mainnet) is what makes an address
    recognizable as belonging to a particular network/address type just
    by its first character after Base58 encoding (mainnet addresses
    start with '1') - decoders check it before trusting the rest.
    """
    payload = bytes([version]) + hash160(public_key_bytes)
    address = encode_check(payload)

    print(f"2. Address: {address}")
    return address


if __name__ == "__main__":
    generate_address(bytes.fromhex("0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352"))
