def create_message_schedule(block: str) -> list:
    """
    Step 4: Split a 512-bit block into sixteen 32-bit words (W0..W15).
    RIPEMD-160 assembles each word LITTLE-ENDIAN: the 4 bytes of a word
    are byte-reversed before being read as a 32-bit value (unlike
    SHA-256, which reads them big-endian / in stream order).
    """
    words = []
    for i in range(0, 512, 32):
        chunk = block[i:i + 32]
        byte_group = [chunk[b:b + 8] for b in range(0, 32, 8)]
        little_endian_word = ''.join(reversed(byte_group))
        words.append(little_endian_word)

    print("4. Create message schedule")
    for index, word in enumerate(words):
        print(f"    W{index:<3}= {word}")
    return words


if __name__ == "__main__":
    example_block = ("01100001011000100110001110000000" + "0" * 480)[:512]
    create_message_schedule(example_block)
