def create_message_schedule(block: str) -> list:
    """
    Step 4: Split a 512-bit block into sixteen 32-bit words (W0..W15).
    """
    words = [block[i:i + 32] for i in range(0, 512, 32)]

    print("4. Create message schedule")
    for index, word in enumerate(words):
        print(f"    W{index:<3}= {word}")
    return words


if __name__ == "__main__":
    example_block = ("01100001011000100110001110000000" + "0" * 480)[:512]
    create_message_schedule(example_block)
