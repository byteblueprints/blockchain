def xor(x, y) -> str:
    """
    Bitwise XOR operation (64-bit).
    Accepts any inputs convertible to int, XORs them, returns 64-bit binary string (no '0b' prefix).
    Prints the binary before and after XOR.
    """
    x = int(x)
    y = int(y)
    before_x = format(x % (1 << 64), '064b')
    before_y = format(y % (1 << 64), '064b')
    result = (x % (1 << 64)) ^ (y % (1 << 64))
    after = format(result, '064b')
    print(f"X:      {before_x}")
    print(f"Y:      {before_y}")
    print(f"XOR:    {after}")
    return after
