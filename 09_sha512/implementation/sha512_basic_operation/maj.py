def maj(x, y, z) -> str:
    """
    Majority operation (Maj), 64-bit.
    Maj(x,y,z) = (x AND y) XOR (x AND z) XOR (y AND z)
    """
    x = int(x) % (1 << 64)
    y = int(y) % (1 << 64)
    z = int(z) % (1 << 64)

    result = (x & y) ^ (x & z) ^ (y & z)
    after = format(result, '064b')

    print(f"X:      {format(x, '064b')}")
    print(f"Y:      {format(y, '064b')}")
    print(f"Z:      {format(z, '064b')}")
    print(f"MAJ:    {after}")
    return after
