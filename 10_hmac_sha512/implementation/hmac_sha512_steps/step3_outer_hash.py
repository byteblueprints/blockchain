import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from hmac_sha512_steps.step1_key_preparation import prepare_key, sha512_bytes
from hmac_sha512_steps.step2_inner_hash import inner_hash

OPAD = 0x5C


def outer_hash(key: bytes, message: bytes) -> bytes:
    """
    Step 3: Compute H((K' XOR opad) || inner_hash) - the final HMAC-SHA512 value.
    """
    prepared_key = prepare_key(key)
    padded = bytes(b ^ OPAD for b in prepared_key)
    inner = inner_hash(key, message)
    digest = sha512_bytes(padded + inner)

    print(f"3. HMAC-SHA512: {digest.hex()}")
    return digest


if __name__ == "__main__":
    outer_hash(b"key", b"The quick brown fox jumps over the lazy dog")
