import os
import sys

_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "06_ecc", "implementation"))
sys.path.append(_ECC_IMPLEMENTATION_DIR)

from ecc_constants.curve_parameters import N, GX, GY
from ecc_basic_operation.mod_inverse import mod_inverse
from ecc_steps.step1_point_addition import point_add
from ecc_steps.step2_point_doubling import point_double
from ecc_steps.step3_scalar_multiplication import scalar_multiply

import io
import contextlib


def verify(public_key, z: int, signature) -> bool:
    """
    Step 4: Verify a signature (r, s) against a message hash z and a
    public key.
        w = s^-1 mod n
        (x, y) = (z*w)*G + (r*w)*public_key
        valid if x mod n == r
    A forged signature would need to know the private key to produce an
    (r, s) pair that survives this check - that's the whole point.
    """
    r, s = signature
    if not (1 <= r <= N - 1 and 1 <= s <= N - 1):
        print("4. Verify: INVALID (r or s out of range)")
        return False

    with contextlib.redirect_stdout(io.StringIO()):
        w = mod_inverse(s, N)
        u1 = (z * w) % N
        u2 = (r * w) % N

        point1 = scalar_multiply(u1, (GX, GY))
        point2 = scalar_multiply(u2, public_key)

        combined = point_double(point1) if point1 == point2 else point_add(point1, point2)

    is_valid = (combined[0] % N) == r

    print(f"4. Verify: {'VALID' if is_valid else 'INVALID'}")
    return is_valid


if __name__ == "__main__":
    verify((GX, GY), 0xba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad, (1, 1))
