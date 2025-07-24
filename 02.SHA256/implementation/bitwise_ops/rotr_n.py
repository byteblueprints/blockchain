def rotr_n(x, n) -> str:
    """
    Bitwise rotate right operation.
    Accepts any input convertible to int, rotates right by n bits, returns 32-bit binary string (no '0b' prefix).
    Prints the binary before and after rotating.
    """
    x = int(x)
    n = int(n)
    before = format(x % (1 << 32), '032b')
    result = ((x % (1 << 32)) >> n) | ((x % (1 << 32)) << (32 - n) & 0xFFFFFFFF)
    after = format(result, '032b')
    print(f"Before: {before}")
    print(f"After : {after}")
    return after 