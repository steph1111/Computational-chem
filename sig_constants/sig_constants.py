#!/usr/bin/env python3
"""
https://github.com/steph1111/PERCISE/blob/main/sig_float/sig_float.py
Module sig_constant contains the sig_constant class--common mathatical
constants of type sig_float
"""
__author__ = "Stephanie L'Heureux"

import sys 
# sys.path.append("/Users/stephanie/Documents/PERCISE/sig_float")
sys.path.insert(0, "/Users/stephanie/Documents/PERCISE/sig_float") #allows import of modules from non-system folder
import sig_float


class sig_constants:
  PI = sig_float("3.14159265358979323846264")
  e = sig_float("2.71828182845904523536")
  C = sig_float("299792458", {"m":1}, {"s":1})
  # h = ("6.62607015 x 10^", ) PLANKS CONSTANT, need scientific notation
  # AVOGADROS_NUMBER = (" 6.02214076 × 10^23")
  R_atm = sig_float("0.08206", {"L":1, "atm":1}, {"K":1, "mol":1})
  R_mmHg = sig_float("62.36", {"L":1, "mmHg":1}, {"K":1, "mol":1})

  