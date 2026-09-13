from ripemd160_steps import step1_message_input as message_input
from ripemd160_steps import step2_padding as padding
from ripemd160_steps import step3_message_block as message_block
from ripemd160_steps import step4_message_schedule as message_schedule
from ripemd160_steps import step6_run_all_steps as run_all_steps
from ripemd160_steps import step7_combine as combine
from ripemd160_steps import step8_digest as digest

INITIAL_HASH_VALUES = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]


def ripemd160(message: str) -> str:
    """
    Runs the full RIPEMD-160 pipeline (steps 2-8) over a message and
    returns the final digest as a hex string.
    """
    bits = ''.join(format(ord(char), '08b') for char in message)

    padded_bits = padding.pad_message(bits)
    blocks = message_block.get_message_blocks(padded_bits)

    hash_values = list(INITIAL_HASH_VALUES)
    for block in blocks:
        words = [int(word, 2) for word in message_schedule.create_message_schedule(block)]
        left, right = run_all_steps.run_all_steps(hash_values, words)
        hash_values = combine.combine(hash_values, left, right)

    return digest.get_digest(hash_values)


def main():
    message, _, _ = message_input.get_message_input()
    result = ripemd160(message)
    print(f"\nRIPEMD-160(\"{message}\") = {result}")


if __name__ == "__main__":
    main()
