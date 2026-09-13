def f3(x, y, z) -> str:
    """
    RIPEMD-160 round function 3 (steps 32-47, both lines).
    f3(x,y,z) = (x OR NOT y) XOR z
    """
    x = int(x) % (1 << 32)
    y = int(y) % (1 << 32)
    z = int(z) % (1 << 32)

    not_y = (~y) & 0xFFFFFFFF
    result = (x | not_y) ^ z
    after = format(result, '032b')

    print(f"X:      {format(x, '032b')}")
    print(f"Y:      {format(y, '032b')}")
    print(f"Z:      {format(z, '032b')}")
    print(f"F3:     {after}")
    return after
