# SHR (Logical Right Shift) Operation

## What is SHR?
SHR (logical right shift) is a bitwise operation that shifts all bits of a binary number to the right by a specified number of positions. Zeros are shifted in from the left, and bits shifted off the right end are discarded.

For example, shifting the 8-bit value `10110011` right by 3 positions yields `00010110`.

## Usage in SHA-256
In the SHA-256 cryptographic hash algorithm, SHR is used in the computation of message schedule and compression functions. It is essential for mixing and diffusion in the hash process.

## Implementation in This Project
- The function `shr_n(x, n)` is implemented in [`02.SHA256/implementation/bitwise_ops/shr_n.py`](../implementation/bitwise_ops/shr_n.py).
    - It accepts an integer `x` and shifts it right by `n` bits, returning a 32-bit binary string.
    - Example usage:
      ```python
      from bitwise_ops.shr_n import shr_n
      shr_n(3454, 5)
      ```
- Demonstration calls are included in [`02.SHA256/implementation/main.py`](../implementation/main.py).

## Visualization
- The animation for the SHR operation is implemented in [`02.SHA256/manim_code/scenes/shr_n_anim.py`](../manim_code/scenes/shr_n_anim.py) as the `ShrNAnim` Manim scene.
- To render the animation, use:
  ```sh
  manim -pql main.py ShrNAnim
  ```
  from the `manim_code` directory.

## Further Reading
- [SHA-256 Wikipedia](https://en.wikipedia.org/wiki/SHA-2)
- [Bitwise shift (Wikipedia)](https://en.wikipedia.org/wiki/Bitwise_operation#Bit_shifts)
