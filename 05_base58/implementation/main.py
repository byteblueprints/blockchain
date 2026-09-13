from base58_steps import step1_encode, step2_decode, step4_encode_check, step5_decode_check


def main():
    payload = bytes.fromhex("00010966776006953D5567439E5E39F86A0D273BEE")

    plain = step1_encode.encode(payload)
    round_trip = step2_decode.decode(plain)
    print(f"\nPlain Base58 round-trip OK: {round_trip == payload}")

    checked = step4_encode_check.encode_check(payload)
    recovered = step5_decode_check.decode_check(checked)
    print(f"\nBase58Check round-trip OK: {recovered == payload}")
    print(f"Base58Check(payload) = {checked}")


if __name__ == "__main__":
    main()
