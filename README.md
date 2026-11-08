<p align="center">
  <img src="assets/banner.svg" alt="Python Study Laboratory - Algorithms, OOP & Tkinter" width="100%" />
</p>

<p align="center">
  <strong>Comprehensive Computer Science Laboratory Curriculum: Core Algorithms, Object-Oriented Design, Cryptography, and Tkinter GUI Applications</strong>
</p>

<p align="center">
  <a href="https://github.com/AbinVarghexe/Python-Study/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="License" /></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.8%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+" /></a>
  <a href="https://docs.python.org/3/library/tkinter.html"><img src="https://img.shields.io/badge/GUI-Tkinter-FFD43B.svg?style=for-the-badge&logo=python&logoColor=black" alt="Tkinter" /></a>
  <a href="https://en.wikipedia.org/wiki/Object-oriented_programming"><img src="https://img.shields.io/badge/Paradigms-OOP%20%7C%20Functional-00A4EF.svg?style=for-the-badge" alt="Paradigms" /></a>
</p>

---

## Overview

**Python-Study** is a structured repository containing hands-on implementations of essential computer science curriculum algorithms, object-oriented software design patterns, and interactive desktop graphical applications built with Python's standard `tkinter` library.

The codebase is organized into clean, self-contained educational modules ranging from foundational mathematical proofs to complete desktop utility interfaces.

```
Python-Study/Tutorial/
├── Core Algorithms (Math & Number Theory)
├── Cryptography & String Manipulation
├── Financial & Tax Computation Engines
├── Object-Oriented Architecture (Classes & Overloading)
└── Interactive Tkinter Desktop GUIs
```

---

## Curriculum Index & Modules

### 1. Mathematical Algorithms & Number Theory

| Script | Concept & Implementation |
| :--- | :--- |
| [`armstrong.py`](Tutorial/armstrong.py) | Digit separation and power sum calculation to identify Narcissistic/Armstrong numbers. |
| [`binary_to_decimal.py`](Tutorial/binary_to_decimal.py) | Positional bit-weight conversion from binary bitstrings to base-10 integers. |
| [`fact.py`](Tutorial/fact.py) | Iterative and recursive implementations of factorial computation ($n!$). |
| [`fibonacci.py`](Tutorial/fibonacci.py) | Dynamic state progression generating the Fibonacci sequence. |
| [`primenumber.py`](Tutorial/primenumber.py) | Primality testing algorithm with square-root factor boundary optimization ($\mathcal{O}(\sqrt{n})$). |
| [`square_root.py`](Tutorial/square_root.py) | Babylonian / Newton-Raphson method for approximating square roots to precision $\epsilon$. |

### 2. Cryptography & String Operations

| Script | Concept & Implementation |
| :--- | :--- |
| [`caesar_cipher.py`](Tutorial/caesar_cipher.py) | Shift cipher encryption and decryption handling uppercase, lowercase, and cyclic modulo wrapping. |
| [`palindromsysm.py`](Tutorial/palindromsysm.py) | Palindromic symmetry detection with two-pointer and slice-inversion checks. |
| [`string_operations.py`](Tutorial/string_operations.py) | Substring indexing, frequency counting, character classification, and formatting utilities. |
| [`string_reversal.py`](Tutorial/string_reversal.py) | Memory-efficient in-place and slice-based string inversion algorithms. |

### 3. Financial & Economic Computation

| Script | Concept & Implementation |
| :--- | :--- |
| [`incometax.py`](Tutorial/incometax.py) | Progressive marginal tax bracket evaluation with deduction allowances. |
| [`investment.py`](Tutorial/investment.py) | Compound interest formula calculation ($A = P(1 + r/n)^{nt}$) with year-by-year amortization. |

### 4. Object-Oriented Programming (OOP)

| Script | Concept & Implementation |
| :--- | :--- |
| [`rational_class.py`](Tutorial/rational_class.py) | Custom `Rational` class implementing exact rational arithmetic (`+`, `-`, `*`, `/`), Euclidean GCD simplification, and rich comparison operators (`__eq__`, `__lt__`). |
| [`student_class.py`](Tutorial/student_class.py) | `Student` entity encapsulation managing roll numbers, multi-subject marks, GPA computation, and academic grade sheet generation. |

### 5. Interactive Tkinter Graphical User Interfaces

| Script | Desktop Application Window |
| :--- | :--- |
| [`gui_arithmetic_operations.py`](Tutorial/gui_arithmetic_operations.py) | Dual-operand graphical calculator with add, subtract, multiply, and divide buttons. |
| [`gui_bill_generator.py`](Tutorial/gui_bill_generator.py) | Retail item entry form with automated subtotal, sales tax, and printable invoice summary. |
| [`gui_label_clear_restore.py`](Tutorial/gui_label_clear_restore.py) | Dynamic state manipulation showcasing Tkinter label buffer switching and widget redrawing. |
| [`gui_login_form.py`](Tutorial/gui_login_form.py) | Secure password-masked entry field with credential validation and feedback modals. |
| [`gui_password_strength.py`](Tutorial/gui_password_strength.py) | Real-time keystroke evaluation scoring length, entropy, digits, and special characters. |
| [`gui_temperature_converter.py`](Tutorial/gui_temperature_converter.py) | Bidirectional Celsius $\leftrightarrow$ Fahrenheit $\leftrightarrow$ Kelvin temperature conversion utility. |

---

## Running the Programs

### Prerequisites

All programs run on standard Python without requiring external third-party packages:
- Python 3.8 or later
- Tkinter (included with standard Python installers on Windows and macOS; on Ubuntu/Debian: `sudo apt install python3-tk`)

### Execution

```bash
# Clone the repository
git clone https://github.com/AbinVarghexe/Python-Study.git
cd Python-Study/Tutorial

# Run any console algorithm
python rational_class.py

# Launch any interactive Tkinter application
python gui_password_strength.py
```

## License

This educational repository is open-sourced under the MIT License - see the [LICENSE](LICENSE) file for details.
