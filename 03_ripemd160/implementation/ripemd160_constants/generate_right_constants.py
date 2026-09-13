# WHY these specific numbers: same "nothing up my sleeve" reasoning as the
# left-line constants (see generate_left_constants.py) - cube roots instead
# of square roots is what separates the right line's constants from the
# left line's. Using a different irrational-root family for each line is a
# simple, transparent way to make the two lines behave differently while
# keeping both derivations equally trivial to verify.

from decimal import Decimal, getcontext

getcontext().prec = 60

TWO_POW_30 = Decimal(2) ** 30
CUBE_ROOT_EXPONENT = Decimal(1) / Decimal(3)
PRIMES = [2, 3, 5, 7]


def generate_right_constants() -> list:
    """
    Generates the RIPEMD-160 right-line round constants (one per round of 16 steps).
    K'(round) = floor(2**30 * cbrt(prime)), for prime in [2, 3, 5, 7], with a
    trailing 0 for round 5 (steps 64-79, no constant is added).
    """
    constants = []
    for prime in PRIMES:
        cube_root = Decimal(prime) ** CUBE_ROOT_EXPONENT
        scaled = int(cube_root * TWO_POW_30)
        binary = format(scaled, '032b')

        print(f"Prime:            {prime}")
        print(f"Cube root:        {cube_root}")
        print(f"Scaled (2^30):    {scaled}")
        print(f"Binary (32-bit):  {binary}")
        print()

        constants.append(scaled)
    constants.append(0)
    return constants


if __name__ == "__main__":
    generate_right_constants()
