import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from sha512_basic_operation.ch import ch
from sha512_basic_operation.maj import maj
from sha512_sigma_functions.step3_SIGMA0.SIGMA0 import SIGMA0
from sha512_sigma_functions.step4_SIGMA1.SIGMA1 import SIGMA1

MASK = (1 << 64) - 1


def compression_round(a, b, c, d, e, f, g, h, k, w):
    """
    Step 7: One round of the SHA-512 compression function, H(t) -> H(t+1).
    Structurally identical to SHA-256's round (see 02_sha256), just with
    64-bit words, 64-bit SIGMA0/SIGMA1, and this module's own K/W values.
    """
    big_sigma1_e = int(SIGMA1(e), 2)
    choice = int(ch(e, f, g), 2)
    t1 = (h + big_sigma1_e + choice + k + w) & MASK

    big_sigma0_a = int(SIGMA0(a), 2)
    majority = int(maj(a, b, c), 2)
    t2 = (big_sigma0_a + majority) & MASK

    new_a = (t1 + t2) & MASK
    new_e = (d + t1) & MASK

    print("7. H(t) -> H(t+1)")
    print(f"    T1 (temp) = {format(t1, '064b')}")
    print(f"    T2 (temp) = {format(t2, '064b')}")
    print(f"    a = {format(new_a, '064b')} <- T1 + T2")
    print(f"    e = {format(new_e, '064b')} <- d + T1")

    return new_a, a, b, c, new_e, e, f, g


if __name__ == "__main__":
    from sha512_constants.generate_h_constants import generate_h_constants
    from sha512_constants.generate_k_constants import generate_k_constants
    import io
    import contextlib

    with contextlib.redirect_stdout(io.StringIO()):
        h0 = generate_h_constants()
        k0 = generate_k_constants()[0]

    compression_round(*h0, k0, int("0110000101100010011000111000000", 2))
