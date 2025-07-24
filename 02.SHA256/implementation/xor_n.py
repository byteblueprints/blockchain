def xor_n(x, y) -> str:
    """
    Bitwise XOR operation.
    Accepts any inputs convertible to int, XORs them, returns 32-bit binary string (no '0b' prefix).
    Prints the binary before and after XOR.
    """
    x = int(x)
    y = int(y)
    before_x = format(x % (1 << 32), '032b')
    before_y = format(y % (1 << 32), '032b')
    result = (x % (1 << 32)) ^ (y % (1 << 32))
    after = format(result, '032b')
    print(f"X:      {before_x}")
    print(f"Y:      {before_y}")
    print(f"XOR:    {after}")
    return after 