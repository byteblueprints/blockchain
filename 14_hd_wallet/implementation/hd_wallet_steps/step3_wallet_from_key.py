import os
import sys

_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "06_ecc", "implementation",
))
_WALLET_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "08_wallet", "implementation",
))
sys.path.append(_ECC_IMPLEMENTATION_DIR)
sys.path.append(_WALLET_IMPLEMENTATION_DIR)

from ecc_steps import step5_generate_public_key, step6_key_encoding
from wallet_steps import step2_address, step3_wif


def wallet_from_private_key(private_key: int) -> dict:
    """
    Step 3: The exact same private-key -> address/WIF pipeline as the
    non-HD wallet (08_wallet) - this is the point made earlier: an HD
    wallet only changes WHERE the private key comes from, not what's done
    with it afterward.
    """
    public_key = step5_generate_public_key.generate_public_key(private_key)
    public_key_compressed = bytes.fromhex(step6_key_encoding.encode_public_key_compressed(public_key))

    address = step2_address.generate_address(public_key_compressed)
    wif = step3_wif.generate_wif(private_key, compressed=True)

    return {
        "private_key": private_key,
        "public_key_compressed": public_key_compressed.hex(),
        "address": address,
        "wif": wif,
    }


if __name__ == "__main__":
    wallet_from_private_key(1)
