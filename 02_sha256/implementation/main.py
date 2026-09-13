from sha256_steps import step1_message_input as message_input
from sha256_steps import step2_padding as padding
from sha256_steps import step3_message_block as message_block
from sha256_steps import step4_message_schedule as message_schedule
from sha256_steps import step5_expand_message_schedule as expand_message_schedule
from sha256_steps import step6_initial_hash_values as initial_hash_values
from sha256_steps import step8_final_block_output as final_block_output
from sha256_steps import step9_h1 as h1


def sha256(message: str) -> str:
    """
    Runs the full SHA-256 pipeline (steps 2-9) over a message and
    returns the final digest as a hex string.
    """
    bits = ''.join(format(ord(char), '08b') for char in message)

    padded_bits = padding.pad_message(bits)
    blocks = message_block.get_message_blocks(padded_bits)

    hash_values = initial_hash_values.get_initial_hash_values()
    for block in blocks:
        words = message_schedule.create_message_schedule(block)
        schedule = expand_message_schedule.expand_message_schedule(words)
        compressed = final_block_output.compress_block(hash_values, schedule)
        hash_values = h1.get_next_hash(hash_values, compressed)

    return ''.join(format(value, '08x') for value in hash_values)


def main():
    message, _, _ = message_input.get_message_input()
    digest = sha256(message)
    print(f"\nSHA-256(\"{message}\") = {digest}")


if __name__ == "__main__":
    main()
