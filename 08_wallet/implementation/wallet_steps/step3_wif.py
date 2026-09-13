import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "05_base58", "implementation")))

from base58_steps.step4_encode_check import encode_check

MAINNET_WIF_VERSION = 0x80
COMPRESSED_FLAG = b'\x01'


def generate_wif(private_key: int, compressed: bool = True, version: int = MAINNET_WIF_VERSION) -> str:
    """
    Step 3: Generate the Wallet Import Format (WIF) encoding of a private key.
    WIF = Base58Check(version_byte + private_key_bytes [+ 0x01 if compressed])
    The trailing 0x01 flag isn't part of the private key value itself - it
    just tells the importing wallet whether to derive the COMPRESSED or
    UNCOMPRESSED public key from this private key, since both give
    different (but equally valid) addresses for the same private key.
    """
    private_key_bytes = private_key.to_bytes(32, byteorder='big')
    payload = bytes([version]) + private_key_bytes
    if compressed:
        payload += COMPRESSED_FLAG

    wif = encode_check(payload)

    print(f"3. WIF ({'compressed' if compressed else 'uncompressed'}): {wif}")
    return wif


if __name__ == "__main__":
    generate_wif(0x18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725, compressed=False)
    generate_wif(0x18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725, compressed=True)
