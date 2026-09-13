from ecc_steps import step4_generate_private_key as generate_private_key
from ecc_steps import step5_generate_public_key as generate_public_key
from ecc_steps import step6_key_encoding as key_encoding


def generate_key_pair():
    """
    Runs the full ECC key pair pipeline (steps 4-6): random private key ->
    derived public key -> encoded forms of both.
    """
    private_key = generate_private_key.generate_private_key()
    public_key = generate_public_key.generate_public_key(private_key)

    return {
        "private_key": private_key,
        "public_key": public_key,
        "private_key_hex": key_encoding.encode_private_key(private_key),
        "public_key_uncompressed": key_encoding.encode_public_key_uncompressed(public_key),
        "public_key_compressed": key_encoding.encode_public_key_compressed(public_key),
    }


def main():
    keys = generate_key_pair()
    print()
    print(f"Private key:              {keys['private_key_hex']}")
    print(f"Public key (uncompressed): {keys['public_key_uncompressed']}")
    print(f"Public key (compressed):   {keys['public_key_compressed']}")


if __name__ == "__main__":
    main()
