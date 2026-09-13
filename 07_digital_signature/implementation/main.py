import os
import sys

_ECC_IMPLEMENTATION_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "06_ecc", "implementation"))
sys.path.append(_ECC_IMPLEMENTATION_DIR)

from ecc_steps import step4_generate_private_key, step5_generate_public_key, step6_key_encoding
from digital_signature_steps import step1_hash_message as hash_message
from digital_signature_steps import step3_sign as sign_module
from digital_signature_steps import step4_verify as verify_module


def generate_key_pair():
    """
    Generates an ECC key pair using the 06_ecc module's own building
    blocks directly, rather than importing its main.py (every module's
    entry point is generically named "main.py", so importing it by name
    across modules would collide with this file's own module name).
    """
    private_key = step4_generate_private_key.generate_private_key()
    public_key = step5_generate_public_key.generate_public_key(private_key)

    return {
        "private_key": private_key,
        "public_key": public_key,
        "private_key_hex": step6_key_encoding.encode_private_key(private_key),
        "public_key_compressed": step6_key_encoding.encode_public_key_compressed(public_key),
    }


def main():
    print("Generating a key pair (reusing the ECC module):")
    keys = generate_key_pair()
    private_key = keys["private_key"]
    public_key = keys["public_key"]
    print(f"  private key: {keys['private_key_hex']}")
    print(f"  public key:  {keys['public_key_compressed']}")

    message = "Hello, blockchain!"
    print(f"\nSigning message: {message!r}")
    z = hash_message.hash_message(message)
    signature = sign_module.sign(private_key, z)

    print("\nVerifying with the correct public key and message:")
    assert verify_module.verify(public_key, z, signature) is True

    print("\nTamper test - altering the message after signing:")
    tampered_z = hash_message.hash_message(message + "!")
    assert verify_module.verify(public_key, tampered_z, signature) is False

    print("\nTamper test - altering the signature:")
    tampered_signature = (signature[0], (signature[1] + 1) % (1 << 256))
    assert verify_module.verify(public_key, z, tampered_signature) is False

    print("\nTamper test - verifying with the wrong public key:")
    other_keys = generate_key_pair()
    assert verify_module.verify(other_keys["public_key"], z, signature) is False

    print("\nAll checks passed: signature verifies correctly and fails on any tampering.")


if __name__ == "__main__":
    main()
