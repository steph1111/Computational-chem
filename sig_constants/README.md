<!-- PROJECT INTRO -->
<h1 align="center">sig_constants module</h1>

  <p align="center">
    Project GitHub Repo
    <br />
    <a href="https://github.com/steph1111/PRECISE/tree/main/sig_constants"><strong>sig_constants »</strong></a>
    <br />
    <br />
    <a href="https://github.com/steph1111/PERCISE/issues">Report Issue</a>
    ·
    <a href="https://github.com/users/steph1111/projects/5/views/1">Project status</a>
    ·
    <a href="https://github.com/steph1111/PERCISE/discussions/18">Discuss</a>
  </p>
</div>

<br>

---
## About The Module
This module provides several commonly used constants of type [sig_float](https://github.com/steph1111/PRECISE/tree/main/sig_float). 

<br>


---
## Getting Started

1. FIXME

<br>

---
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

---
## Usage
Any of the constants above can be used like any sig_float and may be instantiated as follows:
```python
sig_constants.C
```
