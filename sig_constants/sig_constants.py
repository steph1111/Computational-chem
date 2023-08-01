#!/usr/bin/env python3
"""
https://github.com/steph1111/PERCISE/blob/main/sig_float/sig_float.py
Module sig_constant contains the sig_constant class--common mathematical
constants of type sig_float
"""
__author__ = "Stephanie L'Heureux"

import sys 
sys.path.insert(0, "/Users/stephanie/Documents/PERCISE/sig_float") #allows import of modules from non-system folder
from sig_float import sig_float


class sig_constants:
  PI = sig_float("3.141592653589793238462643383279502884197", exact=True)
  e = sig_float("2.71828182845904523536028747135266249", exact=True)
  C = sig_float("299792458", {"m":1, "s":1}, exact=True)
  h = sig_float("6.62607015e-34", {"J":1, "s":1}, exact=True)
  NA = sig_float(" 6.02214076e+23", exact=True)
  R_atm = sig_float("0.08206", {"L":1, "atm":1}, {"K":1, "mol":1})
  R_mmHg = sig_float("62.36", {"L":1, "mmHg":1}, {"K":1, "mol":1})