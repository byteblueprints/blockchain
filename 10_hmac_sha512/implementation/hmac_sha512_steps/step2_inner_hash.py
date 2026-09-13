import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from hmac_sha512_steps.step1_key_preparation import prepare_key, sha512_bytes

IPAD = 0x36


def inner_hash(key: bytes, message: bytes) -> bytes:
    """
    Step 2: Compute H((K' XOR ipad) || message). Same construction as
    HMAC-SHA256 (see 04_hmac) - the choice of hash function underneath
    doesn't change HMAC's own logic at all, only the block/digest sizes.
    """
    prepared_key = prepare_key(key)
    padded = bytes(b ^ IPAD for b in prepared_key)
    digest = sha512_bytes(padded + message)

    print(f"2. Inner hash: {digest.hex()}")
    return digest


if __name__ == "__main__":
    inner_hash(b"key", b"The quick brown fox jumps over the lazy dog")
