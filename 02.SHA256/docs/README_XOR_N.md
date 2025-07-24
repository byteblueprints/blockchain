# XOR (Exclusive OR) Operation

## What is XOR?
XOR (exclusive OR) is a bitwise operation that outputs 1 for each bit position where the corresponding bits of its two operands are different, and 0 where they are the same.

For example, XOR of `1011` and `1101` is `0110`.

## Usage in SHA-256
In the SHA-256 cryptographic hash algorithm, XOR is used to combine intermediate values and message schedule words, contributing to the mixing and diffusion properties of the hash function.

## Implementation in This Project
- The function `xor_n(x, y)` is implemented in [`02.SHA256/implementation/xor_n.py`](../implementation/xor_n.py).
    - It accepts two integers `x` and `y`, performs bitwise XOR, and returns a 32-bit binary string.
    - Example usage:
      ```python
      from xor_n import xor_n
      xor_n(3454, 1234)
      ```
- Demonstration calls are included in [`02.SHA256/implementation/main.py`](../implementation/main.py).

## Visualization
- The animation for the XOR operation is implemented in [`02.SHA256/manim_code/xor_n_anim.py`](../manim_code/xor_n_anim.py) as the `XorNAnim` Manim scene.
- To render the animation, use:
  ```sh
  manim -pql main.py XorNAnim
  ```
  from the `manim_code` directory.

## Further Reading
- [SHA-256 Wikipedia](https://en.wikipedia.org/wiki/SHA-2)
- [XOR (Wikipedia)](https://en.wikipedia.org/wiki/Exclusive_or) 