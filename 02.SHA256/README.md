# SHA-256 Bitwise Operations & Visualizations

This module provides clear Python implementations and Manim visualizations of the core bitwise operations used in the SHA-256 cryptographic hash algorithm. It is designed for both educational and practical purposes, making it easy to understand, demonstrate, and extend these fundamental operations.

## Directory Structure

```
02.SHA256/
  implementation/
    bitwise_ops/      # All bitwise operation implementations (SHR, ROTR, XOR, ADD)
    main.py           # Demonstration script for all operations
    README.md         # Details on usage and structure
  manim_code/
    scenes/           # All Manim animation scenes for visualizing operations
    main.py           # Entry point for rendering scenes
    README.md         # Animation usage and details
  docs/               # Resource markdowns for each operation
    README_SHR_N.md
    README_ROTR_N.md
    README_XOR_N.md
    README_ADD_N.md
  README.md           # (this file)
```

## Quick Start

### 1. Bitwise Operations (Python)
- See [`implementation/README.md`](implementation/README.md) for details.
- Example usage:
  ```python
  from bitwise_ops.shr_n import shr_n
  from bitwise_ops.rotr_n import rotr_n
  from bitwise_ops.xor_n import xor_n
  from bitwise_ops.add_n import add_n

  shr_n(3454, 5)
  rotr_n(3454, 5)
  xor_n(3454, 1234)
  add_n(3454, 1234)
  ```
- Or run all demonstrations:
  ```sh
  python implementation/main.py
  ```

### 2. Visualizations (Manim)
- See [`manim_code/README.md`](manim_code/README.md) for details.
- Render any operation's animation from the `manim_code` directory:
  ```sh
  manim -pql main.py ShrNAnim      # SHR
  manim -pql main.py Rotr32Anim    # ROTR
  manim -pql main.py XorNAnim      # XOR
  manim -pql main.py AddNAnim      # ADD
  ```

### 3. Documentation
- In-depth explanations for each operation are in the [`docs/`](docs/) folder.

## Requirements
- Python 3.13+
- [Manim](https://www.manim.community/) for animations

## License
MIT (or your project license)

---
For questions, improvements, or contributions, please see the subfolder READMEs or open an issue! 