def get_message_blocks(padded_bits: str) -> list:
    """
    Step 3: Split the padded message into 512-bit blocks.
    If the padded message is longer than 512 bits, there will be
    multiple message blocks.
    """
    blocks = [padded_bits[i:i + 512] for i in range(0, len(padded_bits), 512)]

    for index, block in enumerate(blocks):
        print(f"3. Message Block {index}: {block}")
    return blocks


if __name__ == "__main__":
    import io
    import contextlib
    from step2_padding import pad_message

    with contextlib.redirect_stdout(io.StringIO()):
        padded = pad_message("011000010110001001100011")

    get_message_blocks(padded)
