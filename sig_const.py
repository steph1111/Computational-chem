"""
https://github.com/steph1111/PRECISE/blob/main/sig_const.py
Defines several common constants of type sig_float
"""
__author__ = "Stephanie L'Heureux"

from precise import sig_float

"""
Defines several common constants of type sig_float
"""

PI = sig_float("3.141592653589793238462643383279502884197", exact=True)  # Pi
e = sig_float("2.71828182845904523536028747135266249", exact=True)  # Euler's number
C = sig_float("299792458", {"m":1, "s":1}, exact=True)  # Speed of light
h = sig_float("6.626e-34", {"J":1, "s":1}, exact=True)  # Planck's constant 
NA = sig_float(" 6.022e+23", exact=True)  # Avogadro's number
R_atm = sig_float("0.08206", {"L":1, "atm":1}, {"K":1, "mol":1})  # Gas constant (atm)
R_mmHg = sig_float("62.36", {"L":1, "mmHg":1}, {"K":1, "mol":1})  # Gas constant (mmHg)