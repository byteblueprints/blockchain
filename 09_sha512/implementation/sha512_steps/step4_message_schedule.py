def create_message_schedule(block: str) -> list:
    """
    Step 4: Split a 1024-bit block into sixteen 64-bit words (W0..W15).
    """
    words = [block[i:i + 64] for i in range(0, 1024, 64)]

    print("4. Create message schedule")
    for index, word in enumerate(words):
        print(f"    W{index:<3}= {word}")
    return words


if __name__ == "__main__":
    example_block = ("0110000101100010011000111000000" + "0" * 991)[:1024]
    create_message_schedule(example_block)
