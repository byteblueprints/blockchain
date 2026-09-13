def rot64(x, n) -> str:
    """
    Bitwise rotate right operation (64-bit).
    Accepts any input convertible to int, rotates right by n bits, returns 64-bit binary string (no '0b' prefix).
    Prints the binary before and after rotating.
    """
    x = int(x)
    n = int(n)
    before = format(x % (1 << 64), '064b')
    result = ((x % (1 << 64)) >> n) | ((x % (1 << 64)) << (64 - n) & 0xFFFFFFFFFFFFFFFF)
    after = format(result, '064b')
    print(f"Before: {before}")
    print(f"After : {after}")
    return after
