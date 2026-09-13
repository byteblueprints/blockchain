import os
import sys
import secrets

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from ecc_constants.curve_parameters import N


def generate_private_key() -> int:
    """
    Step 4: Generate a private key - a secure random integer in [1, n-1].

    WHY secrets, not a hand-rolled RNG: everywhere else in this project we
    hand-build the algorithm because determinism was the whole point (same
    input must give the same, verifiable output). A private key needs the
    opposite property - unpredictability. Writing our own RNG here would be
    actively wrong: it's the one primitive where "bare metal" should mean
    "use the operating system's cryptographically secure source", not
    "invent your own". `secrets` wraps that OS source.
    """
    private_key = secrets.randbelow(N - 1) + 1

    print(f"4. Private key: {hex(private_key)}")
    return private_key


if __name__ == "__main__":
    generate_private_key()
