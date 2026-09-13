# Same "nothing up my sleeve" reasoning as SHA-256's K (see 02_sha256) -
# fractional part of the cube root of the first 80 primes (SHA-512 has 80
# rounds, not 64), scaled to 2**64 instead of 2**32.

from decimal import Decimal, getcontext
from functools import lru_cache

getcontext().prec = 60

TWO_POW_64 = Decimal(2) ** 64
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


@lru_cache(maxsize=None)
def generate_k_constants(count: int = 80) -> list:
    """
    Generates the SHA-512 round constants (K), 64-bit each, one per round
    (80 rounds).

    Cached: this does real Decimal arbitrary-precision arithmetic (cube
    roots at 60-digit precision), and SHA-512 is hashed thousands of times
    over by PBKDF2 (see 11_pbkdf2) - recomputing these on every single
    hash call would make that thousands of times slower for no reason,
    since the constants are always the same values.
    """
    constants = []
    for prime in _first_n_primes(count):
        cube_root = Decimal(prime) ** CUBE_ROOT_EXPONENT
        fractional_part = cube_root - int(cube_root)
        scaled = int(fractional_part * TWO_POW_64)
        binary = format(scaled, '064b')

        print(f"Prime:            {prime}")
        print(f"Cube root:        {cube_root}")
        print(f"Fractional part:  {fractional_part}")
        print(f"Scaled (64-bit):  {scaled}")
        print(f"Binary (64-bit):  {binary}")
        print()

        constants.append(scaled)
    return constants


if __name__ == "__main__":
    generate_k_constants()
