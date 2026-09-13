import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))

from sha512_basic_operation.rot64 import rot64
from sha512_basic_operation.shr64 import shr64
from sha512_basic_operation.xor import xor


def sigma0(x) -> str:
    """
    SHA-512 lower-case sigma0 function.
    sigma0(x) = ROT1(x) XOR ROT8(x) XOR SHR7(x)
    """
    rot1 = int(rot64(x, 1), 2)
    rot8 = int(rot64(x, 8), 2)
    shr7 = int(shr64(x, 7), 2)

    step = int(xor(rot1, rot8), 2)
    result = xor(step, shr7)
    return result


if __name__ == "__main__":
    sigma0(2 ** 64 - 1)
