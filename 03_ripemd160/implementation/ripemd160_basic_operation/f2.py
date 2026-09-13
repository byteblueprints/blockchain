def f2(x, y, z) -> str:
    """
    RIPEMD-160 round function 2 (steps 16-31 / 48-63).
    f2(x,y,z) = (x AND y) OR (NOT x AND z)
    """
    x = int(x) % (1 << 32)
    y = int(y) % (1 << 32)
    z = int(z) % (1 << 32)

    not_x = (~x) & 0xFFFFFFFF
    result = (x & y) | (not_x & z)
    after = format(result, '032b')

    print(f"X:      {format(x, '032b')}")
    print(f"Y:      {format(y, '032b')}")
    print(f"Z:      {format(z, '032b')}")
    print(f"F2:     {after}")
    return after
