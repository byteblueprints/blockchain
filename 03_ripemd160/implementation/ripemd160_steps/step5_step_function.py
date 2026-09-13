import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from ripemd160_basic_operation.f1 import f1
from ripemd160_basic_operation.f2 import f2
from ripemd160_basic_operation.f3 import f3
from ripemd160_basic_operation.f4 import f4
from ripemd160_basic_operation.f5 import f5
from ripemd160_basic_operation.rol32 import rol32
from ripemd160_constants.tables import function_index_for_step

MASK = (1 << 32) - 1
FUNCTIONS = {1: f1, 2: f2, 3: f3, 4: f4, 5: f5}


def ripemd_step(a, b, c, d, e, step, x, k, s, is_right_line=False):
    """
    Step 5: One step of a RIPEMD-160 line (left or right).
    T = ROL_s(A + f(B,C,D) + X + K) + E
    Registers then shift: A'=E, B'=T, C'=B, D'=ROL10(C), E'=D
    """
    function_index = function_index_for_step(step, is_right_line)
    f_value = int(FUNCTIONS[function_index](b, c, d), 2)

    t = (a + f_value + x + k) & MASK
    t = int(rol32(t, s), 2)
    t = (t + e) & MASK

    new_c = int(rol32(c, 10), 2)

    print(f"5. Step {step} ({'right' if is_right_line else 'left'} line)")
    print(f"    T = {format(t, '032b')}")

    return e, t, b, new_c, d


if __name__ == "__main__":
    h0 = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
    example_word = int("01100001011000100110001110000000", 2)
    ripemd_step(*h0, step=0, x=example_word, k=0, s=11, is_right_line=False)
