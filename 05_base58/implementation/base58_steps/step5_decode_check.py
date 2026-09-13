import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from base58_steps.step2_decode import decode
from base58_steps.step3_checksum import checksum, CHECKSUM_LENGTH


def decode_check(text: str) -> bytes:
    """
    Step 5: Base58Check decoding - the inverse of encode_check.
    Splits the decoded bytes into payload and checksum, recomputes the
    checksum over the payload, and raises if it doesn't match (corrupted
    or invalid input) rather than silently returning bad data.
    """
    raw = decode(text)
    if len(raw) < CHECKSUM_LENGTH:
        raise ValueError("Base58Check input too short to contain a checksum")

    payload, check = raw[:-CHECKSUM_LENGTH], raw[-CHECKSUM_LENGTH:]
    expected_check = checksum(payload)

    if check != expected_check:
        raise ValueError(f"Base58Check checksum mismatch: got {check.hex()}, expected {expected_check.hex()}")

    print(f"5. Base58Check decode: {text} -> {payload.hex()}")
    return payload


if __name__ == "__main__":
    decode_check("16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM")
