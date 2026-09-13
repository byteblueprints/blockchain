import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))

from sha256_basic_operation.rot32 import rot32
from sha256_basic_operation.shr32 import shr32
from sha256_basic_operation.xor import xor


def sigma0(x) -> str:
    """
    SHA-256 lower-case sigma0 function.
    sigma0(x) = ROT7(x) XOR ROT18(x) XOR SHR3(x)
    """
    rot7 = int(rot32(x, 7), 2)
    rot18 = int(rot32(x, 18), 2)
    shr3 = int(shr32(x, 3), 2)

    step = int(xor(rot7, rot18), 2)
    result = xor(step, shr3)
    return result


if __name__ == "__main__":
    sigma0(2147483647)
