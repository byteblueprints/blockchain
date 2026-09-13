# WHY this specific 58-character alphabet: it's the 62 alphanumeric
# characters (0-9, A-Z, a-z) with four removed - '0' (zero), 'O' (capital
# o), 'I' (capital i), and 'l' (lowercase L) - because those pairs are easy
# to confuse with each other in many fonts, and this encoding exists
# specifically for values a human might read, hand-copy, or compare
# (private keys, addresses). Unlike the hash function constants, there's
# no "nothing up my sleeve" derivation here - it's a practical, readability
# -driven choice, standardized by Bitcoin and now used across the industry.
ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

BASE = len(ALPHABET)

assert BASE == 58
