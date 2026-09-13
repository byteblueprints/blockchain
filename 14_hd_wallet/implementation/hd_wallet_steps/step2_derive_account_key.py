import os
import sys

_BIP39_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "12_bip39", "implementation",
))
_BIP32_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "13_bip32", "implementation",
))
sys.path.append(_BIP39_IMPLEMENTATION_DIR)
sys.path.append(_BIP32_IMPLEMENTATION_DIR)

from bip39_steps.step4_seed import mnemonic_to_seed
from bip32_steps.step5_derive_path import derive_path

BITCOIN_MAINNET_COIN_TYPE = 0


def derive_account_private_key(mnemonic: str, passphrase: str = "", account: int = 0,
                                change: int = 0, address_index: int = 0,
                                coin_type: int = BITCOIN_MAINNET_COIN_TYPE) -> int:
    """
    Step 2: Turn a mnemonic into one specific private key, following the
    standard BIP44 path structure:
        m / 44' / coin_type' / account' / change / address_index

    WHY this exact shape (BIP44): it's what lets ANY wallet software agree
    on where a given coin's keys live inside the same seed - "44'" marks
    this as a BIP44-structured wallet, "coin_type'" separates Bitcoin (0)
    from other coins sharing the same seed, "account'" lets one seed hold
    multiple separate accounts, and "change" (0 = receiving, 1 = change/
    internal) separates addresses you'd hand out from ones the wallet
    uses internally for transaction change.
    """
    seed = mnemonic_to_seed(mnemonic, passphrase)
    path = f"m/44'/{coin_type}'/{account}'/{change}/{address_index}"

    private_key, _chain_code, _depth, _parent_fp, _child_number = derive_path(seed, path)

    print(f"2. Derived {path}: private key = {hex(private_key)}")
    return private_key


if __name__ == "__main__":
    derive_account_private_key(
        "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
    )
