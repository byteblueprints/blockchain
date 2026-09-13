import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from hmac_steps.step1_key_preparation import prepare_key, sha256_bytes
from hmac_steps.step2_inner_hash import inner_hash

OPAD = 0x5C


def outer_hash(key: bytes, message: bytes) -> bytes:
    """
    Step 3: Compute H((K' XOR opad) || inner_hash) - the final HMAC value.
    ipad (0x36) and opad (0x5c) just need to be fixed, distinct bit
    patterns with roughly half their bits set - their specific values
    aren't a secret or a "nothing up my sleeve" derivation, they only
    need to differ from each other so the inner and outer hash calls
    aren't operating on the same effective key.
    """
    prepared_key = prepare_key(key)
    padded = bytes(b ^ OPAD for b in prepared_key)
    inner = inner_hash(key, message)
    digest = sha256_bytes(padded + inner)

    print(f"3. HMAC: {digest.hex()}")
    return digest


if __name__ == "__main__":
    outer_hash(b"key", b"The quick brown fox jumps over the lazy dog")
