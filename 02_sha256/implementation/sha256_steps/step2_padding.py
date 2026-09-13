def pad_message(bits: str) -> str:
    """
    Step 2: Pad the message bits per the SHA-256 spec.
    Append '1', then '0's until length % 512 == 448, then the original
    message length as a 64-bit big-endian integer.
    """
    original_length = len(bits)
    padded = bits + '1'
    while len(padded) % 512 != 448:
        padded += '0'

    length_bits = format(original_length, '064b')
    zero_padding = padded[original_length + 1:]
    padded += length_bits

    print(f"2. Padding: {bits}(1)<-separator ({zero_padding}) <- 448 bits ({length_bits}) <- 64 bit length of the message")
    return padded


if __name__ == "__main__":
    pad_message("011000010110001001100011")
