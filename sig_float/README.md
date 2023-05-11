<!-- PROJECT INTRO -->
<h1 align="center">sig_float module</h1>

  <p align="center">
    Project GitHub Repo
    <br />
    <a href="https://github.com/steph1111/PERCISE/tree/main/sig_float"><strong>sig_float »</strong></a>
    <br />
    <br />
    <a href="https://github.com/steph1111/PERCISE/issues">Report Issue</a>
    ·
    <a href="https://github.com/users/steph1111/projects/1">Project status</a>
    ·
    <a href="https://github.com/steph1111/PERCISE/discussions/18">Discuss</a>
  </p>
</div>

<br>

<!-- ABOUT THE PROJECT -->

---
## About The Module
This module provides the infastructure to preform calculations that behave according to signficant figure rules. An instance of the sig_float class maybe added, subtracted, multiplied, or divided with another sig_float using standard operators and the resultant will retain the proper number of signifiant figures. Units can optionally be provided.

<br>

<!-- GETTING STARTED -->

---
## Getting Started

1. Clone the repo
   ```sh
   git clone https://github.com/steph1111/PERCISE.git
   ```
2. Import the sig_float class and round_sig function to your workspace 
   ```python
    from sig_float import sig_float
    from sig_float import round_sig
   ```

<br>

<!-- USAGE -->

---
## Usage
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Usage table of contents</summary>
  <ol>
    <li><a href="#sig_float">sig_float()</a>
    <li><a href="#sig_figs">.sig_figs()</a></li>
    <li><a href="#multiplication-">Multiplication (*)</a></li>
    <li><a href="#division-">Division (/)</a></li>
    <li><a href="#addition-">Addition (+)</a></li>
    <li><a href="#subtraction--">Subtraction (-)</a></li>
    <li><a href="#str">str()</a></li>
    <li><a href="#bool">bool()</a></li>
    <li><a href="#float-">float()</a></li>
    <li><a href="#round_sig">round_sig()</a></li>
  </ol>
</details>
<br>

### sig_float()
*sig_float(self, str_num:str="0", units:dict=dict(), float_num:float=None)->None:*

sig_float objects have two in which ways they represent a number. A string holds the number with the correct number of significant figures. A float stores the numerical unrounded value for calculations. 

An instance of the sig_float class is created by providing the constructor with a string argument containing a numeric value. The units of the value may also be provided in a dictionary in which the key is a string representation of the unit, and the value is the power to which it is raised. Negative exponents may be used. One can also supply the initial internal float value, but this is **not recommended**.
```python
sig_float("0012.0001")
```
```python
sig_float("0.08206", {"L":1, "atm":1, "mol":-1, "K":-1})
```
The recommended usage of a sig_float object is is to create variables of type sig_float then use those variables in a mathmatical expression.
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

### latex()
*.latex(format:int=1)->str:*

Formats sig_float to a LaTeX string. The one may provide a format type, 1 or 2.
- format=1: Units formatted on one line 
- format=2: Units formatted in a fraction
```python 
R = sig_float("0.08206", {"L":1, "atm":1, "mol":-1, "K":-1})
```
format=1
```python
print(R.latex(format=1))
# Outputs: 
```
format=2
```python
print(R.latex(format=2))
# Outputs: 
```
<br/>

### str()
Overloaded python str() function. Python's builtin str() function converts an object to type string. The sig_float function provides the same functionality. Also enables usage of python's print() function.
```python
num = sig_float("047.00990")
string(num)
# Results in "47.00990"
```
<br>

### bool()
Overloaded python bool() function. Python's builtin bool() function converts an object to type bool. Returns True unless the object is 0 in which the return value is False. The sig_float function provides the same functionality. 
```python
num = sig_float("0.889")
bool(num)
# Results in True
```
<br>

### float()
Overloaded python float() function. Python's builtin float() function converts an object to type float. The sig_float function provides the same functionality. Use this operation with caution, the internal float is **not** stored to proper significant figures.
```python
num = sig_float("47")
float(num)
# Results in 47.0
```
<br>

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
