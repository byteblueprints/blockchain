# Same "nothing up my sleeve" reasoning as SHA-256's H0 (see 02_sha256) -
# fractional part of the square root of the first 8 primes, just scaled to
# 2**64 instead of 2**32 since SHA-512 works with 64-bit words.

from decimal import Decimal, getcontext
from functools import lru_cache

getcontext().prec = 60

TWO_POW_64 = Decimal(2) ** 64
SQUARE_ROOT_EXPONENT = Decimal(1) / Decimal(2)


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
def generate_h_constants(count: int = 8) -> list:
    """
    Generates the SHA-512 initial hash values (H0), 64-bit each.

    Cached for the same reason as generate_k_constants (see there) -
    this is Decimal arbitrary-precision arithmetic re-run on every SHA-512
    call otherwise, and PBKDF2 (11_pbkdf2) calls SHA-512 thousands of times.
    """
    constants = []
    for prime in _first_n_primes(count):
        square_root = Decimal(prime) ** SQUARE_ROOT_EXPONENT
        fractional_part = square_root - int(square_root)
        scaled = int(fractional_part * TWO_POW_64)
        binary = format(scaled, '064b')

        print(f"Prime:            {prime}")
        print(f"Square root:      {square_root}")
        print(f"Fractional part:  {fractional_part}")
        print(f"Scaled (64-bit):  {scaled}")
        print(f"Binary (64-bit):  {binary}")
        print()

        constants.append(scaled)
    return constants


if __name__ == "__main__":
    generate_h_constants()
