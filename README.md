<div align="center">

# ⚡ NumberForge

### Find the maximum. Understand the logic. Keep it simple.

A lightweight command-line Python project that finds the largest value in a comma-separated list of integers.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Not%20specified-lightgrey?style=for-the-badge)](https://github.com/ansh44233/NumberForge)
[![Dependencies](https://img.shields.io/badge/Dependencies-None-2ea44f?style=for-the-badge)](https://github.com/ansh44233/NumberForge)

[**View Source**](largest_number.py) · [Report an Issue](https://github.com/ansh44233/NumberForge/issues) · [Star History](https://star-history.com/#ansh44233/NumberForge&Date)

</div>

---

## 📌 About

**NumberForge** is a small Python CLI program built around one fundamental programming task: finding the largest number in a collection.

Provide a comma-separated list of integers, and the program compares the values to determine and print the maximum.

The project keeps the implementation intentionally simple, making it useful for understanding loops, conditions, lists, type conversion, and basic algorithmic thinking.

## ✨ What it demonstrates

- **Command-line input** — accepting values from the terminal.
- **Type conversion** — converting input strings into integers.
- **Python lists** — storing and iterating over a collection of values.
- **Conditional logic** — comparing values with an `if` statement.
- **Maximum tracking** — maintaining the largest value found so far.
- **Algorithmic fundamentals** — solving a simple problem with a linear scan.

## 🚀 Quick start

### 1. Clone the repository

```bash
git clone https://github.com/ansh44233/NumberForge.git
cd NumberForge
```

### 2. Run the program

```bash
python largest_number.py
```

> **Requirement:** Python 3. No third-party packages are needed.

If your system uses `python3` as the Python command, run `python3 largest_number.py` instead.

## 💻 Example

Enter a comma-separated list of integers when prompted:

```text
12, 45, 7, 89, 23

89
```

The program checks the values and prints the largest one.

## 🧠 How the logic works

1. Read the comma-separated input.
2. Split the input into individual values and convert them to integers.
3. Treat the first value as the current largest value.
4. Visit each value and compare it with the current maximum.
5. Update the maximum whenever a larger value is found.
6. Print the final result.

## ⏱️ Complexity

For an input containing **n** integers:

| Metric | Complexity | Explanation |
|---|---:|---|
| Time | **O(n)** | Each value is checked once. |
| Extra working space | **O(1)** | Only a fixed number of tracking variables are used, excluding the input list. |

## 🗂️ Repository structure

```text
NumberForge/
├── largest_number.py   # Main Python program
├── README.md           # Project documentation
└── .gitignore          # Files excluded from Git
```

## 🛣️ Possible next steps

Potential improvements for a future version:

- Handle empty input and invalid values gracefully.
- Support decimal numbers.
- Add automated tests for different input cases.
- Add clearer prompts and error messages.
- Package the logic into a reusable function.

These are ideas for future development; they are not features of the current script.

## 🌟 Star history

[![Star History Chart](https://api.star-history.com/svg?repos=ansh44233/NumberForge&type=Date)](https://star-history.com/#ansh44233/NumberForge&Date)

---

<div align="center">

**A small project built to practise the fundamentals of Python.**

If this repository helped you, consider leaving a ⭐.

</div>
