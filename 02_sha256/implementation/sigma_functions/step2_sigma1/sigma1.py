import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))

from sha256_basic_operation.rot32 import rot32
from sha256_basic_operation.shr32 import shr32
from sha256_basic_operation.xor import xor


def sigma1(x) -> str:
    """
    SHA-256 lower-case sigma1 function.
    sigma1(x) = ROT17(x) XOR ROT19(x) XOR SHR10(x)
    """
    rot17 = int(rot32(x, 17), 2)
    rot19 = int(rot32(x, 19), 2)
    shr10 = int(shr32(x, 10), 2)

    step = int(xor(rot17, rot19), 2)
    result = xor(step, shr10)
    return result


if __name__ == "__main__":
    sigma1(2147483647)
