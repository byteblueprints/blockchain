import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))

from sha512_basic_operation.rot64 import rot64
from sha512_basic_operation.shr64 import shr64
from sha512_basic_operation.xor import xor


def sigma1(x) -> str:
    """
    SHA-512 lower-case sigma1 function.
    sigma1(x) = ROT19(x) XOR ROT61(x) XOR SHR6(x)
    """
    rot19 = int(rot64(x, 19), 2)
    rot61 = int(rot64(x, 61), 2)
    shr6 = int(shr64(x, 6), 2)

    step = int(xor(rot19, rot61), 2)
    result = xor(step, shr6)
    return result


if __name__ == "__main__":
    sigma1(2 ** 64 - 1)
