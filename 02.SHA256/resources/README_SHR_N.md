# SHR_N: Logical Right Shift Utility

This module provides a simple implementation of a logical right shift (bitwise shift right) operation in Python, returning a 32-bit binary string representation of the result. It is useful for understanding bitwise operations, especially in the context of cryptographic algorithms like SHA-256.

## Introduction

The `shr_n` function takes an integer input, shifts it right by a specified number of bits, and returns the result as a 32-bit binary string. It also prints the binary representation before and after the shift for educational purposes.

## Code Usage

### 1. Import and Use the Function

```
from shr_n import shr_n

result = shr_n(3454, 5)
print(result)  # Output: 32-bit binary string after shifting
```

### 2. Run the Example Script

You can also run the provided `main.py` script to see an example usage:

```
python main.py
```

This will output:
```
Before: 00000000000000000000110101111110
After : 00000000000000000000001011011111
```

## Requirements
- Python 3.13 or higher (as specified in `pyproject.toml`)

## File Structure
- `shr_n.py` : Contains the `shr_n` function implementation.
- `main.py`  : Example script demonstrating usage.

---
For more details, see the code and comments in `shr_n.py`.
