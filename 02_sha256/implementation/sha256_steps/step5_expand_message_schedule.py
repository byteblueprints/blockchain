import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from sigma_functions.step1_sigma0.sigma0 import sigma0
from sigma_functions.step2_sigma1.sigma1 import sigma1

MASK = (1 << 32) - 1


def expand_message_schedule(words: list) -> list:
    """
    Step 5: Expand the 16 words (W0..W15) into the full 64-word message schedule.
    W[t] = (sigma1(W[t-2]) + W[t-7] + sigma0(W[t-15]) + W[t-16]) mod 2**32
    """
    schedule = [int(word, 2) for word in words]

    for t in range(16, 64):
        s1 = int(sigma1(schedule[t - 2]), 2)
        s0 = int(sigma0(schedule[t - 15]), 2)
        word = (s1 + schedule[t - 7] + s0 + schedule[t - 16]) & MASK
        schedule.append(word)

    print("5. Expand message schedule to 64 words")
    for t, word in enumerate(schedule):
        print(f"    W{t:<3}= {format(word, '032b')}")
    return schedule


if __name__ == "__main__":
    example_words = [format(0, '032b')] * 16
    example_words[0] = "01100001011000100110001110000000"
    example_words[15] = "00000000000000000000000000011000"
    expand_message_schedule(example_words)
