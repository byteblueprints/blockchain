def word_to_little_endian_hex(value: int) -> str:
    return value.to_bytes(4, byteorder='little').hex()


def get_digest(hash_values: list) -> str:
    """
    Step 8: Assemble the final digest. RIPEMD-160 outputs each 32-bit word
    little-endian (byte-reversed), unlike SHA-256 which outputs big-endian.
    """
    digest = ''.join(word_to_little_endian_hex(value) for value in hash_values)
    print(f"8. Digest: {digest}")
    return digest


if __name__ == "__main__":
    example_hash = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
    get_digest(example_hash)
