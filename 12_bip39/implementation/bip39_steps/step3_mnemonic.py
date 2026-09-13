import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from bip39_wordlist import WORDLIST, WORD_TO_INDEX
from bip39_steps.step2_checksum import checksum_bits


def entropy_to_mnemonic(entropy: bytes) -> str:
    """
    Step 3: Turn entropy + its checksum into a mnemonic sentence.
    Concatenate entropy bits with the checksum bits, then read off 11-bit
    groups (2^11 = 2048, exactly the wordlist size) - each group is a
    direct index into the wordlist. 128 bits entropy + 4 bits checksum =
    132 bits = 12 words; 256 bits entropy + 8 bits checksum = 264 bits =
    24 words.
    """
    entropy_bits = ''.join(format(byte, '08b') for byte in entropy)
    all_bits = entropy_bits + checksum_bits(entropy)

    words = []
    for i in range(0, len(all_bits), 11):
        index = int(all_bits[i:i + 11], 2)
        words.append(WORDLIST[index])

    mnemonic = ' '.join(words)
    print(f"3. Mnemonic ({len(words)} words): {mnemonic}")
    return mnemonic


def mnemonic_to_entropy(mnemonic: str) -> bytes:
    """
    The inverse of entropy_to_mnemonic - also verifies the checksum,
    rejecting a mnemonic that's been mistyped or corrupted.
    """
    words = mnemonic.split()
    all_bits = ''.join(format(WORD_TO_INDEX[word], '011b') for word in words)

    checksum_length = len(all_bits) // 33
    entropy_bit_length = len(all_bits) - checksum_length

    entropy_bits = all_bits[:entropy_bit_length]
    given_checksum = all_bits[entropy_bit_length:]

    entropy = int(entropy_bits, 2).to_bytes(entropy_bit_length // 8, byteorder='big')
    expected_checksum = checksum_bits(entropy)

    if given_checksum != expected_checksum:
        raise ValueError("Invalid mnemonic: checksum mismatch")

    return entropy


if __name__ == "__main__":
    entropy_to_mnemonic(bytes(16))
