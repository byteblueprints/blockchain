# WHY these specific numbers: they are "nothing up my sleeve" constants.
# Cube roots of small primes produce digit sequences that look statistically
# random (no discernible pattern an attacker could exploit), while being
# trivial for anyone to recompute and verify from a public, simple formula.
# This proves the designers didn't secretly hand-pick values that create a
# hidden mathematical weakness or backdoor - the constants are only as
# "special" as "cube root of 2, 3, 5, ...", nothing more.

from decimal import Decimal, getcontext

getcontext().prec = 60

TWO_POW_32 = Decimal(2) ** 32
CUBE_ROOT_EXPONENT = Decimal(1) / Decimal(3)


def _is_prime(candidate: int) -> bool:
    if candidate < 2:
        return False
    if candidate in (2, 3):
        return True
    if candidate % 2 == 0:
        return False
    for divisor in range(3, int(candidate ** 0.5) + 1, 2):
        if candidate % divisor == 0:
            return False
    return True


def _first_n_primes(n: int) -> list:
    primes = []
    candidate = 2
    while len(primes) < n:
        if _is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


def generate_k_constants(count: int = 64) -> list:
    """
    Generates the SHA-256 round constants (K).

    For each of the first `count` prime numbers:
      1. Take the cube root of the prime.
      2. Take the fractional part of the cube root.
      3. Scale the fractional part to a 32-bit integer (multiply by 2**32).
      4. Represent the result as a 32-bit binary string.

    Example (2nd prime is not used here, shown for the first prime, 2):
        Cube root of 2:                 1.2599210498948732...
        Fractional part:                0.2599210498948732...
        Scaled to 32-bit integer:       1116352408
        Binary (32-bit):                01000010100010100010111110011000
    """
    constants = []
    for prime in _first_n_primes(count):
        cube_root = Decimal(prime) ** CUBE_ROOT_EXPONENT
        fractional_part = cube_root - int(cube_root)
        scaled = int(fractional_part * TWO_POW_32)
        binary = format(scaled, '032b')

        print(f"Prime:            {prime}")
        print(f"Cube root:        {cube_root}")
        print(f"Fractional part:  {fractional_part}")
        print(f"Scaled (32-bit):  {scaled}")
        print(f"Binary (32-bit):  {binary}")
        print()

        constants.append(scaled)
    return constants


if __name__ == "__main__":
    generate_k_constants()
