# WHY these specific numbers: unlike the K/K' round constants, these are NOT
# derived from primes - they are the same "nothing up my sleeve" constants
# Ron Rivest introduced in MD4 (and reused in MD5), extended with one more
# for RIPEMD-160's fifth register. Each is just the sequence of hex digits
# 0123456789abcdef, written out in a simple counting pattern and then
# byte-reversed (since the algorithm stores words little-endian):
#   h0 = byte-reverse(0x01234567)                 -> 0x67452301
#   h1 = byte-reverse(0x89abcdef)                 -> 0xefcdab89
#   h2 = byte-reverse(0xfedcba98)  (counting down) -> 0x98badcfe
#   h3 = byte-reverse(0x76543210)  (counting down) -> 0x10325476
#   h4 = byte-reverse(0xf0e1d2c3)  (high nibble counts down while low
#        nibble counts up: f,0,e,1,d,2,c,3)        -> 0xc3d2e1f0
# The point is the same as the prime-based constants elsewhere: anyone can
# see exactly how these were built, so there's no room to hide a value
# secretly chosen to weaken the algorithm.
INITIAL_HASH_VALUES = [
    0x67452301,
    0xEFCDAB89,
    0x98BADCFE,
    0x10325476,
    0xC3D2E1F0,
]

LABELS = "01234"


def get_initial_hash_values() -> list:
    """
    RIPEMD-160 initial hash values (IV) - fixed literals shared with the
    MD4/MD5 family, not derived from primes.
    """
    print("Initial hash values (H0)")
    for label, value in zip(LABELS, INITIAL_HASH_VALUES):
        print(f"    h{label} = {format(value, '032b')}")
    return list(INITIAL_HASH_VALUES)


if __name__ == "__main__":
    get_initial_hash_values()
