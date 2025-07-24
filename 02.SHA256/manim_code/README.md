# SHA-256 Bitwise Operations: Manim Visualizations

This directory contains Manim animation scenes that visually demonstrate the core bitwise operations used in SHA-256. Each operation has its own animation file for clarity and modularity.

## Animation Files

- `shr_n_anim.py`   : Logical right shift (SHR) animation (`ShrNAnim` scene).
- `rotr_n_anim.py`  : Bitwise rotate right (ROTR) animation (`Rotr32Anim` scene).
- `xor_n_anim.py`   : Bitwise exclusive OR (XOR) animation (`XorNAnim` scene).
- `add_n_anim.py`   : 16-bit binary addition animation (`AddNAnim` scene).
- `main.py`         : Entry point for rendering any of the above scenes.

## How to Render an Animation

From this directory, use the following command to render a scene (replace `SceneName` as needed):

```sh
manim -pql main.py ShrNAnim      # For SHR animation
manim -pql main.py Rotr32Anim    # For ROTR animation
manim -pql main.py XorNAnim      # For XOR animation
manim -pql main.py AddNAnim      # For Addition animation
```

## Further Reading
For detailed explanations and code for each operation, see the resource markdown files in `../resources/`:
- `README_SHR_N.md`
- `README_ROTR_N.md`
- `README_XOR_N.md`
- `README_ADD_N.md`
