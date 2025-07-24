# SHA-256 Bitwise Operations: Implementation

This directory contains Python implementations of core bitwise operations used in the SHA-256 cryptographic hash algorithm. Each operation is implemented in its own file for clarity and modularity.

## Files and Their Purpose

- `shr_n.py`   : Logical right shift (SHR) operation.
- `rotr_n.py`  : Bitwise rotate right (ROTR) operation.
- `xor_n.py`   : Bitwise exclusive OR (XOR) operation.
- `add_n.py`   : 32-bit integer addition (modulo 2^32).
- `main.py`    : Demonstrates usage of all the above operations.

## Usage

You can import and use any operation directly:

```python
from shr_n import shr_n
from rotr_n import rotr_n
from xor_n import xor_n
from add_n import add_n

shr_n(3454, 5)
rotr_n(3454, 5)
xor_n(3454, 1234)
add_n(3454, 1234)
```

Or run the demonstration script:

```sh
python main.py
```

## Further Reading
For detailed explanations and visualizations, see the corresponding resource markdown files in `../resources/`:
- `README_SHR_N.md`
- `README_ROTR_N.md`
- `README_XOR_N.md`
- `README_ADD_N.md`
