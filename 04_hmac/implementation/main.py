from hmac_steps import step3_outer_hash


def hmac_sha256(key: bytes, message: bytes) -> str:
    """
    Runs the full HMAC-SHA256 pipeline (steps 1-3) and returns the hex digest.
    """
    digest = step3_outer_hash.outer_hash(key, message)
    return digest.hex()


def main():
    key = b"key"
    message = b"The quick brown fox jumps over the lazy dog"
    result = hmac_sha256(key, message)
    print(f"\nHMAC-SHA256(key={key!r}, message={message!r}) = {result}")


if __name__ == "__main__":
    main()
