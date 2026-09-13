def rol32(x, n) -> str:
    """
    Bitwise rotate left operation.
    Accepts any input convertible to int, rotates left by n bits, returns 32-bit binary string (no '0b' prefix).
    Prints the binary before and after rotating.
    """
    x = int(x)
    n = int(n)
    before = format(x % (1 << 32), '032b')
    result = ((x % (1 << 32)) << n & 0xFFFFFFFF) | ((x % (1 << 32)) >> (32 - n))
    after = format(result, '032b')
    print(f"Before: {before}")
    print(f"After : {after}")
    return after
