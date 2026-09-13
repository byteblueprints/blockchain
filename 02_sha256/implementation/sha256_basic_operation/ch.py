def ch(x, y, z) -> str:
    """
    Choice operation (Ch).
    Accepts any inputs convertible to int, computes (x AND y) XOR (NOT x AND z),
    returns 32-bit binary string (no '0b' prefix).
    Prints the binary before and after.
    """
    x = int(x) % (1 << 32)
    y = int(y) % (1 << 32)
    z = int(z) % (1 << 32)
    before_x = format(x, '032b')
    before_y = format(y, '032b')
    before_z = format(z, '032b')
    not_x = (~x) & 0xFFFFFFFF
    result = (x & y) ^ (not_x & z)
    after = format(result, '032b')
    print(f"X:      {before_x}")
    print(f"Y:      {before_y}")
    print(f"Z:      {before_z}")
    print(f"CH:     {after}")
    return after
