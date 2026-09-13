def f5(x, y, z) -> str:
    """
    RIPEMD-160 round function 5 (steps 64-79 / 0-15).
    f5(x,y,z) = x XOR (y OR NOT z)
    """
    x = int(x) % (1 << 32)
    y = int(y) % (1 << 32)
    z = int(z) % (1 << 32)

    not_z = (~z) & 0xFFFFFFFF
    result = x ^ (y | not_z)
    after = format(result, '032b')

    print(f"X:      {format(x, '032b')}")
    print(f"Y:      {format(y, '032b')}")
    print(f"Z:      {format(z, '032b')}")
    print(f"F5:     {after}")
    return after
