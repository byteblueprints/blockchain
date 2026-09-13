def f1(x, y, z) -> str:
    """
    RIPEMD-160 round function 1 (steps 0-15 / 64-79).
    f1(x,y,z) = x XOR y XOR z
    """
    x = int(x) % (1 << 32)
    y = int(y) % (1 << 32)
    z = int(z) % (1 << 32)

    result = x ^ y ^ z
    after = format(result, '032b')

    print(f"X:      {format(x, '032b')}")
    print(f"Y:      {format(y, '032b')}")
    print(f"Z:      {format(z, '032b')}")
    print(f"F1:     {after}")
    return after
