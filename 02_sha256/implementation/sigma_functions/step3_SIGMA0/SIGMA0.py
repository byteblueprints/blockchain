import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))

from sha256_basic_operation.rot32 import rot32
from sha256_basic_operation.xor import xor


def SIGMA0(x) -> str:
    """
    SHA-256 upper-case SIGMA0 function.
    SIGMA0(x) = ROT2(x) XOR ROT13(x) XOR ROT22(x)
    """
    rot2 = int(rot32(x, 2), 2)
    rot13 = int(rot32(x, 13), 2)
    rot22 = int(rot32(x, 22), 2)

    step = int(xor(rot2, rot13), 2)
    result = xor(step, rot22)
    return result


if __name__ == "__main__":
    SIGMA0(2147483647)
