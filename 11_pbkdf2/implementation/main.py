from pbkdf2_steps import step2_derive_key


def pbkdf2_hmac_sha512(password: bytes, salt: bytes, iterations: int, key_length: int) -> bytes:
    """
    PBKDF2 with HMAC-SHA512 as the underlying pseudorandom function - the
    exact configuration BIP39 uses to turn a mnemonic phrase into a seed.
    """
    return step2_derive_key.derive_key(password, salt, iterations, key_length)


def main():
    password = b"password"
    salt = b"salt"
    iterations = 1000  # BIP39 itself uses 2048 - kept lower here so the demo stays fast
    key_length = 64

    derived = pbkdf2_hmac_sha512(password, salt, iterations, key_length)
    print(f"\nPBKDF2-HMAC-SHA512(password={password!r}, salt={salt!r}, iterations={iterations}) = {derived.hex()}")


if __name__ == "__main__":
    main()
