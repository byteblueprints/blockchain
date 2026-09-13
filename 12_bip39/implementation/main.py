from bip39_steps import step1_generate_entropy, step3_mnemonic, step4_seed


def generate_mnemonic(bits: int = 128) -> str:
    """Generates a fresh, valid BIP39 mnemonic sentence."""
    entropy = step1_generate_entropy.generate_entropy(bits)
    return step3_mnemonic.entropy_to_mnemonic(entropy)


def main():
    mnemonic = generate_mnemonic(128)
    seed = step4_seed.mnemonic_to_seed(mnemonic)

    print()
    print(f"Mnemonic: {mnemonic}")
    print(f"Seed:     {seed.hex()}")


if __name__ == "__main__":
    main()
