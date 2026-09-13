from hd_wallet_steps import step1_new_mnemonic, step2_derive_account_key, step3_wallet_from_key


def create_hd_wallet(mnemonic: str | None = None, passphrase: str = "", address_index: int = 0) -> dict:
    """
    The full standard flow: mnemonic -> BIP39 seed -> BIP32 derivation
    (BIP44 path) -> private key -> address + WIF. Generates a fresh
    mnemonic if none is given.
    """
    if mnemonic is None:
        mnemonic = step1_new_mnemonic.new_mnemonic()

    private_key = step2_derive_account_key.derive_account_private_key(
        mnemonic, passphrase, address_index=address_index,
    )
    wallet = step3_wallet_from_key.wallet_from_private_key(private_key)
    wallet["mnemonic"] = mnemonic
    return wallet


def main():
    wallet = create_hd_wallet()
    print()
    print(f"Mnemonic: {wallet['mnemonic']}")
    print(f"Private key: {hex(wallet['private_key'])}")
    print(f"Address:     {wallet['address']}")
    print(f"WIF:         {wallet['wif']}")


if __name__ == "__main__":
    main()
