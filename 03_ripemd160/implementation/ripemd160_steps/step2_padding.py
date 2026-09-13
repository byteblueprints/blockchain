def pad_message(bits: str) -> str:
    """
    Step 2: Pad the message bits per the RIPEMD-160 spec.
    Append '1', then '0's until length % 512 == 448, then the original
    message length as a 64-bit LITTLE-ENDIAN integer (unlike SHA-256,
    which appends the length big-endian).
    """
    original_length = len(bits)
    padded = bits + '1'
    while len(padded) % 512 != 448:
        padded += '0'

    length_bytes_le = original_length.to_bytes(8, byteorder='little')
    length_bits = ''.join(format(byte, '08b') for byte in length_bytes_le)
    zero_padding = padded[original_length + 1:]
    padded += length_bits

    print(f"2. Padding: {bits}(1)<-separator ({zero_padding}) <- 448 bits ({length_bits}) <- 64 bit little-endian length of the message")
    return padded


if __name__ == "__main__":
    pad_message("011000010110001001100011")
