import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))

from sha256_basic_operation.rot32 import rot32
from sha256_basic_operation.xor import xor


def SIGMA1(x) -> str:
    """
    SHA-256 upper-case SIGMA1 function.
    SIGMA1(x) = ROT6(x) XOR ROT11(x) XOR ROT25(x)
    """
    rot6 = int(rot32(x, 6), 2)
    rot11 = int(rot32(x, 11), 2)
    rot25 = int(rot32(x, 25), 2)

    step = int(xor(rot6, rot11), 2)
    result = xor(step, rot25)
    return result


if __name__ == "__main__":
    SIGMA1(2147483647)
