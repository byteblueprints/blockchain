import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from base58_constants import ALPHABET, BASE


def decode(text: str) -> bytes:
    """
    Step 2: Decode a Base58 string back into bytes - the inverse of encode.

    Each character contributes value = ALPHABET.index(char), accumulated as
    number = number * 58 + value, same as reading a normal base-10 number
    digit by digit but with base 58. Leading '1' characters are the
    encoded form of leading zero bytes, so they're converted back directly
    rather than through the integer (0 * 58 + 0 = 0 either way, but a
    leading zero BYTE would otherwise vanish once everything is one
    giant integer with no fixed length).
    """
    leading_one_count = 0
    for char in text:
        if char == ALPHABET[0]:
            leading_one_count += 1
        else:
            break

    number = 0
    for char in text:
        number = number * BASE + ALPHABET.index(char)

    if number == 0:
        body = b''
    else:
        body = number.to_bytes((number.bit_length() + 7) // 8, byteorder='big')

    decoded = b'\x00' * leading_one_count + body

    print(f"2. Decode: {text} -> {decoded.hex()}")
    return decoded


if __name__ == "__main__":
    decode("16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM")
