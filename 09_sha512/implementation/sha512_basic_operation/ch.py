def ch(x, y, z) -> str:
    """
    Choice operation (Ch), 64-bit.
    Ch(x,y,z) = (x AND y) XOR (NOT x AND z)
    """
    x = int(x) % (1 << 64)
    y = int(y) % (1 << 64)
    z = int(z) % (1 << 64)

    not_x = (~x) & 0xFFFFFFFFFFFFFFFF
    result = (x & y) ^ (not_x & z)
    after = format(result, '064b')

    print(f"X:      {format(x, '064b')}")
    print(f"Y:      {format(y, '064b')}")
    print(f"Z:      {format(z, '064b')}")
    print(f"CH:     {after}")
    return after
