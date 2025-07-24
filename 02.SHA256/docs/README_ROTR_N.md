# ROTR (Rotate Right) Operation

## What is ROTR?
ROTR (rotate right) is a bitwise operation that shifts all bits of a binary number to the right by a specified number of positions. Unlike a logical shift, the bits that fall off the right end are wrapped around and reappear on the left end.

For example, rotating the 8-bit value `10110011` right by 3 positions yields `01110110`.

## Usage in SHA-256
In the SHA-256 cryptographic hash algorithm, ROTR is used extensively in the computation of message schedule and compression functions. It is a key part of the bit-mixing process that ensures diffusion and non-linearity in the hash output.

## Implementation in This Project
- The function `rotr_n(x, n)` is implemented in [`02.SHA256/implementation/rotr_n.py`](../implementation/rotr_n.py).
    - It accepts an integer `x` and rotates it right by `n` bits, returning a 32-bit binary string.
    - Example usage:
      ```python
      from rotr_n import rotr_n
      rotr_n(3454, 5)
      ```
- Demonstration calls are included in [`02.SHA256/implementation/main.py`](../implementation/main.py).

## Visualization
- The animation for the ROTR operation is implemented in [`02.SHA256/manim_code/rotr_n_anim.py`](../manim_code/rotr_n_anim.py) as the `Rotr32Anim` Manim scene.
- To render the animation, use:
  ```sh
  manim -pql main.py Rotr32Anim
  ```
  from the `manim_code` directory.

## Further Reading
- [SHA-256 Wikipedia](https://en.wikipedia.org/wiki/SHA-2)
- [Bitwise rotation (Wikipedia)](https://en.wikipedia.org/wiki/Bitwise_operation#Bitwise_rotation) 