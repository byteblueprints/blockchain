import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from hmac_steps.step1_key_preparation import prepare_key, sha256_bytes

IPAD = 0x36


def inner_hash(key: bytes, message: bytes) -> bytes:
    """
    Step 2: Compute H((K' XOR ipad) || message).

    WHY xor the key into the hash input instead of just hashing
    key||message directly: SHA-256 (like MD5 and most Merkle-Damgard
    hashes) is vulnerable to length-extension - given H(secret||message)
    and the length of secret, an attacker can compute H(secret||message||
    extra) for a chosen extra WITHOUT knowing secret. Wrapping the key
    through two separate hash calls, mixed with different fixed patterns
    (ipad/opad) on each side, is what defeats that attack. This is HMAC's
    entire reason to exist instead of naive keyed hashing.
    """
    prepared_key = prepare_key(key)
    padded = bytes(b ^ IPAD for b in prepared_key)
    digest = sha256_bytes(padded + message)

    print(f"2. Inner hash: {digest.hex()}")
    return digest


if __name__ == "__main__":
    inner_hash(b"key", b"The quick brown fox jumps over the lazy dog")
