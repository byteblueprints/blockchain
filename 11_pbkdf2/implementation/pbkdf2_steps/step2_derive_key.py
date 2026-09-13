import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from pbkdf2_steps.step1_f_function import f_function, DIGEST_SIZE


def derive_key(password: bytes, salt: bytes, iterations: int, key_length: int) -> bytes:
    """
    Step 2: PBKDF2 - derive a key of any requested length by computing as
    many F-function blocks as needed and concatenating them, then
    truncating to the exact length asked for.
        DK = F(1) || F(2) || ... || F(ceil(key_length / hash_size))
    BIP39 only ever asks for exactly one hash-size's worth of output (64
    bytes from SHA-512), so in practice only block 1 is ever computed
    here - but PBKDF2 itself is a general-purpose primitive, not
    BIP39-specific, so it needs to support arbitrary output lengths.
    """
    block_count = -(-key_length // DIGEST_SIZE)  # ceiling division
    blocks = [f_function(password, salt, iterations, i) for i in range(1, block_count + 1)]
    derived_key = b''.join(blocks)[:key_length]

    print(f"2. Derived key ({key_length} bytes): {derived_key.hex()}")
    return derived_key


if __name__ == "__main__":
    derive_key(b"password", b"salt", 1, 64)
