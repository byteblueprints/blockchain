import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from ecc_basic_operation.mod_inverse import mod_inverse
from ecc_constants.curve_parameters import P, A


def point_double(point):
    """
    Step 2: Add a point to itself (P + P), using the tangent line at P
    instead of a line through two distinct points.
        slope = (3*x1^2 + a) * inverse(2*y1) mod p
        x3 = slope^2 - 2*x1 mod p
        y3 = slope*(x1 - x3) - y1 mod p
    """
    x1, y1 = point

    slope = ((3 * x1 * x1 + A) * mod_inverse(2 * y1, P)) % P
    x3 = (slope * slope - 2 * x1) % P
    y3 = (slope * (x1 - x3) - y1) % P

    print(f"P:      ({hex(x1)}, {hex(y1)})")
    print(f"slope:  {hex(slope)}")
    print(f"2P:     ({hex(x3)}, {hex(y3)})")
    return (x3, y3)


if __name__ == "__main__":
    from ecc_constants.curve_parameters import GX, GY

    point_double((GX, GY))
