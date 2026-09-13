import os
import sys
import unicodedata

_PBKDF2_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "11_pbkdf2", "implementation",
))
sys.path.append(_PBKDF2_IMPLEMENTATION_DIR)

from pbkdf2_steps.step2_derive_key import derive_key

PBKDF2_ITERATIONS = 2048
SEED_LENGTH = 64


def mnemonic_to_seed(mnemonic: str, passphrase: str = "") -> bytes:
    """
    Step 4: Derive the 64-byte seed from a mnemonic (and optional
    passphrase) via PBKDF2-HMAC-SHA512.
        seed = PBKDF2(password=mnemonic, salt="mnemonic"+passphrase, iterations=2048, dklen=64)

    Unicode NFKD normalization matters here: the same phrase can be
    represented as different byte sequences depending on how accented
    characters are encoded, and two wallets that normalize differently
    would derive different seeds from what looks like the same phrase to
    a human. NFKD is the specific form the BIP39 spec mandates.

    The optional passphrase is sometimes called a "25th word" - it's not
    part of the mnemonic itself, but changing it produces an entirely
    different, valid-looking wallet from the same 12/24 words, which is
    used both for extra security and for plausible-deniability "hidden"
    wallets.
    """
    normalized_mnemonic = unicodedata.normalize("NFKD", mnemonic)
    normalized_salt = unicodedata.normalize("NFKD", "mnemonic" + passphrase)

    seed = derive_key(
        normalized_mnemonic.encode("utf-8"),
        normalized_salt.encode("utf-8"),
        PBKDF2_ITERATIONS,
        SEED_LENGTH,
    )

    print(f"4. Seed: {seed.hex()}")
    return seed


if __name__ == "__main__":
    mnemonic_to_seed("abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about")
