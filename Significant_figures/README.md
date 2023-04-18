<!-- PROJECT INTRO -->
<h1 align="center">sig_float module</h1>

  <p align="center">
    Project GitHub Repo
    <br />
    <a href="https://github.com/steph1111/Computational-chem/tree/main/Significant_figures"><strong>sig_float »</strong></a>
    <br />
    <br />
    <a href="https://github.com/steph1111/Computational-chem/issues">Report Issue</a>
    ·
    <a href="https://github.com/users/steph1111/projects/1">Project status</a>
    ·
    <a href="https://github.com/steph1111/Computational-chem/discussions">Discuss</a>
  </p>
</div>

<br>

<!-- ABOUT THE PROJECT -->
## About The Project
---
This module provides the infastructure to preform calculations that behave according to signficant figure rules. An instance of the sig_float class maybe added, subtracted, multiplied, or divided with another sig_float using standard operators and the resultant will retain the proper number of signifiant figures. 

<br>

<!-- GETTING STARTED -->
## Getting Started
---

1. Clone the repo
   ```sh
   git clone https://github.com/steph1111/Computational-chem.git
   ```
2. Install the module to your workspace 
   ```python
   from sig_float import sig_float
   ```

<br>

<!-- USAGE -->
## Usage
___
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Usage table of contents</summary>
  <ol>
    <li><a href="#sig_float">sig_float()</a>
    <li><a href="#sig_figs">.sig_figs()</a></li>
    <li><a href="multiplication-">Multiplication (*)</a></li>
    <li><a href="#division-">Division (/)</a></li>
    <li><a href="#addition-">Addition (+)</a><li>
  </ol>
</details>
<br>

### sig_float()
*sig_float(str_num:str="0", float_num:float=None)->None:*

sig_float objects have two in which ways they represent a number. A string holds the number with the correct number of significant figures. A float stores the numerical unrounded value for calculations. 

An instance of the sig_float class is created by providing the constructor with a string argument containing a numeric value. One can also provide the initial internal float value, but this is **not recommended**.
```python
sig_float("0012.0001")
```
The recommended usage of a sig_float object is is to create variables of type sig_float then use those variables in a mathmatical expression.
```python
Vi = sig_float("30.0")
Ti = sig_float("415.2")
Pi = sig_float("0.250")
Vf = sig_float("4.23")
Tf = sig_float("212.1")
Pf = (Tf * Pi * Vi) / (Vf * Ti) 
# Pf has value in sig_float("0.906")
``` 
<br>

### .sig_figs()
*sig_float()->int:*

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
### Division (/)
### Addition (+)
### Subtraction (-)
### .float
### .string
### str()
### bool()
### float()
### round_sig()
*round_sig(number, sig_figs:int):->sig_float*
