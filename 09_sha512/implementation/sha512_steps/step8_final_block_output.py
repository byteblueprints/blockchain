import os
import sys
import io
import contextlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from sha512_basic_operation.ch import ch
from sha512_basic_operation.maj import maj
from sha512_constants.generate_k_constants import generate_k_constants
from sha512_sigma_functions.step3_SIGMA0.SIGMA0 import SIGMA0
from sha512_sigma_functions.step4_SIGMA1.SIGMA1 import SIGMA1

MASK = (1 << 64) - 1
LABELS = "abcdefgh"


def compress_block(initial_hash: list, schedule: list) -> list:
    """
    Step 8: Run all 80 rounds of the compression function over one
    1024-bit block's expanded (80-word) message schedule, returning the
    final working registers (a..h).
    """
    with contextlib.redirect_stdout(io.StringIO()):
        k_constants = generate_k_constants()

    a, b, c, d, e, f, g, h = initial_hash

    for t in range(80):
        big_sigma1_e = int(SIGMA1(e), 2)
        choice = int(ch(e, f, g), 2)
        t1 = (h + big_sigma1_e + choice + k_constants[t] + schedule[t]) & MASK

        big_sigma0_a = int(SIGMA0(a), 2)
        majority = int(maj(a, b, c), 2)
        t2 = (big_sigma0_a + majority) & MASK

        a, b, c, d, e, f, g, h = (
            (t1 + t2) & MASK, a, b, c,
            (d + t1) & MASK, e, f, g,
        )

    registers = [a, b, c, d, e, f, g, h]

    print("8. Final output of message block")
    for label, value in zip(LABELS, registers):
        print(f"    {label} = {format(value, '064b')}")
    return registers


if __name__ == "__main__":
    from sha512_constants.generate_h_constants import generate_h_constants

    with contextlib.redirect_stdout(io.StringIO()):
        h0 = generate_h_constants()

    example_schedule = [0] * 80
    example_schedule[0] = int("0110000101100010011000111000000", 2)

    compress_block(h0, example_schedule)
