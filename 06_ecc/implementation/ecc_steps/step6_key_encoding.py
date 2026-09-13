def encode_private_key(private_key: int) -> str:
    """32-byte big-endian hex encoding of the private key."""
    return private_key.to_bytes(32, byteorder='big').hex()


def encode_public_key_uncompressed(point) -> str:
    """
    0x04 prefix followed by the full x and y coordinates (65 bytes total).
    """
    x, y = point
    encoded = b'\x04' + x.to_bytes(32, byteorder='big') + y.to_bytes(32, byteorder='big')
    return encoded.hex()


def encode_public_key_compressed(point) -> str:
    """
    Step 6: Compressed form (33 bytes) - only x is stored, plus a 1-byte
    prefix (0x02 if y is even, 0x03 if y is odd) recording which of the two
    possible y-values (y and p - y, the curve's two roots for a given x)
    was the real one. The other side can recompute y from x using the
    curve equation itself, so storing y in full would be redundant.
    """
    x, y = point
    prefix = b'\x02' if y % 2 == 0 else b'\x03'
    encoded = prefix + x.to_bytes(32, byteorder='big')
    return encoded.hex()


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))
    from ecc_constants.curve_parameters import GX, GY

    print(f"6. Private key (hex):            {encode_private_key(1)}")
    print(f"   Public key (uncompressed):    {encode_public_key_uncompressed((GX, GY))}")
    print(f"   Public key (compressed):      {encode_public_key_compressed((GX, GY))}")
