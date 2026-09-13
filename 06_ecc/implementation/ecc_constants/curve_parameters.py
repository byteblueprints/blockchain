# secp256k1 - the elliptic curve used by Bitcoin and Ethereum for key pairs
# and signatures. Curve equation: y^2 = x^3 + a*x + b (mod p).
#
# WHY these specific numbers: unlike the hash function constants, these are
# NOT "nothing up my sleeve" derived values - they're a standardized,
# publicly agreed-upon curve chosen (originally by Certicom, in SEC 2) for
# its efficient arithmetic (a=0 makes point doubling cheaper) and because it
# has no known structural weakness after decades of public scrutiny. Every
# wallet and node in Bitcoin/Ethereum must use the exact same curve, so
# these values are fixed by convention, not computed.
# Verified against the widely-used python-ecdsa library's own constants.

P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F  # field prime
A = 0x0000000000000000000000000000000000000000000000000000000000000000  # curve coefficient a
B = 0x0000000000000000000000000000000000000000000000000000000000000007  # curve coefficient b

GX = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798  # generator point x
GY = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8  # generator point y

N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141  # order of G
H = 1  # cofactor

# Sanity check the field prime matches its well-known closed form.
assert P == 2**256 - 2**32 - 977
