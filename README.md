<h1 align="center">PRECISE</h1>
<h3 align="center">Precision Rules Enforced Calculations In Scientific Environments</h3>

<br>

<div align="center"><img src="https://camo.githubusercontent.com/7572a938f78b7dde0dbd741844b0b2bd7c031fdae63a420e0f80cbcd9911a154/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d434325323042592d2d4e432d2d5341253230342e302d6c69676874677265792e737667" alt="License"></div>

<br>
  <p align="center">
    Project GitHub Repo
    <br />
    <a href="https://github.com/steph1111/PRECISE"><strong>PRECISE »</strong></a>
    <br />
    <br />
    <a href="https://github.com/steph1111/PRECISE/issues">Report Issue</a>
    ·
    <a href="https://github.com/steph1111/PRECISE/projects?query=is%3Aopen">Project status</a>
    ·
    <a href="https://github.com/steph1111/PRECISE/discussions">Discuss</a>
  </p>
</div>

<br>

<!-- ABOUT THE PROJECT -->

---
## About The Project
FIXME

<br>

<!-- GETTING STARTED -->

---
## Getting Started

1. FIXME 

<br>

<!-- USAGE -->

---
## Available modules
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Modules table of contents</summary>
  <ol>
    <li><a href="#sig_float-">sig_float</a>
    <li><a href="#sig_constants-">sig_const</a>
  </ol>
</details>
<br>

<a href="#sig_float">sig_float » </a>

This module provides the infrastructure to preform calculations that behave according to significant figure rules. An instance of the sig_float class may be added, subtracted, multiplied, or divided with another sig_float using standard operators. The resultant will retain the proper number of significant figures. Units can optionally be provided.

<br>

<a href="#sig_const">sig_const »</a>

This module provides several commonly used constants of type `sig_float`.

<br>

# sig_float
## About The Module
This module provides the infrastructure to preform calculations that behave according to significant figure rules. An instance of the sig_float class may be added, subtracted, multiplied, or divided with another sig_float using standard operators. The resultant will retain the proper number of significant figures. Units can optionally be provided.

<br>

<!-- GETTING STARTED -->

---
## Getting Started

Import the sig_float class and round_sig function to your workspace 
```python
from sig_float import sig_float
from sig_float import round_sig
```
<br>

---
## Usage
<details>
  <summary>Usage table of contents</summary>
  <ol>
    <li><a href="#sig_float">sig_float()</a>
    <li><a href="#sig_figs">.sig_figs()</a></li>
    <li><a href="#precision">.precision()</a></li>
    <li><a href="#latex">.latex()</a></li>
    <li><a href="#exact">.exact()</a></li>
    <li><a href="#multiplication-">Multiplication (*)</a></li>
    <li><a href="#exponential--">Exponential (**)</a></li>
    <li><a href="#division-">Division (/)</a></li>
    <li><a href="#addition-">Addition (+)</a></li>
    <li><a href="#subtraction--">Subtraction (-)</a></li>
    <li><a href="#str">str()</a></li>
    <li><a href="#bool">bool()</a></li>
    <li><a href="#float">float()</a></li>
    <li><a href="#round_sig">round_sig()</a></li>
  </ol>
</details>
<br>

---
### sig_float()
*sig_float(str_num:str="0", units:dict=dict(), exact:bool=False) -> None:*

A sig_float object is designed to be used in situations in which the user wants to preform calculations which retain the proper significant figures and units. the recommended usage of a sig_float object is is to create variables of type sig_float then use those variables in a mathematical expressions.

**str_num**="0": A string argument containing a numeric value. Scientific notation may also be used with standard python scientific formatting.
```python
R = sig_float("0.08206")
C = sig_float("3.00e+8", {"m":1, "s":-1})
```

**units**=dict(): A dictionary of units in which the key is a string representation of the unit, and the value is the power to which it is raised. Negative exponents may be used.
```python
R = sig_float("0.08206", {"L":1, "atm":1, "mol":-1, "K":-1})
```

**exact**=False: A boolean describing if a number is exact. If exact is set to True, this sig_float will not affect the rounding of operations.
```python
R = sig_float("0.08206", {"L":1, "atm":1, "mol":-1, "K":-1}, exact=True)
```

Usage example
```python
V1 = sig_float("2.00", {"L":1})
P1 = sig_float("752.0", {"mmHg":1})
T1 = sig_float("293", {"K":1})
P2 = sig_float("2943", {"mmHg":1})
T2 = sig_float("273", {"K":1})
V2 = (T2 * P1 * V1) / (P2 * T1)
# V2 has value of sig_float("0.476", {"L", 1})
``` 
<br>

---
### .sig_figs()
*.sig_figs()->int:*

Returns the number of significant digits for a given sig_float object. Sig figs are calculated using the following sig fig rules:
* All non-zero digits are significant.
* All captive zeros are significant.
* Trailing zeros are only significant if they follow a decimal point
* Leading zeros are never significant.
```python
num = sig_float("0012000.")
num.sig_figs()
# Results in 5
```
<br>

---
### .precision() 
*.precision() -> int:*

Returns the number of places to which the number is precise to. A negative number is returned if the number is precise to a whole number.

What does the precision value mean? Given the number 1234.567, the following precisions are assigned to each digit.
|  |  |  |  |  |  |  |  |  |
| :---------------- | :--: | :--: |:--: |:--: |:--: |:--: |:--: |:--: |
| Number | 1 | 2 | 3 | 4 | . | 5 | 6 | 7 |
| Precision | -3 | -2 | -1 | 0 |   | 1 | 2 | 3 |
<br>

```python
a = sig_float("200")
a.precision()
# Results in -2
```
```python
b = sig_float("200.")
b.precision()
# Results in 0
```
```python
c = sig_float("0.0020")
c.precision()
# Results in 4
```
<br>

---
### .latex()
*.latex(format:int=1, sci:bool=False)->str:*

Formats sig_float to a $\LaTeX{}$ string. An argument may be provided to choose a unit format type. An additional argument may be used to change the number format to scientific. 

*The following sig_float is used in subsequent examples:*
```python 
R = sig_float("0.08206", {"L":1, "atm":1, "mol":-1, "K":-1}, exact=True)
```

<br>

**format**=1: (default): Units represented on one line using negative exponents
```python
print(R.latex(format=1))  # Or print(R.latex())
# Outputs: 0.08206 \; L \cdot atm \cdot mol^{-1} \cdot K^{-1}
```
$\large 0.08206 \; L \cdot atm \cdot mol^{-1} \cdot K^{-1}$

<br>

**format**=2: Units represented as a fraction
```python
print(R.latex(format=2))
# Outputs: 0.08206 \frac{L \cdot atm}{mol \cdot K}
```
$\large 0.08206 \frac{L \cdot atm}{mol \cdot K}$

<br>

**format**=3: Units represented on one line using a fraction
```python
print(R.latex(format=3))
# Outputs: 0.08206 \; L \cdot atm / mol \cdot K
```
$\large 0.08206 \; L \cdot atm / mol \cdot K$

<br> 
<h4 align="center">- - -</h1>
<br>

*The following sig_float is used in subsequent examples:*
```python 
C = sig_float("3.00e+8", {"m":1, "s":-1})
```

<br>

**sci**=False (default): Number represented in standard format
```python
print(C.latex(sci=False))
# Outputs: 30\bar{0}000000 \; m \cdot s^{-1}
```
$\large 30\bar{0}000000 \; m \cdot s^{-1}$

<br>

**sci**=True (default): Number represented in standard format
```python
print(C.latex(sci=True))
# Outputs: 3.00 \times 10^{8} \; m \cdot s^{-1}
```
$\large 3.00 \times 10^{8} \; m \cdot s^{-1}$

<br>

---
### .exact()
*.exact() -> bool*

Returns if a given sig_float is exact or not.
```python 
a = sig_float("1", exact=True)
b = sig_float("3", exact=True)
c = a / b
print(f"{a} / {b} = {c}. Exact? {c.exact()}")
# Outputs: 1 / 3 = 0.3333333333333333. Exact? True
```
<br>

---
### Multiplication (*)
*sig_float * sig_float*

Multiplies two operands of type sig_float using the standard multiplication operator (*). The resulting product is a number of type sig_float rounded to the proper number of sig figs according to the following sig fig rule:
* In multiplication and division, the result should be rounded to the least number of significant figures of any one term. 

If provided, units are also accounted for.
```python
a = sig_float("0.004")
b = sig_float("5280")
a * b
# Results in 20
```
<br>

---
### Exponential  (**)
*sig_float ** int/float*

Raises an operand of type sig_float to an integer or float power using the exponential operator (**). The resulting product is a number of type sig_float rounded to the proper number of sig figs according to the following sig fig rule:
* In multiplication and division, the result should be rounded to the least number of significant figures of any one term. 

If provided, units are also accounted for.
```python
v = sig_float("7.30", {"m":1, "s":-1})
print(v ** 2)
# Results in sig_float("53.3", {"m":2, "s":-2})
```
<br>

---
### Division (/)
*sig_float / sig_float*

Divides two operands of type sig_float using the standard division operator (/). The resulting quotient is a number of type sig_float rounded to the proper number of sig figs according to the following sig fig rule:
* In multiplication and division, the result should be rounded to the least number of significant figures of any one term. 

If provided, units are also accounted for.
```python
a = sig_float("2.8", {"kg":2, "m":5})
b = sig_float("2.2", {"kg":2, "m":1})
a / b
# Results in sig_float("1.3", {"m":4})
```
<br>

---
### Addition (+)
*sig_float + sig_float*

Adds two operands of type sig_float using the standard addition operator (+). The resulting sum is a number of type sig_float rounded to the proper precision according to the following rule:
* In addition and subtraction, the result is rounded off to the least number of decimal
places in any term, regardless of the significant figures of any one term.

If provided, units are also accounted for.
```python
a = sig_float("13.0198")
b = sig_float("1.2")
a + b
# Results in 14.2
```
<br>

---
### Subtraction (-)
*sig_float - sig_float*

Subtracts two operands of type sig_float using the standard subtraction operator (-). The resulting difference is a number of type sig_float rounded to the proper precision according to the following rule:
* In addition and subtraction, the result is rounded off to the least number of decimal
places in any term, regardless of the significant figures of any one term.

If provided, units are also accounted for.
```python
a = sig_float("300")
b = sig_float("47.465")
a - b
# Results in 300
```
<br>

---
### str()
Overloaded python str() function. Python's builtin str() function converts an object to type string. The sig_float function provides the same functionality. Also enables usage of python's print() function.
```python
num = sig_float("047.00990")
str(num)
# Results in "47.00990"
```
<br>

---
### bool()
Overloaded python bool() function. Python's builtin bool() function converts an object to type bool. Returns True unless the object is 0 in which the return value is False. The sig_float function provides the same functionality. 
```python
num = sig_float("0.889")
bool(num)
# Results in True
```
<br>

---
### float()
Overloaded python float() function. Python's builtin float() function converts an object to type float. The sig_float function provides the same functionality. Use this operation with caution, the internal float is **not** stored to proper significant figures.
```python
num = sig_float("47")
float(num)
# Results in 47.0
```
<br>

---
### round_sig()
*round_sig(number, sig_figs:int)->sig_float:*

Given a number and a number of significant figures, returns a sig_float object rounded the number given sig figs following standard sig fig rounding rules:
* If the first nonsignificant digit is less than 5, drop all nonsignificant digits.
* If the first nonsignificant digit is greater than or equal to 5, increase the last significant digit by 1 and drop all nonsignificant digits.

round_sig() works with sig_float objects 
```python
num = sig_float("47033.2")
round_sig(num, 4)
# Results in 47030
```
Or any object which can be converted to a float using float()
```python
round_sig(98982.8, 3)
# Results in 99000
```

<br>

# sig_const

## About The Module
This module provides several commonly used constants of type [sig_float](https://github.com/steph1111/PRECISE/tree/main/sig_float).

<br>

## Getting started

Import the sig_const class to your workspace 
```py
from precise import sig_const
```
<br>

## Available constants
|  Full name | Constant name | Implementation |
| :--------- | :------------ | :-------------- |
| Pi | `PI`  | `PI = sig_float("3.141592653589793238462643383279502884197", exact=True)`|
| Euler's number | `e` | `e = sig_float("2.71828182845904523536028747135266249", exact=True)`|
| Speed of light | `C` | `C = sig_float("299792458", {"m":1, "s":1}, exact=True)`|
| Planck's constant | `h` | `h = sig_float("6.62607015e-34", {"J":1, "s":1}, exact=True)`|
| Avogadro's number | `NA` | `NA = sig_float(" 6.02214076e+23", exact=True)`|
| Gas constant (atm) | `R_atm` | `R_atm = sig_float("0.08206", {"L":1, "atm":1}, {"K":1, "mol":1})`|
| Gas constant (mmHg) | `R_mmHg` | `R_mmHg = sig_float("62.36", {"L":1, "mmHg":1}, {"K":1, "mol":1})`|

<br>

## Usage
Any of the constants above can be used like any sig_float and may be instantiated as follows:
```python
sig_const.C
```


<br>

---
## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg