import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from sha512_sigma_functions.step1_sigma0.sigma0 import sigma0
from sha512_sigma_functions.step2_sigma1.sigma1 import sigma1

MASK = (1 << 64) - 1


def expand_message_schedule(words: list) -> list:
    """
    Step 5: Expand the 16 words (W0..W15) into the full 80-word message schedule.
    W[t] = (sigma1(W[t-2]) + W[t-7] + sigma0(W[t-15]) + W[t-16]) mod 2**64
    """
    schedule = [int(word, 2) for word in words]

    for t in range(16, 80):
        s1 = int(sigma1(schedule[t - 2]), 2)
        s0 = int(sigma0(schedule[t - 15]), 2)
        word = (s1 + schedule[t - 7] + s0 + schedule[t - 16]) & MASK
        schedule.append(word)

    print("5. Expand message schedule to 80 words")
    for t, word in enumerate(schedule):
        print(f"    W{t:<3}= {format(word, '064b')}")
    return schedule


if __name__ == "__main__":
    example_words = [format(0, '064b')] * 16
    example_words[0] = format(int("0110000101100010011000111000000", 2), '064b')
    expand_message_schedule(example_words)
