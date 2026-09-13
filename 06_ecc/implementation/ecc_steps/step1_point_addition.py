import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from ecc_basic_operation.mod_inverse import mod_inverse
from ecc_constants.curve_parameters import P


def point_add(point1, point2):
    """
    Step 1: Add two DISTINCT points on the elliptic curve (P != Q, and
    neither is the point at infinity / the other's negation).
    Geometrically: draw a line through point1 and point2, find where it
    crosses the curve a third time, then reflect that point over the x-axis.
        slope = (y2 - y1) * inverse(x2 - x1) mod p
        x3 = slope^2 - x1 - x2 mod p
        y3 = slope*(x1 - x3) - y1 mod p
    """
    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2:
        raise ValueError("point_add requires distinct x-coordinates; use point_double for P+P")

    slope = ((y2 - y1) * mod_inverse(x2 - x1, P)) % P
    x3 = (slope * slope - x1 - x2) % P
    y3 = (slope * (x1 - x3) - y1) % P

    print(f"P1:     ({hex(x1)}, {hex(y1)})")
    print(f"P2:     ({hex(x2)}, {hex(y2)})")
    print(f"slope:  {hex(slope)}")
    print(f"P1+P2:  ({hex(x3)}, {hex(y3)})")
    return (x3, y3)


if __name__ == "__main__":
    from ecc_constants.curve_parameters import GX, GY, A

    # Compute 2*G via the doubling formula inline (point_add itself only
    # handles two DISTINCT points), then add G + 2G = 3G as the demo.
    slope = ((3 * GX * GX + A) * mod_inverse(2 * GY, P)) % P
    double_x = (slope * slope - 2 * GX) % P
    double_y = (slope * (GX - double_x) - GY) % P

    point_add((GX, GY), (double_x, double_y))
