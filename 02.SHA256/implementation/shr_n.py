def shr_n(x, n) -> str:
    """
    Bitwise shift right operation (logical shift).
    Accepts any input convertible to int, shifts right by n bits, returns 32-bit binary string (no '0b' prefix).
    Prints the binary before and after shifting.
    """
    x = int(x)
    n = int(n)
    before = format(x % (1 << 32), '032b')
    result = (x % (1 << 32)) >> n
    after = format(result, '032b')
    print(f"Before: {before}")
    print(f"After : {after}")
    return after 
