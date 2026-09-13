# WHY these specific numbers: same "nothing up my sleeve" reasoning as the
# K constants (see generate_k_constants.py) - square roots of the first
# primes instead of cube roots, which is what separates the initial hash
# values (H0) from the per-round constants (K). Anyone can recompute them
# from "square root of 2, 3, 5, ..." - there is nothing hidden to trust.

from decimal import Decimal, getcontext

getcontext().prec = 60

TWO_POW_32 = Decimal(2) ** 32
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


def generate_h_constants(count: int = 8) -> list:
    """
    Generates the SHA-256 initial hash values (H0).

    For each of the first `count` prime numbers:
      1. Take the square root of the prime.
      2. Take the fractional part of the square root.
      3. Scale the fractional part to a 32-bit integer (multiply by 2**32).
    """
    constants = []
    for prime in _first_n_primes(count):
        square_root = Decimal(prime) ** SQUARE_ROOT_EXPONENT
        fractional_part = square_root - int(square_root)
        scaled = int(fractional_part * TWO_POW_32)
        binary = format(scaled, '032b')

        print(f"Prime:            {prime}")
        print(f"Square root:      {square_root}")
        print(f"Fractional part:  {fractional_part}")
        print(f"Scaled (32-bit):  {scaled}")
        print(f"Binary (32-bit):  {binary}")
        print()

        constants.append(scaled)
    return constants


if __name__ == "__main__":
    generate_h_constants()
