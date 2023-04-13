#!/usr/bin/env python3
"""
https://github.com/steph1111/Computational-chem/blob/main/Significant%20figures/sig_float.py
Module sig_float contains the sig_float class--instances 
of numbers that behave according to sig fig rules.
"""
__author__ = "Stephanie L'Heureux"

import warnings


class sig_float:
  """
  Defines a numerical float-like type that obides to significant figure rules:
  • All non-zero digits are significant.
  • All captive zeros are significant.
  • Trailing zeros are only significant if they
    follow a decimal point or have a bar written
    above them.
  • Leading zeros are never significant.
  """

  def __init__(self, str_number:str="0", units:str="")->None:
    """
    Initializes a sig_float object
    'str_number' has a default value of 0 
    """
  
    # If the user did not provide a string arguement, arguement 
    # is converted to a string and warning is raised
    if not isinstance(str_number, str):
      warnings.warn("Warning: Arguement should be of type str", PendingDeprecationWarning)
      str_number = str(str_number)
    
    # Initializations
    self._str = str_number
    self._sig_figs = self.sig_figs()
    self._precision = self.precision()
    self._float = float(self._str)
    self._units = units

  def sig_figs(self)->int:
    """
    Returns the number of sig figs of a sig_float object
    """
    
    # Default start and end
    start = 0
    end = len(self._str)
    negative = False

    # print(f"First {self._str}") # >>> test_2 = sig_float(8829.9000) -> First 8829.9

    # Account for negative
    if self._str[0] == "-":
      negative = True
      self._str = self._str[1:] 
   
    # Find stopping point of leading zeros
    for digit in self._str:
      if digit == "0":
        start += 1
      elif digit == ".":
        break
      else:
        break

    # Find stopping point of trailing zeros
    if self._str.find(".") != -1: # Contains decimal point
      self._str = self._str[start:] # Update string representation
      # Add the negative back in
      if negative:
        self._str = "-" + self._str
        start += 1
      return end - start - 1 # -1 to account for the "." char
    else:
      # Add the negative back in
      if negative:
        self._str = "-" + self._str
        start += 1
      # Iterate reversed string to find stopping point of trailing zeros
      string_num_reversed = reversed(self._str)
      for digit in string_num_reversed:
        if digit != "0":
          break     
        end -= 1
      self._str = self._str[start:] # Update string representation
    return end - start
  
  def precision(self)->int:
    """
    Returns the number of decimal places to which the number is percise to
    """
    index_decimal = self._str.find(".")
    if index_decimal != -1:
      return len(self._str) - self._str.find(".") -1
    return 0
  
  #TODO: Finish the section for when there is a decimal place
  def round_sig(self, sig_figs:int): #->sig_float
    # Deterine the number of digits
    negative = False
    if self._str[0] == "-":
      negative = True
    
    decimal_index = self._str.find(".")
    if decimal_index == -1:
      return sig_float(str(round(self._float, -sig_figs)))
    else:
      if not negative:
        pass
      else:
        pass
  
  # TODO: Implicate
  def scientific(self)->str:
    """
    Converts to a scientific notation string representation 
    """
    decimal_index = self._str.find(".")
    # if decimal_index == -1: 
    #   pass
    # if self._str[0] == "-":
    #   pass
  
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
    
    # FIXME Rounding causing issue?????
    return sig_float("404")
  
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
    
    # FIXME Rounding causing issue????? See _round_sig()
    return sig_float("404")

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
    sum_precision = min(self._precision, other._precision)
    temp_str = str(round(sum, sum_precision))

    # Remove trailing decimal python adds
    if sum_precision == 0:
      return sig_float(temp_str[:-2])

    return sig_float(temp_str)

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
    diff_precision = min(self._precision, other._precision)
    temp_str = str(round(diff, diff_precision))
  
    # Remove trailing decimal python adds
    if diff_precision == 0:
      return sig_float(temp_str[:-2])
  
    return sig_float(temp_str)
  
  @property
  def numeric(self)->float:
    """
    Returns a float representation of the number, may have improper sig figs. Use with caution!!
    Call by object.numeric
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
    # TODO: Ask how equality should work
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
  num1 = sig_float("13.0198")
  num2 = sig_float("1.2")
  print(f"1. {num1} + {num2} = {num1 + num2}")

  num1 = sig_float("94")
  num2 = sig_float("15")
  num3 = sig_float("182.113")
  print(f"2. {num1} + {num2} + {num3} = {num1 + num2 + num3}")

  num1 = sig_float("59.21")
  num2 = sig_float("18.8722")
  print(f"3. {num1} - {num2} = {num1 - num2}")

  num1 = sig_float("8.679")
  num2 = sig_float("0.3")
  num3 = sig_float("5.88")
  print(f"4. {num1} + {num2} + {num3} = {num1 + num2 + num3}")

  num1 = sig_float("2.36")
  num2 = sig_float("5.4")
  print(f"5. {num1} + {num2} = {num1 + num2}")

  num1 = sig_float("7.2361")
  num2 = sig_float("8.42")
  print(f"6. {num1} + {num2} = {num1 + num2}")

  num1 = sig_float("420.")
  num2 = sig_float("3.51")
  print(f"6. {num1} + {num2} = {num1 + num2}")

  # Should be 500
  num1 = sig_float("500")
  num2 = sig_float("1.365")
  print(f"7. {num1} + {num2} = {num1 + num2}")
