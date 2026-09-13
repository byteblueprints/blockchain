import secrets

# BIP39 allows entropy lengths of 128, 160, 192, 224, or 256 bits, giving
# mnemonics of 12, 15, 18, 21, or 24 words respectively (each 32 bits of
# entropy adds 3 words). 128 bits (12 words) is the most common choice.
VALID_ENTROPY_BITS = (128, 160, 192, 224, 256)


def generate_entropy(bits: int = 128) -> bytes:
    """
    Step 1: Generate secure random entropy for a new mnemonic.
    Same reasoning as the ECC private key generator (06_ecc) - this is
    the one place "bare metal" should mean "use the OS's cryptographically
    secure source" via `secrets`, not hand-roll an RNG. Everything after
    this step is deterministic; only this step needs to be unpredictable.
    """
    if bits not in VALID_ENTROPY_BITS:
        raise ValueError(f"entropy bits must be one of {VALID_ENTROPY_BITS}, got {bits}")

    entropy = secrets.token_bytes(bits // 8)

    print(f"1. Entropy ({bits} bits): {entropy.hex()}")
    return entropy


if __name__ == "__main__":
    generate_entropy(128)
