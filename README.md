<div align="center">

# NumberForge

**A beginner-friendly Python CLI that finds the largest number in a comma-separated list.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-CLI-222222)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen)

[Source Code](largest_number.py) · [Issues](https://github.com/ansh44233/NumberForge/issues)

</div>

---

## Overview

NumberForge reads a comma-separated sequence of integers, compares the values, and prints the largest one. It is a compact example of core Python programming and a simple linear-time algorithm.

## What It Demonstrates

- Reading input from the command line
- Converting strings into integers
- Working with Python lists
- Iteration, comparisons, and conditional statements
- Tracking a running maximum

## How It Works

1. Enter integers separated by commas.
2. The program converts the input into a list of integers.
3. It initializes the current maximum using the first element.
4. It checks each value and updates the maximum when a larger value is found.
5. It prints the result.

## Run Locally

**Requirements:** Python 3. No third-party packages are required.

```bash
git clone https://github.com/ansh44233/NumberForge.git
cd NumberForge
python largest_number.py
```

Use `python3` instead of `python` on systems where that is the Python 3 command.

## Example

```text
Input:
12,45,7,89,23

Output:
89
```

## Complexity

For `n` input numbers:

| Measure | Complexity |
|---|---:|
| Time | O(n) |
| Auxiliary space | O(1), excluding the input list |

The program performs one traversal of the list to find the maximum.

## Project Structure

```text
NumberForge/
├── largest_number.py
├── README.md
└── .gitignore
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ansh44233/NumberForge&type=Date)](https://star-history.com/#ansh44233/NumberForge&Date)

---

<div align="center">

**Built with Python · Made for learning**

If you find this project useful, consider giving it a ⭐.

</div>
