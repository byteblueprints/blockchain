MASK = (1 << 64) - 1
LABELS = "abcdefgh"


def get_next_hash(initial_hash: list, compressed_registers: list) -> list:
    """
    Step 9: H1 = H0 + compressed registers (mod 2**64), word by word.
    """
    next_hash = [(h0 + reg) & MASK for h0, reg in zip(initial_hash, compressed_registers)]

    print("9. H1")
    for label, value in zip(LABELS, next_hash):
        print(f"    {label} = {format(value, '064b')}")
    return next_hash


if __name__ == "__main__":
    example_h0 = [
        0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
        0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b, 0x5be0cd19137e2179,
    ]
    example_compressed = list(example_h0)
    get_next_hash(example_h0, example_compressed)
