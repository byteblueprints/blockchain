import os
import sys
import io
import contextlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from sha256_constants.generate_h_constants import generate_h_constants

LABELS = "abcdefgh"


def get_initial_hash_values() -> list:
    """
    Step 6: Compression - H0 (initial hash values a..h), derived from the
    fractional part of the square root of the first 8 primes.
    """
    with contextlib.redirect_stdout(io.StringIO()):
        constants = generate_h_constants()

    print("6. Compression H0 (initial hash values)")
    for label, value in zip(LABELS, constants):
        print(f"    {label} = {format(value, '032b')}")
    return constants


if __name__ == "__main__":
    get_initial_hash_values()
