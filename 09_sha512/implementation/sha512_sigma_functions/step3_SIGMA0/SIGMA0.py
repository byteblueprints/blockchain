import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))

from sha512_basic_operation.rot64 import rot64
from sha512_basic_operation.xor import xor


def SIGMA0(x) -> str:
    """
    SHA-512 upper-case SIGMA0 function.
    SIGMA0(x) = ROT28(x) XOR ROT34(x) XOR ROT39(x)
    """
    rot28 = int(rot64(x, 28), 2)
    rot34 = int(rot64(x, 34), 2)
    rot39 = int(rot64(x, 39), 2)

    step = int(xor(rot28, rot34), 2)
    result = xor(step, rot39)
    return result


if __name__ == "__main__":
    SIGMA0(2 ** 64 - 1)
