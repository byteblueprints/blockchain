import os
import sys

_BIP39_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "12_bip39", "implementation",
))
sys.path.append(_BIP39_IMPLEMENTATION_DIR)

from bip39_steps.step1_generate_entropy import generate_entropy
from bip39_steps.step3_mnemonic import entropy_to_mnemonic


def new_mnemonic(bits: int = 128) -> str:
    """
    Step 1: Generate a fresh BIP39 mnemonic - this is the ONE thing in the
    whole HD wallet a person actually needs to write down and keep safe;
    everything else (every address, every private key) is deterministically
    re-derivable from it.
    """
    entropy = generate_entropy(bits)
    return entropy_to_mnemonic(entropy)


if __name__ == "__main__":
    new_mnemonic()
