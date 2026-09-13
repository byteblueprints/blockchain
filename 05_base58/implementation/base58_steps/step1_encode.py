import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from base58_constants import ALPHABET, BASE


def encode(data: bytes) -> str:
    """
    Step 1: Encode bytes as a Base58 string.

    This is arbitrary-precision base conversion: read the bytes as one big
    big-endian integer, then repeatedly divide by 58, using the remainder
    each time to pick a character - the same way you'd convert to binary
    or hex by hand, just with a 58-symbol alphabet instead of 2 or 16.

    Leading zero bytes need special handling: they carry no value once
    converted to an integer (0x00 = 0, same as no bytes at all), but they
    still need to show up in the output, so each one becomes a leading
    '1' (the alphabet's zero-value character) instead.
    """
    leading_zero_count = 0
    for byte in data:
        if byte == 0:
            leading_zero_count += 1
        else:
            break

    number = int.from_bytes(data, byteorder='big')

    digits = []
    while number > 0:
        number, remainder = divmod(number, BASE)
        digits.append(ALPHABET[remainder])

    encoded = ALPHABET[0] * leading_zero_count + ''.join(reversed(digits))

    print(f"1. Encode: {data.hex()} -> {encoded}")
    return encoded


if __name__ == "__main__":
    encode(bytes.fromhex("00010966776006953D5567439E5E39F86A0D273BEED61967F6"))
