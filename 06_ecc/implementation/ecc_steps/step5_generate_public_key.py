import os
import sys
import io
import contextlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from ecc_steps.step3_scalar_multiplication import scalar_multiply


def generate_public_key(private_key: int):
    """
    Step 5: Derive the public key from the private key.
    public_key = private_key * G
    This is a one-way operation: computing public_key from private_key is
    fast (scalar_multiply), but recovering private_key from public_key
    would require solving the elliptic curve discrete logarithm problem,
    which is believed to be computationally infeasible for secp256k1's
    256-bit group. That asymmetry is the entire basis of the security here.
    """
    from ecc_constants.curve_parameters import GX, GY

    with contextlib.redirect_stdout(io.StringIO()):
        public_key = scalar_multiply(private_key, (GX, GY))

    print(f"5. Public key: ({hex(public_key[0])}, {hex(public_key[1])})")
    return public_key


if __name__ == "__main__":
    generate_public_key(2)
