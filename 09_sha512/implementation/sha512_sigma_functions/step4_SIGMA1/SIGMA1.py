import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))

from sha512_basic_operation.rot64 import rot64
from sha512_basic_operation.xor import xor


def SIGMA1(x) -> str:
    """
    SHA-512 upper-case SIGMA1 function.
    SIGMA1(x) = ROT14(x) XOR ROT18(x) XOR ROT41(x)
    """
    rot14 = int(rot64(x, 14), 2)
    rot18 = int(rot64(x, 18), 2)
    rot41 = int(rot64(x, 41), 2)

    step = int(xor(rot14, rot18), 2)
    result = xor(step, rot41)
    return result


if __name__ == "__main__":
    SIGMA1(2 ** 64 - 1)
