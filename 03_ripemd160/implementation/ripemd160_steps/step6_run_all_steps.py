import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from ripemd160_basic_operation.f1 import f1
from ripemd160_basic_operation.f2 import f2
from ripemd160_basic_operation.f3 import f3
from ripemd160_basic_operation.f4 import f4
from ripemd160_basic_operation.f5 import f5
from ripemd160_basic_operation.rol32 import rol32
from ripemd160_constants.generate_left_constants import generate_left_constants
from ripemd160_constants.generate_right_constants import generate_right_constants
from ripemd160_constants.tables import (
    LEFT_WORD_ORDER,
    RIGHT_WORD_ORDER,
    LEFT_ROTATION,
    RIGHT_ROTATION,
    function_index_for_step,
)

import io
import contextlib

MASK = (1 << 32) - 1
FUNCTIONS = {1: f1, 2: f2, 3: f3, 4: f4, 5: f5}


def _step(a, b, c, d, e, step, x, k, is_right_line):
    function_index = function_index_for_step(step, is_right_line)
    f_value = int(FUNCTIONS[function_index](b, c, d), 2)
    s = (RIGHT_ROTATION if is_right_line else LEFT_ROTATION)[step]

    with contextlib.redirect_stdout(io.StringIO()):
        t = int(rol32((a + f_value + x + k) & MASK, s), 2)
        t = (t + e) & MASK
        new_c = int(rol32(c, 10), 2)

    return e, t, b, new_c, d


def run_all_steps(initial_hash: list, schedule: list) -> tuple:
    """
    Step 6: Run all 160 steps (80 left + 80 right, in parallel) of the
    RIPEMD-160 compression function over one block's 16-word schedule.
    Returns the final left registers (a..e) and right registers (a'..e').
    """
    with contextlib.redirect_stdout(io.StringIO()):
        left_k = generate_left_constants()
        right_k = generate_right_constants()

    a1, b1, c1, d1, e1 = initial_hash
    a2, b2, c2, d2, e2 = initial_hash

    for step in range(80):
        round_number = step // 16
        left_word = schedule[LEFT_WORD_ORDER[step]]
        right_word = schedule[RIGHT_WORD_ORDER[step]]

        a1, b1, c1, d1, e1 = _step(a1, b1, c1, d1, e1, step, left_word, left_k[round_number], False)
        a2, b2, c2, d2, e2 = _step(a2, b2, c2, d2, e2, step, right_word, right_k[round_number], True)

    left = [a1, b1, c1, d1, e1]
    right = [a2, b2, c2, d2, e2]

    print("6. Final registers after 80 steps")
    print(f"    left  (a..e)  = {[format(v, '032b') for v in left]}")
    print(f"    right (a'..e') = {[format(v, '032b') for v in right]}")
    return left, right


if __name__ == "__main__":
    h0 = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
    example_schedule = [0] * 16
    example_schedule[0] = int("01100001011000100110001110000000", 2)
    run_all_steps(h0, example_schedule)
