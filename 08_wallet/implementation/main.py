import os
import sys

_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "06_ecc", "implementation"))
sys.path.append(_ECC_IMPLEMENTATION_DIR)

from ecc_steps import step4_generate_private_key, step5_generate_public_key, step6_key_encoding
from wallet_steps import step2_address, step3_wif


def generate_wallet():
    """
    Generates a full wallet: a fresh key pair (reusing 06_ecc), its
    compressed public key bytes, the corresponding P2PKH address, and
    both WIF encodings of the private key.
    """
    private_key = step4_generate_private_key.generate_private_key()
    public_key = step5_generate_public_key.generate_public_key(private_key)
    public_key_compressed = bytes.fromhex(step6_key_encoding.encode_public_key_compressed(public_key))

    address = step2_address.generate_address(public_key_compressed)
    wif_compressed = step3_wif.generate_wif(private_key, compressed=True)

    return {
        "private_key": private_key,
        "public_key_compressed": public_key_compressed.hex(),
        "address": address,
        "wif": wif_compressed,
    }


def main():
    wallet = generate_wallet()
    print()
    print(f"Private key:  {hex(wallet['private_key'])}")
    print(f"Public key:   {wallet['public_key_compressed']}")
    print(f"Address:      {wallet['address']}")
    print(f"WIF:          {wallet['wif']}")


if __name__ == "__main__":
    main()
