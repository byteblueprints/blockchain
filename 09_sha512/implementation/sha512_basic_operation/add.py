def add(x, y) -> str:
    """
    64-bit integer addition (modulo 2^64).
    Accepts any inputs convertible to int, adds them, returns 64-bit binary string (no '0b' prefix).
    Prints the binary before and after addition.
    """
    x = int(x)
    y = int(y)
    before_x = format(x % (1 << 64), '064b')
    before_y = format(y % (1 << 64), '064b')
    result = (x + y) % (1 << 64)
    after = format(result, '064b')
    print(f"X:      {before_x}")
    print(f"Y:      {before_y}")
    print(f"ADD:    {after}")
    return after
