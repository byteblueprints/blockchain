def pad_message(bits: str) -> str:
    """
    Step 2: Pad the message bits per the SHA-512 spec.
    Append '1', then '0's until length % 1024 == 896, then the original
    message length as a 128-bit big-endian integer (SHA-256 uses a 512-bit
    block and a 64-bit length field; SHA-512 doubles both to a 1024-bit
    block and a 128-bit length field, matching its 64-bit word size).
    """
    original_length = len(bits)
    padded = bits + '1'
    while len(padded) % 1024 != 896:
        padded += '0'

    length_bits = format(original_length, '0128b')
    zero_padding = padded[original_length + 1:]
    padded += length_bits

    print(f"2. Padding: {bits}(1)<-separator ({zero_padding}) <- 896 bits ({length_bits}) <- 128 bit length of the message")
    return padded


if __name__ == "__main__":
    pad_message("011000010110001001100011")
