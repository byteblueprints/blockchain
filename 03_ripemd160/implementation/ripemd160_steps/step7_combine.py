MASK = (1 << 32) - 1


def combine(previous_hash: list, left: list, right: list) -> list:
    """
    Step 7: Combine the left/right line final registers with the previous
    hash state into the next hash state. Unlike SHA-256's simple add-back,
    RIPEMD-160 cross-mixes left and right registers in a rotated pattern:

        T  = h1 + c1 + d2
        h1 = h2 + d1 + e2
        h2 = h3 + e1 + a2
        h3 = h4 + a1 + b2
        h4 = h0 + b1 + c2
        h0 = T
    """
    h0, h1, h2, h3, h4 = previous_hash
    a1, b1, c1, d1, e1 = left
    a2, b2, c2, d2, e2 = right

    next_hash = [
        (h1 + c1 + d2) & MASK,
        (h2 + d1 + e2) & MASK,
        (h3 + e1 + a2) & MASK,
        (h4 + a1 + b2) & MASK,
        (h0 + b1 + c2) & MASK,
    ]

    print("7. Combine -> next hash state")
    for index, value in enumerate(next_hash):
        print(f"    h{index} = {format(value, '032b')}")
    return next_hash


if __name__ == "__main__":
    h0 = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
    combine(h0, h0, h0)
