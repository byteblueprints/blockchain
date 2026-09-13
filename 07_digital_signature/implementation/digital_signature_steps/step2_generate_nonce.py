import os
import sys
import secrets

_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "06_ecc", "implementation",
))
sys.path.append(_ECC_IMPLEMENTATION_DIR)

from ecc_constants.curve_parameters import N


def generate_nonce() -> int:
    """
    Step 2: Generate a secure random nonce k in [1, n-1] for this signature.

    SECURITY WARNING: k must be secret, random, and used EXACTLY ONCE per
    signature. If the same k is ever reused across two different signed
    messages (or if k is predictable), the private key can be recovered
    directly from the two signatures using basic algebra - this is exactly
    how Sony's PS3 signing key leaked in 2010. Using `secrets` (the same
    OS-backed CSPRNG as the private key generator) is the minimum bar; a
    production system would instead derive k deterministically from the
    private key and message (RFC 6979) to remove the "randomness must never
    fail" requirement entirely.
    """
    nonce = secrets.randbelow(N - 1) + 1

    print(f"2. Nonce (k): {hex(nonce)}")
    return nonce


if __name__ == "__main__":
    generate_nonce()
