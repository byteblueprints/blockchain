# BIP32 fixed constants - standardized version bytes and the hardened-
# derivation offset, not derived from anything, just agreed-upon values
# every wallet must match exactly to produce interoperable "xprv"/"xpub"
# strings.
VERSION_PRIVATE = 0x0488ADE4  # mainnet extended private key ("xprv...")
VERSION_PUBLIC = 0x0488B21E   # mainnet extended public key ("xpub...")

# Child indices >= this value mean "hardened" derivation (written as 0'
# or 0H in a path like m/44'/0'/0'). Hardened derivation mixes in the
# PARENT PRIVATE key when computing a child, so it's impossible to derive
# a hardened child from just the parent's public key + chain code -
# unlike normal derivation, where anyone holding the public key and chain
# code can derive further public children without ever seeing a private key.
HARDENED_OFFSET = 0x80000000
