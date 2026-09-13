import os
import sys
import io
import contextlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from ecc_steps.step1_point_addition import point_add
from ecc_steps.step2_point_doubling import point_double


def scalar_multiply(k: int, point):
    """
    Step 3: Compute k * point using the right-to-left double-and-add
    algorithm - the elliptic curve equivalent of fast exponentiation.
    Walks the bits of k from least to most significant: doubles a running
    "current" point every step (current = 2^i * point), and folds it into
    the accumulating result whenever that bit of k is 1. This turns a
    private key (a huge integer) into a public key (a point) in roughly
    log2(k) steps instead of k steps.
    """
    if k == 0:
        raise ValueError("scalar_multiply(0, point) is the point at infinity, not representable here")

    result = None  # point at infinity (identity element)
    current = point

    with contextlib.redirect_stdout(io.StringIO()):
        for bit in reversed(bin(k)[2:]):
            if bit == '1':
                if result is None:
                    result = current
                elif result == current:
                    result = point_double(current)
                else:
                    result = point_add(result, current)
            current = point_double(current)

    print(f"k:        {hex(k)}")
    print(f"k*point:  ({hex(result[0])}, {hex(result[1])})")
    return result


if __name__ == "__main__":
    from ecc_constants.curve_parameters import GX, GY

    scalar_multiply(2, (GX, GY))
