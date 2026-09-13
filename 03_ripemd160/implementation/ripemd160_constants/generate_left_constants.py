# WHY these specific numbers: "nothing up my sleeve" constants, same idea as
# SHA-256's K table. Square roots of the first few primes produce digit
# sequences with no discernible structure, so anyone can recompute and
# verify them from a trivial public formula - proving the designers didn't
# secretly pick values that hide a mathematical weakness. RIPEMD-160 scales
# by 2**30 (not 2**32 like SHA-256) and keeps the WHOLE value rather than
# just the fractional part, which is just a different convention, not a
# different security property.

from decimal import Decimal, getcontext

getcontext().prec = 60

TWO_POW_30 = Decimal(2) ** 30
SQUARE_ROOT_EXPONENT = Decimal(1) / Decimal(2)
PRIMES = [2, 3, 5, 7]


def generate_left_constants() -> list:
    """
    Generates the RIPEMD-160 left-line round constants (one per round of 16 steps).
    K(round) = floor(2**30 * sqrt(prime)), for prime in [2, 3, 5, 7], with an
    extra leading 0 for round 1 (steps 0-15, no constant is added).
    """
    constants = [0]
    for prime in PRIMES:
        square_root = Decimal(prime) ** SQUARE_ROOT_EXPONENT
        scaled = int(square_root * TWO_POW_30)
        binary = format(scaled, '032b')

        print(f"Prime:            {prime}")
        print(f"Square root:      {square_root}")
        print(f"Scaled (2^30):    {scaled}")
        print(f"Binary (32-bit):  {binary}")
        print()

        constants.append(scaled)
    return constants


if __name__ == "__main__":
    generate_left_constants()
