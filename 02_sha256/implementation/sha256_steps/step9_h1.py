MASK = (1 << 32) - 1
LABELS = "abcdefgh"


def get_next_hash(initial_hash: list, compressed_registers: list) -> list:
    """
    Step 9: H1 = H0 + compressed registers (mod 2**32), word by word.
    This is the running hash value carried into the next message block,
    or the final digest if this was the last block.
    """
    next_hash = [(h0 + reg) & MASK for h0, reg in zip(initial_hash, compressed_registers)]

    print("9. H1")
    for label, value in zip(LABELS, next_hash):
        print(f"    {label} = {format(value, '032b')}")
    return next_hash


if __name__ == "__main__":
    example_h0 = [
        1779033703, 3144134277, 1013904242, 2773480762,
        1359893119, 2600822924, 528734635, 1541459225,
    ]
    example_compressed = list(example_h0)
    get_next_hash(example_h0, example_compressed)
