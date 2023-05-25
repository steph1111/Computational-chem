#!/usr/bin/env python3
"""
https://github.com/steph1111/PERCISE/blob/main/sig_float/sig_float.py
Module sig_float contains the sig_float class--instances 
of numbers that behave according to sig fig rules.
"""
__author__ = "Stephanie L'Heureux"

import warnings
import math
import itertools

# TODO Implicate
# DERIVED_UNITS = {
# ({"s":-1}):"Hz",
# ({"kg":1, "m":1, "s":-2}):"N",
# ({"kg":1, "m":-1, "s":-2}): "Pa",
# ({"m":2, "kg":1, "s":-2}): "J",
# ({"m":2, "kg":1, "s":-3}): "W"
# }

# if units in DERIVED_UNITS:
# Frozen set

# TODO: REWRITE THIS TO BE BETTER   
def round_sig(number, sig_figs: int):  #->sig_float
  """
  Rounds a number to a certain number of significant figures
  """

  # Function that counts the number of valid digits in a string representation of a number
  def digits(num: str) -> int:
    num_digits = len(num)
    if num.find("-") != -1:
      num_digits -= 1
    if num.find(".") != -1:
      num_digits -= 1
    return num_digits

  # Float representation
  float_number = float(number)

  # Rounds the number to the correct number of sig figs
  rounded_number = str(round(float_number, sig_figs - int(math.floor(math.log10(abs(float_number)))) - 1))

  # Remove trailing decimal python adds
  if rounded_number[-2:] == ".0" and sig_figs != len(rounded_number) - 1:
    rounded_number = rounded_number[:-2]

  # Notes if the number has a decimal place
  no_decimal = rounded_number.find(".") == -1

  # If there should be trailing significant zeros
  if len(rounded_number) < sig_figs:
    if no_decimal:
      rounded_number += "." + (sig_figs - len(rounded_number)) * "0"
      no_decimal = False
    else:
      rounded_number += ("0" * (sig_figs - len(rounded_number) - 1))

  # Build the return sig_float
  if isinstance(number, sig_float):
    rounded_sig_float = sig_float(rounded_number, number._units, float_number)
  else:
    rounded_sig_float = sig_float(rounded_number, float_num=float_number)
  rounded_sig_float._sig_figs = sig_figs

  # Distinguish significant digit with overline
  if digits(rounded_number) > sig_figs and rounded_number[sig_figs - 1] == "0":
    rounded_sig_float._str = rounded_number[:sig_figs - 1] + "0̅" + rounded_number[sig_figs:]

  # Decimal place after the number
  if digits(rounded_number) == sig_figs and rounded_number[-1] == "0" and no_decimal:
    rounded_sig_float._str = rounded_number + "."

  return rounded_sig_float


class sig_float:
  """
  Defines a numerical float-like type that obides to significant figure rules:
  • All non-zero digits are significant.
  • All captive zeros are significant.
  • Trailing zeros are only significant if they
    follow a decimal point
  • Leading zeros are never significant.
  """

  def __init__(self, str_num: str = "0", units: dict = dict(), exact: bool = False, float_num: float = None) -> None:
    """
    Initializes a sig_float object
    'str_num has a default value of 0 
    """
    # If the user did not provide a string argument, argument
    # is converted to a string and warning is raised
    if not isinstance(str_num, str):
      warnings.warn("Warning: Argument should be of type str", PendingDeprecationWarning)
      str_num = str(str_num)

    # Initializations
    self._str = str_num
    self._sig_figs = self.sig_figs()
    self._precision = self.precision()
    self._units = units
    self._exact = exact
    if float_num != None:
      self._float = float_num
    else:
      self._float = float(self._str)

  @staticmethod
  def _round_precision(val_1: int, val_2: int) -> int:
    """
    Given two place values, determines which to round to. Uses
    the place convention defined in precision() 
    Number:      138828.9823
    Place:     -(543210)1234
    """
    if val_1 >= 0 and val_2 >= 0:  # Rounding with two decimals
      return min(val_1, val_2)
    elif val_1 <= 0 and val_2 <= 0:  # Rounding with two whole numbers
      return -max(abs(val_1), abs(val_2))
    else:  # Rounding with a decimal and a whole number
      return min(val_1, val_2)

  def sig_figs(self) -> int:
    """
    Returns the number of sig figs of a sig_float object
    """
    negative = True if self._str[0] == "-" else False

    # Remove leading zeros and negative
    self._str = self._str.lstrip("-00̅")

    # Count the initial sig figs from the front
    sig_figs_count = len(self._str.lstrip(".0"))

    # Count the sig figs from the back
    if self._str.find(".") != -1 and self._str[0] != ".":
      sig_figs_count -= 1
    elif self._str.find(".") == -1 and self._str[0] != ".":
      sig_figs_count -= len(self._str) - len(self._str.rstrip("00̅"))

    # Re build the string representation
    self._str = "-0" + self._str if negative and self._str[0] == "." else "0" + self._str if self._str[
        0] == "." else "-" + self._str if negative else self._str

    return sig_figs_count

  def precision(self) -> int:
    """
    Returns the number of decimal places to which the number is precise to
    Returns a negative number if should be precise to a whole number value
    Number:      138828.9823
    Place:     -(543210)1234
    """
    index = self._str.find(".")
    if index != -1:
      return len(self._str) - index - 1
    else:
      index = 0
      for digit in reversed(self._str):
        if digit != "0":
          break
        index -= 1
    return index

  # TODO: Implicate
  def scientific(self) -> str:
    """
    Converts to a scientific notation string representation 
    """
    pass

  def _clear_units(self) -> None:
    """
    Clears units with value 0
    """
    for unit in list(self._units):
      if self._units[unit] == 0:
        del self._units[unit]

  def latex(self, format: int = 1) -> str:
    pos_units = " \cdot ".join(unit if exponent == 1 else unit + "^{" + str(exponent) + "}" for unit, exponent in [(
        filtered_unit,
        filtered_exponent) for filtered_unit, filtered_exponent in self._units.items() if filtered_exponent > 0])
    if format == 1:
      neg_units = " \cdot ".join(unit + "^{" + str(exponent) + "}" for unit, exponent in [(
          filtered_unit,
          filtered_exponent) for filtered_unit, filtered_exponent in self._units.items() if filtered_exponent < 0])
      if len(pos_units) == 0 and len(neg_units) == 0:
        return self._str
      elif len(pos_units) == 0:
        return self._str + " \; " + neg_units
      elif len(neg_units) == 0:
        return self._str + " \; " + pos_units
      else:
        return self._str + " \; " + pos_units + " \cdot " + neg_units
    else:
      neg_units = " \cdot ".join(
          unit if exponent == -1 else unit + "^{" + str(abs(exponent)) + "}" for unit, exponent in [(
              filtered_unit,
              filtered_exponent) for filtered_unit, filtered_exponent in self._units.items() if filtered_exponent < 0])
      if len(pos_units) == 0 and len(neg_units) == 0:
        return self._str
      elif len(pos_units) == 0:
        return self._str + " \\frac {" + "1" + "}{" + neg_units + "}"
      elif len(neg_units) == 0:
        return self._str + " \; " + pos_units
      else:
        return self._str + " \\frac{" + pos_units + "}{" + neg_units + "}"

  def __mul__(self, other):  # ->sig_float
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

    new_units = {
        unit: self._units.get(unit, 0) + other._units.get(unit, 0)
        for unit in itertools.chain(self._units, other._units)
    }

    # Build return product as a sig_float
    return_product = round_sig(product, product_sig_figs)  # Rounds to proper sig figs
    return_product._units = new_units
    return_product._clear_units()

    return return_product

  def __truediv__(self, other):  # ->sig_float
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

    # Update units
    new_units = {
        unit: self._units.get(unit, 0) - other._units.get(unit, 0)
        for unit in itertools.chain(self._units, other._units)
    }

    # Build return quotient as a sig_float
    return_quotient = round_sig(quotient, quotient_sig_figs)  # Rounds to proper sig figs
    return_quotient._units = new_units
    return_quotient._clear_units()

    return return_quotient

  def __add__(self, other):  # ->sig_float
    """
    Adds two numbers of type sig_float with + using sig fig rules
    """
    # Ensures both operands units are the same
    if self._units != other._units:
      raise Exception("Error: Units must match")

    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    # Addition using sig fig rules
    sum = self._float + other._float
    sum_precision = sig_float._round_precision(self._precision, other._precision)
    temp_str = str(round(sum, sum_precision))

    # Remove trailing decimal python adds
    if sum_precision <= 0:
      return sig_float(temp_str[:-2])

    return sig_float(temp_str, units=self._units, float_num=sum)

  def __sub__(self, other):  # ->sig_float
    """
    Subtracts two numbers of type sig_float with + using sig fig rules
    """
    # Ensures both operands units are the same
    if self._units != other._units:
      raise Exception("Error: Units must match")

    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    # Subtraction using sig fig rules
    diff = self._float - other._float
    diff_precision = sig_float._round_precision(self._precision, other._precision)
    temp_str = str(round(diff, diff_precision))

    # Remove trailing decimal python adds
    if diff_precision <= 0:
      return sig_float(temp_str[:-2])

    return sig_float(temp_str, units=self._units, float_num=diff)

  def __str__(self) -> str:
    """
    Returns a string representation of the number with correct sig figs and units
    """
    return self._str + " " + " ".join(
        unit if exponent == 1 else unit + "^" + str(exponent) for unit, exponent in self._units.items())

  def __bool__(self) -> bool:
    """
    Applies standard numeric to bool coversions. 0 is false, non-zero is true
    """
    return bool(self._float)

  def __float__(self) -> float:
    """
    Returns a float representation of the number, may have improper sig figs. Use with caution!!
    """
    return self._float

  def __repr__(self) -> str:
    return f"{type(self).__name__}('{self}')"

  def __eq__(self, other) -> bool:
    """
    Evaluates if two numbers of type sig_float are equal
    """
    # TODO: Ask how equality should work
    raise NotImplementedError("Equality not implicated yet. Todo")
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._str == other._str

  def __ne__(self, other) -> bool:
    """
    Evaluates if two numbers of type sig_float are not equal
    """
    raise NotImplementedError("Not equal not implicated yet. Todo")
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._str != other._str

  def __lt__(self, other) -> bool:
    """
    Evaluates if a number is less than another number. 
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float < other._float

  def __le__(self, other) -> bool:
    """
    Evaluates if a number is less or equal to than another number. 
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float <= other._float

  def __gt__(self, other) -> bool:
    """
    Evaluates if a number is greater than another number.
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float > other._float

  def __ge__(self, other) -> bool:
    """
    Evaluates if a number is greater than or equal to another number. 
    Numbers should be of type sig_float
    """
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    return self._float >= other._float

  def __assign__(self, other):
    """
    Assigns an object to an object of type sig_float
    """
    if isinstance(other, sig_float):
      self._str = other._str
      self._sig_figs = other._sig_figs
      self._precision = other._precision
      self._float = other._float
      self._units = other._units
    else:
      self = sig_float(other)


if __name__ == "__main__":
  pass
