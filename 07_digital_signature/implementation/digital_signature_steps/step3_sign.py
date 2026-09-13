import os
import sys
import io
import contextlib

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_DIGITAL_SIGNATURE_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(_THIS_DIR, ".."))
_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(_THIS_DIR, "..", "..", "..", "06_ecc", "implementation"))

sys.path.append(_DIGITAL_SIGNATURE_IMPLEMENTATION_DIR)
sys.path.append(_ECC_IMPLEMENTATION_DIR)

from ecc_constants.curve_parameters import N, GX, GY
from ecc_basic_operation.mod_inverse import mod_inverse
from ecc_steps.step3_scalar_multiplication import scalar_multiply
from digital_signature_steps.step2_generate_nonce import generate_nonce


def sign(private_key: int, z: int):
    """
    Step 3: Sign a message hash z with a private key, producing (r, s).
        R = k * G                              (k = one-time secret nonce)
        r = R.x mod n
        s = k^-1 * (z + r * private_key) mod n
    Retries with a fresh nonce in the astronomically unlikely case that
    r or s comes out as 0 (which would make the signature unverifiable).
    """
    while True:
        with contextlib.redirect_stdout(io.StringIO()):
            k = generate_nonce()
            point_r = scalar_multiply(k, (GX, GY))

        r = point_r[0] % N
        if r == 0:
            continue

        with contextlib.redirect_stdout(io.StringIO()):
            k_inverse = mod_inverse(k, N)
        s = (k_inverse * (z + r * private_key)) % N
        if s == 0:
            continue

        break

    print(f"3. Signature:")
    print(f"    r = {hex(r)}")
    print(f"    s = {hex(s)}")
    return (r, s)


if __name__ == "__main__":
    sign(1, 0xba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad)
