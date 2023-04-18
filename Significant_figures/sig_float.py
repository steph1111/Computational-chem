#!/usr/bin/env python3
"""
https://github.com/steph1111/Computational-chem/blob/main/Significant_figures/sig_float.py
Module sig_float contains the sig_float class--instances 
of numbers that behave according to sig fig rules.
"""
__author__ = "Stephanie L'Heureux"

import warnings
import math


def round_precision(val_1:int, val_2:int)->int:
  """
  Given two place values, determines which to round to. Uses
  the place convention defined in precision() 
  Number:      138828.9823
  Place:     -(543210)1234
  """
  if val_1 >= 0 and val_2 >= 0: # Rounding with two decimals
    return min(val_1, val_2)
  elif val_1 <= 0 and val_2 <= 0: # Rounding with two whole numbers
    return -max(abs(val_1), abs(val_2))
  else: # Rounding with a decimal and a whole number
    return min(val_1, val_2)

def round_sig(number, sig_figs:int): #->sig_float
  """
  Rounds a number to a certain number of significant figures
  """
  # If given a number of type sig_float, use the numemeric atribute in calculations
  if type(number) == sig_float:
    number = number.float

  # Rounds the number to the correct number of sig figs
  rounded_number = str(round(number, sig_figs - int(math.floor(math.log10(abs(number)))) - 1))

  # Remove trailing decimal python adds
  if rounded_number[-2:] == ".0" and sig_figs != len(rounded_number) - 1:
    rounded_number = rounded_number[:-2] 
  
  # If there should be trailing significant zeros
  if len(rounded_number) < sig_figs:
    if rounded_number.find(".") == -1:
      rounded_number += "." +  (sig_figs - len(rounded_number)) * "0"
    else:
      rounded_number += ("0" *  (sig_figs - len(rounded_number) - 1))

  return sig_float(rounded_number, float_num=number)


class sig_float:
  """
  Defines a numerical float-like type that obides to significant figure rules:
  • All non-zero digits are significant.
  • All captive zeros are significant.
  • Trailing zeros are only significant if they
    follow a decimal point
  • Leading zeros are never significant.
  """

  def __init__(self, str_num:str="0", float_num:float=None, units:str="")->None:
    """
    Initializes a sig_float object
    'str_number' has a default value of 0 
    """
    # If the user did not provide a string arguement, arguement 
    # is converted to a string and warning is raised
    if not isinstance(str_num, str):
      warnings.warn("Warning: Arguement should be of type str", PendingDeprecationWarning)
      str_number = str(str_num)
    
    # Initializations
    self._str = str_num
    self._sig_figs = self.sig_figs()
    self._precision = self.precision()
    if float_num != None:
      self._float = float_num
    else:
      self._float = float(self._str)
    self._units = units # Not implemented yet. See github for idea

  def sig_figs(self)->int:
    """
    Returns the number of sig figs of a sig_float object
    """
    # Default start and end
    start = 0
    end = len(self._str)
    negative = False

    # Account for negative
    if self._str[0] == "-":
      negative = True
      self._str = self._str[1:] 
   
    # Find stopping point of leading zeros
    for digit in self._str:
      if digit == "0":
        start += 1
      elif digit != ".":
        break
  
    if self._str[:2] != "0.":
      self._str = self._str[start:] # Update string representation

    if negative: 
      self._str = "-" + self._str # Add the negative back in
      start += 1 # Negative sign should not be counted as a sig fig
    
    # Find stopping point of trailing zeros
    if self._str.find(".") != -1: # Contains decimal point
      return end - start - 1 # -1 to account for the "." char
    else:
      # Iterate reversed string to find stopping point of trailing zeros
      string_num_reversed = reversed(self._str)
      for digit in string_num_reversed:
        if digit != "0":
          break 
        end -= 1
    return end - start
  
  def precision(self)->int:
    """
    Returns the number of decimal places to which the number is percise to
    Returns a negative number if should be percise to a whole number value
    Number:      138828.9823
    Place:     -(543210)1234
    """
    index = self._str.find(".")
    if index != -1:
      return len(self._str) - index -1
    else:
      index = 0
      for digit in reversed(self._str):
        if digit != "0":
          break
        index -= 1
    return index
  
  # TODO: Implicate
  def scientific(self)->str:
    """
    Converts to a scientific notation string representation 
    """
    pass
  
  def __mul__(self, other): # ->sig_float
    """
    Multiplies two numbers of type sig_float with * using sig fig rules
    """
    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    # Multiplication using sig fig rules  
    product = self._float * other._float
    product_sig_figs = min(self._sig_figs, other.sig_figs())

    return round_sig(product, product_sig_figs)
  
  def __truediv__(self, other): # ->sig_float
    """
    Divides two numbers of type sig_float with / using sig fig rules
    """
    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    # Multiplication using sig fig rules  
    quotient = self._float / other._float
    quotient_sig_figs = min(self._sig_figs, other.sig_figs())

    return round_sig(quotient, quotient_sig_figs)

  def __add__(self, other): # ->sig_float
    """
    Adds two numbers of type sig_float with + using sig fig rules
    """
    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)
    
    # Addition using sig fig rules
    sum = self._float + other._float
    sum_precision = round_precision(self._precision, other._precision)
    temp_str = str(round(sum, sum_precision))

    # Remove trailing decimal python adds
    if sum_precision <= 0:
      return sig_float(temp_str[:-2])

    return sig_float(temp_str, float_num=sum)

  def __sub__(self, other): # ->sig_float
    """
    Subtracts two numbers of type sig_float with + using sig fig rules
    """
    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    # Subtraction using sig fig rules
    diff = self._float - other._float
    diff_precision = round_precision(self._precision, other._precision)
    temp_str = str(round(diff, diff_precision))
  
    # Remove trailing decimal python adds
    if diff_precision <= 0:
      return sig_float(temp_str[:-2])
  
    return sig_float(temp_str, float_num=diff)
  
  @property
  def float(self)->float:
    """
    Returns a float representation of the number, may have improper sig figs. Use with caution!!
    Call by object.float
    """
    return self._float

  @property
  def string(self)->str:
    """
    Returns a string represntation of the number
    Call by object.string
    """
    return self._str

  def __str__(self)->str:
    """
    Returns a string represntation of the number with correct sig figs
    """
    return self._str
  
  def __bool__(self)->bool:
    """
    Applies standard numeric to bool coversions. 0 is false, non-zero is true
    """
    return bool(self._float)
  
  def __float__(self)->float:
    """
    Returns a float represntation of the number, may have improper sig figs. Use with caution!!
    """
    return self._float
  
  def __repr__(self)->str:
    return f"{type(self).__name__}('{self}')"
  
  def __eq__(self, other)->bool:
    """
    Evaluates if two numbers of type sig_float are equal
    """
    # TODO: Ask how equality should work
    raise NotImplementedError("Equality not implicated yet. Todo")
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._str == other._str

  def __ne__(self, other)->bool:
    """
    Evaluates if two numbers of type sig_float are not equal
    """
    raise NotImplementedError("Not equal not implicated yet. Todo")
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._str != other._str

  
  def __lt__(self, other)->bool:
    """
    Evaluates if a number is less than another number. 
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float < other._float
  
  def __le__(self, other)->bool:
    """
    Evaluates if a number is less or equal to than another number. 
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float <= other._float

  def __gt__(self, other)->bool:
    """
    Evaluates if a number is greater than another number.
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float > other._float
  
  def __ge__(self, other)->bool:
    """
    Evaluates if a number is greater than or equal to another number. 
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float >= other._float

if __name__ == "__main__":
  pass
