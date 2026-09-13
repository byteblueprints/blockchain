import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from sha256_basic_operation.ch import ch
from sha256_basic_operation.maj import maj
from sigma_functions.step3_SIGMA0.SIGMA0 import SIGMA0
from sigma_functions.step4_SIGMA1.SIGMA1 import SIGMA1

MASK = (1 << 32) - 1


def compression_round(a, b, c, d, e, f, g, h, k, w):
    """
    Step 7: One round of the SHA-256 compression function, H(t) -> H(t+1).
    T1 = h + SIGMA1(e) + Ch(e,f,g) + K[t] + W[t]   (mod 2**32)
    T2 = SIGMA0(a) + Maj(a,b,c)                    (mod 2**32)
    Then shift everything down by one, with a = T1 + T2 and e = d + T1.
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
    print(f"    T1 (temp) = {format(t1, '032b')}")
    print(f"    T2 (temp) = {format(t2, '032b')}")
    print(f"    a = {format(new_a, '032b')} <- T1 + T2")
    print(f"    b = {format(a, '032b')}")
    print(f"    c = {format(b, '032b')}")
    print(f"    d = {format(c, '032b')}")
    print(f"    e = {format(new_e, '032b')} <- d + T1")
    print(f"    f = {format(e, '032b')}")
    print(f"    g = {format(f, '032b')}")
    print(f"    h = {format(g, '032b')}")

    return new_a, a, b, c, new_e, e, f, g


if __name__ == "__main__":
    compression_round(
        1779033703, 3144134277, 1013904242, 2773480762,
        1359893119, 2600822924, 528734635, 1541459225,
        1116352408, int("01100001011000100110001110000000", 2),
    )
