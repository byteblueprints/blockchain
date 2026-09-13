import os
import sys
import io
import contextlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from sha256_basic_operation.ch import ch
from sha256_basic_operation.maj import maj
from sha256_constants.generate_k_constants import generate_k_constants
from sigma_functions.step3_SIGMA0.SIGMA0 import SIGMA0
from sigma_functions.step4_SIGMA1.SIGMA1 import SIGMA1

MASK = (1 << 32) - 1
LABELS = "abcdefgh"


def compress_block(initial_hash: list, schedule: list) -> list:
    """
    Step 8: Run all 64 rounds of the compression function over one
    512-bit block's expanded message schedule, returning the final
    working registers (a..h) - the compressed output of this block,
    before it is added back to the initial hash values (see step 12).
    """
    with contextlib.redirect_stdout(io.StringIO()):
        k_constants = generate_k_constants()

    a, b, c, d, e, f, g, h = initial_hash

    for t in range(64):
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

    print("8. Final output of first message block")
    for label, value in zip(LABELS, registers):
        print(f"    {label} = {format(value, '032b')}")
    return registers


if __name__ == "__main__":
    from sha256_constants.generate_h_constants import generate_h_constants

    with contextlib.redirect_stdout(io.StringIO()):
        h0 = generate_h_constants()

    example_schedule = [0] * 64
    example_schedule[0] = int("01100001011000100110001110000000", 2)
    example_schedule[15] = int("00000000000000000000000000011000", 2)

    compress_block(h0, example_schedule)
