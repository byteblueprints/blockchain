def shr64(x, n) -> str:
    """
    Bitwise shift right operation (logical shift, 64-bit).
    Accepts any input convertible to int, shifts right by n bits, returns 64-bit binary string (no '0b' prefix).
    Prints the binary before and after shifting.
    """
    x = int(x)
    n = int(n)
    before = format(x % (1 << 64), '064b')
    result = (x % (1 << 64)) >> n
    after = format(result, '064b')
    print(f"Before: {before}")
    print(f"After : {after}")
    return after
