def maj(x, y, z) -> str:
    """
    Majority operation (Maj).
    Accepts any inputs convertible to int, computes (x AND y) XOR (x AND z) XOR (y AND z),
    returns 32-bit binary string (no '0b' prefix).
    Prints the binary before and after.
    """
    x = int(x) % (1 << 32)
    y = int(y) % (1 << 32)
    z = int(z) % (1 << 32)
    before_x = format(x, '032b')
    before_y = format(y, '032b')
    before_z = format(z, '032b')
    result = (x & y) ^ (x & z) ^ (y & z)
    after = format(result, '032b')
    print(f"X:      {before_x}")
    print(f"Y:      {before_y}")
    print(f"Z:      {before_z}")
    print(f"MAJ:    {after}")
    return after
