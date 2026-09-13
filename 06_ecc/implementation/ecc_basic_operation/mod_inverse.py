def mod_inverse(a, m) -> int:
    """
    Modular multiplicative inverse of a mod m, via the Extended Euclidean
    Algorithm: finds x such that (a * x) % m == 1.
    This is "division" in a finite field - elliptic curve point arithmetic
    needs it to divide coordinates, since normal division doesn't exist
    modulo a prime.
    """
    a = int(a) % m
    if a == 0:
        raise ValueError("0 has no modular inverse")

    old_r, r = a, m
    old_s, s = 1, 0

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    if old_r != 1:
        raise ValueError(f"{a} has no inverse mod {m} (not coprime)")

    inverse = old_s % m

    print(f"a:        {hex(a)}")
    print(f"m:        {hex(m)}")
    print(f"inverse:  {hex(inverse)}")
    return inverse


if __name__ == "__main__":
    mod_inverse(3, 11)
