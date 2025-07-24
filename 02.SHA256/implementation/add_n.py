def add_n(x, y) -> str:
    """
    32-bit integer addition (modulo 2^32).
    Accepts any inputs convertible to int, adds them, returns 32-bit binary string (no '0b' prefix).
    Prints the binary before and after addition.
    """
    x = int(x)
    y = int(y)
    before_x = format(x % (1 << 32), '032b')
    before_y = format(y % (1 << 32), '032b')
    result = (x + y) % (1 << 32)
    after = format(result, '032b')
    print(f"X:      {before_x}")
    print(f"Y:      {before_y}")
    print(f"ADD:    {after}")
    return after 