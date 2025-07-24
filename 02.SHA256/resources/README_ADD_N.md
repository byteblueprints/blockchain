# 32-bit Integer Addition (Binary)

## What is 32-bit Integer Addition?
32-bit integer addition is the process of adding two 32-bit binary numbers. In computer systems, this is typically performed modulo 2^32, meaning that any overflow beyond 32 bits is discarded (wrap-around behavior).

For example, adding `1011` and `1101` in binary yields `11000`, but in 4 bits, the result is `1000` (the leftmost bit is discarded).

## Usage in SHA-256
In the SHA-256 cryptographic hash algorithm, 32-bit integer addition is used to combine intermediate values, message schedule words, and constants. All additions are performed modulo 2^32 to ensure results fit within 32 bits.

## Implementation in This Project
- The function `add_n(x, y)` is implemented in [`02.SHA256/implementation/add_n.py`](../implementation/add_n.py).
    - It accepts two integers `x` and `y`, adds them modulo 2^32, and returns a 32-bit binary string.
    - Example usage:
      ```python
      from add_n import add_n
      add_n(3454, 1234)
      ```
- Demonstration calls are included in [`02.SHA256/implementation/main.py`](../implementation/main.py).

## Visualization
- The animation for 16-bit binary addition is implemented in [`02.SHA256/manim_code/add_n_anim.py`](../manim_code/add_n_anim.py) as the `AddNAnim` Manim scene.
- To render the animation, use:
  ```sh
  manim -pql main.py AddNAnim
  ```
  from the `manim_code` directory.

## Further Reading
- [SHA-256 Wikipedia](https://en.wikipedia.org/wiki/SHA-2)
- [Binary addition (Wikipedia)](https://en.wikipedia.org/wiki/Binary_number#Addition) 