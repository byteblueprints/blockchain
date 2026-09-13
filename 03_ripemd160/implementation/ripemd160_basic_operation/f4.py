def f4(x, y, z) -> str:
    """
    RIPEMD-160 round function 4 (steps 48-63 / 16-31).
    f4(x,y,z) = (x AND z) OR (y AND NOT z)
    """
    x = int(x) % (1 << 32)
    y = int(y) % (1 << 32)
    z = int(z) % (1 << 32)

    not_z = (~z) & 0xFFFFFFFF
    result = (x & z) | (y & not_z)
    after = format(result, '032b')

    print(f"X:      {format(x, '032b')}")
    print(f"Y:      {format(y, '032b')}")
    print(f"Z:      {format(z, '032b')}")
    print(f"F4:     {after}")
    return after
