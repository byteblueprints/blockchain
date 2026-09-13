import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from base58_steps.step1_encode import encode
from base58_steps.step3_checksum import checksum


def encode_check(payload: bytes) -> str:
    """
    Step 4: Base58Check encoding = Base58(payload + checksum(payload)).

    The checksum makes a corrupted or mistyped Base58Check string
    detectable: a single changed character will, with overwhelming
    probability, no longer match its checksum, so the mistake is caught
    instead of silently producing a valid-looking but wrong address or key.
    """
    check = checksum(payload)
    encoded = encode(payload + check)

    print(f"4. Base58Check encode: {payload.hex()} -> {encoded}")
    return encoded


if __name__ == "__main__":
    encode_check(bytes.fromhex("00010966776006953D5567439E5E39F86A0D273BEE"))
