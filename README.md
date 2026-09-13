# ByteBlueprints: Blockchain Implementation from Scratch

Welcome to the ByteBlueprints project! This repository is dedicated to building a complete blockchain implementation from the ground up, with a strong focus on education, clarity, and modularity. Every component is explained, visualized, and coded step by step, making it an ideal resource for learners, educators, and contributors.

## Project Goals
- **Educational:** Demystify blockchain technology by breaking it into understandable, well-documented modules.
- **From Scratch:** No hidden libraries for the actual cryptography — every core algorithm is implemented and explained by hand. (The only exceptions are the OS's secure random source (`secrets`) for key/nonce generation, and Unicode normalization for BIP39 — both text/OS concerns, not cryptographic primitives.)
- **Verified:** Every module is checked against official test vectors and/or independent references (`hashlib`, the `cryptography` library) before being considered done.
- **Modular:** Each module is self-contained, numbered in build order, and reuses earlier modules rather than duplicating them.

## Repository Structure

Each module lives in `NN_name/implementation/`, runnable via `uv run python NN_name/implementation/main.py` from the repo root (one shared `uv` project covers all modules — see `pyproject.toml`).

| Module | What it is |
|---|---|
| `01_introduction/` | Project overview, learning path, and foundational concepts |
| `02_sha256/` | SHA-256 hash function, built from bitwise primitives up |
| `03_ripemd160/` | RIPEMD-160 hash function (dual-line, little-endian) |
| `04_hmac/` | HMAC (keyed hashing), using SHA-256 |
| `05_base58/` | Base58 / Base58Check encoding (Bitcoin's address encoding) |
| `06_ecc/` | Elliptic curve (secp256k1) key pair generation |
| `07_digital_signature/` | ECDSA sign/verify, using `02_sha256` + `06_ecc` |
| `08_wallet/` | Address + WIF generation from a private key (non-HD / "JBOK" wallet) |
| `09_sha512/` | SHA-512 hash function (64-bit word variant of SHA-256) |
| `10_hmac_sha512/` | HMAC using SHA-512 (needed for PBKDF2/BIP39) |
| `11_pbkdf2/` | PBKDF2 key derivation, using HMAC-SHA512 |
| `12_bip39/` | Mnemonic seed phrases (entropy → 2048-word wordlist → seed) |
| `13_bip32/` | Hierarchical Deterministic (HD) key derivation |
| `14_hd_wallet/` | Full standard flow: mnemonic → HD derivation → address/WIF, reusing `08_wallet` |

## Roadmap

- [x] SHA-256 (bitwise primitives → full hash function, verified against `hashlib`)
- [x] RIPEMD-160 (verified against `hashlib`)
- [x] HMAC / HMAC-SHA512 (verified against RFC 4231 vectors and Python's `hmac`)
- [x] Base58 / Base58Check (verified against Bitcoin wiki test vectors)
- [x] Elliptic curve key pairs, secp256k1 (verified against `cryptography`)
- [x] Digital signatures, ECDSA (verified against `cryptography`, both sign and verify directions)
- [x] Wallets: address + WIF generation (verified against an independently-computed reference chain)
- [x] SHA-512 (verified against `hashlib`)
- [x] PBKDF2 (verified against `hashlib`, including the real 2048-iteration BIP39 case)
- [x] BIP39 mnemonic seed phrases (verified against the official BIP39 test vectors)
- [x] BIP32 HD key derivation (verified against the official BIP32 test vectors 1 and 2)
- [x] Full HD wallet flow: mnemonic → address (verified end-to-end against an independent reference)
- [ ] Merkle tree construction and proofs
- [ ] Block structure and Proof-of-Work mining
- [ ] Transactions (data structure, UTXO vs. account model)
- [ ] Consensus edge cases (forks, longest/heaviest valid chain)
- [ ] Peer-to-peer networking basics
- [ ] Full blockchain node

### Next up: Merkle Tree, then Block + Proof-of-Work

With the full cryptographic toolkit now built (hashing, signatures, wallets, HD
derivation), the next milestone is the actual "chain" part of "blockchain":

1. **Merkle tree** — commits many transactions to a single root hash using
   `02_sha256`, no new primitives needed
2. **Block + Blockchain + PoW** — chain blocks by embedding each one's previous
   hash, and mine by searching for a nonce that meets a difficulty target
3. **Transactions** — structure first (sender/receiver/amount via the wallets
   already built), then UTXO vs. account model
4. **Consensus edge cases** — forks, longest/heaviest valid chain, orphan blocks
5. **(Optional, larger scope) P2P networking** — only needed for an actually
   distributed system, not a local simulation

## A note on correctness discipline

This project treats "looks right" and "is right" as different things. Constants,
tables, and test vectors are pulled from canonical sources (official specs,
audited reference implementations) rather than trusted from memory — several
real bugs were caught this way, including two cases where two modules used an
identically-named internal package (e.g. `constants`, `sigma_functions`) that
silently shadowed each other only when both modules were used together in the
same process. Every module is cross-checked against `hashlib`, official test
vectors, or the `cryptography` library before being called done.

## Contributing
Contributions, suggestions, and questions are welcome! Please open an issue or pull request.

## License
MIT (or your project license)

---
**Start your blockchain journey here—one bit at a time!**
