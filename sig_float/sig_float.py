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

# TODO Implicate. Non hashable type this does not work
# DERIVED_UNITS = {
# ({"s":-1}):"Hz",
# ({"kg":1, "m":1, "s":-2}):"N",
# ({"kg":1, "m":-1, "s":-2}): "Pa",
# ({"m":2, "kg":1, "s":-2}): "J",
# ({"m":2, "kg":1, "s":-3}): "W"
# }

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

  # Decimal place after the number
  if digits(rounded_number) == sig_figs and rounded_number[-1] == "0" and no_decimal:
    rounded_number += "."

  # Distinguish significant digit with overline
  if digits(rounded_number) > sig_figs and rounded_number[sig_figs - 1] == "0" and sig_figs - 1 != 0:
    rounded_number = rounded_number[:sig_figs - 1] + "0̅" + rounded_number[sig_figs:]

  # Build the return sig_float
  if isinstance(number, sig_float):
    rounded_sig_float = sig_float(rounded_number, number._units, float_num=float_number)
  else:
    rounded_sig_float = sig_float(rounded_number, float_num=float_number)
  rounded_sig_float._sig_figs = sig_figs

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
    # If the user did not provide a string argument, argument is converted to a string and warning is raised
    if not isinstance(str_num, str):
      warnings.warn("Warning: Argument should be of type str", PendingDeprecationWarning)
      str_num = str(str_num)
    
    self._units = units
    self._exact = exact
    self._float = float(str_num) if float_num == None else float_num

    e_index = str_num.find("e")

    if e_index != -1: # The number is in scientific
      # Counts the number of sig figs in the number
      self._sig_figs = len(str_num[:e_index]) - 1 if str_num.find(".") != -1 else len(str_num[:e_index])

      # **SURPRESS SCIENTIFIC**
      exp = str_num[e_index + 1:] # Exponent
      # Number of decimal places for negative exponent
      n_places = -int(exp) + self._sig_figs - 1 # NEGATIVE
      # n_places # POSITIVE
      print(f"Surpress: {self._float:.{n_places}f}") # f'{number:.(required_number_of_decimal_places)f}'

      # self._str = str(self._float) + "0" * (self._sig_figs - (str(self._float) - 1))
      # Add overlined zero if needed
    else:
      self._str = str_num
      self._sig_figs = self.sig_figs() # Should be defined by 
      self._precision = self.precision()
      

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
      sig_figs_count -= len(self._str) - len(self._str.rstrip("00̅")) # What happens to overlined zeros?? This seems wrong

    # Re build the string representation
    self._str = "-0" + self._str if negative and self._str[0] == "." else "0" + self._str if self._str[
        0] == "." else "-" + self._str if negative else self._str

    return sig_figs_count

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

  def latex(self, format: int = 1, sci: bool = False) -> str:
    """
    Returns a string formatted using LaTeX
    format=1 (default): Units represented on one line using negative exponents
    format=2: Units represented as a fraction
    format=3: Units represented on one line using a fraction
    """
    # If there are any overlined digits, replace them with LaTeX format
    latex_str = self._str.replace("0̅", "\\bar{0}")

    if sci:
      latex_str = self._scientific().replace("x", "\\times")

    # Join positive units around " \cdot ". Formatted as unit^{exponent} or unit (if exponent is 1)
    pos_units = " \cdot ".join(unit if exponent == 1 else unit + "^{" + str(exponent) + "}" for unit, exponent in [(
        filtered_unit,
        filtered_exponent) for filtered_unit, filtered_exponent in self._units.items() if filtered_exponent > 0])
    if format == 1:
      # Join negative units around " \cdot ". Formatted as unit^{exponent}
      neg_units = " \cdot ".join(unit + "^{" + str(exponent) + "}" for unit, exponent in [(
          filtered_unit,
          filtered_exponent) for filtered_unit, filtered_exponent in self._units.items() if filtered_exponent < 0])
      if len(pos_units) == 0 and len(neg_units) == 0:  # If there are no units
        return latex_str
      elif len(pos_units) == 0:  # If there are only negative units
        return latex_str + " \; " + neg_units
      elif len(neg_units) == 0:  # If there are only positive units
        return latex_str + " \; " + pos_units
      else:  # Both negative and positive units
        return latex_str + " \; " + pos_units + " \cdot " + neg_units
    else:
      # Join negative units around " \cdot ". Formatted as unit^{abs(exponent)}
      neg_units = " \cdot ".join(
          unit if exponent == -1 else unit + "^{" + str(abs(exponent)) + "}" for unit, exponent in [(
              filtered_unit,
              filtered_exponent) for filtered_unit, filtered_exponent in self._units.items() if filtered_exponent < 0])
      if len(pos_units) == 0 and len(neg_units) == 0:  # If there are no units
        return latex_str
      elif len(pos_units) == 0:  # If there are only negative units
        return latex_str + " \\frac {" + "1" + "}{" + neg_units + "}" if format == 2 else latex_str + " \; 1 / " + neg_units
      elif len(neg_units) == 0:  # If there are only positive units
        return latex_str + " \; " + pos_units
      else:  # Both negative and positive unit
        return latex_str + " \\frac{" + pos_units + "}{" + neg_units + "}" if format == 2 else latex_str + " \; " + pos_units + " / " + neg_units

  def _scientific(self) -> str:
    """
    Returns the sig_float in scientific notation
    """
    scientific_notation = "{:e}".format(self._float)  # Python's builtin scientific notation conversion
    index = scientific_notation.find("e")  # Find the index of e to split on
    coefficient_temp = str(round(float(scientific_notation[:index]), self._sig_figs - 1))  # Split and round it
    coefficient = coefficient_temp if len(coefficient_temp) - 1 == self._sig_figs else coefficient_temp + "0" * (
        self._sig_figs - (len(coefficient_temp) - 1))  # Add extra zeros if needed
    exp = str(int(scientific_notation[index + 1:]))  # Split exponent

    return coefficient + " x 10^{" + exp + "}" if exp != "0" else self._str

  def exact(self) -> bool:
    """
    Returns if a sig_float is exact
    """
    return self._exact

  def _clear_units(self) -> None:
    """
    Clears units with value 0
    """
    for unit in list(self._units):
      if self._units[unit] == 0:
        del self._units[unit]

  def __mul__(self, other):  # ->sig_float
    """
    Multiplies two numbers of type sig_float with * using sig fig rules
    """
    # Ensures both operands are of type sig_float
    if not isinstance(other, sig_float):
      other = sig_float(other)
      warnings.warn("Warning: Operands should be of type sig_float", PendingDeprecationWarning)

    # Multiply
    product = self._float * other._float

    # Create new units of the product
    new_units = {
        unit: self._units.get(unit, 0) + other._units.get(unit, 0)
        for unit in itertools.chain(self._units, other._units)
    }

    # Choose product sig figs
    product_sig_figs = None if self._exact and other._exact else other._sig_figs if self._exact else self._sig_figs if other._exact else min(
        self._sig_figs, other._sig_figs)

    # If both numbers are exact, build return product
    if product_sig_figs == None:
      return_product = sig_float(str(product), units=new_units, exact=True, float_num=product)
    else:
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

    # Divide
    quotient = self._float / other._float

    # Create new units of the quotient
    new_units = {
        unit: self._units.get(unit, 0) - other._units.get(unit, 0)
        for unit in itertools.chain(self._units, other._units)
    }

    # Choose quotient sig figs
    quotient_sig_figs = None if self._exact and other._exact else other._sig_figs if self._exact else self._sig_figs if other._exact else min(
        self._sig_figs, other._sig_figs)

    # If both numbers are exact, build return quotient
    if quotient_sig_figs == None:
      return_quotient = sig_float(str(quotient), units=new_units, exact=True, float_num=quotient)
    else:
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

    # Choose sum precision
    sum_precision = None if self._exact and other._exact else other._sig_figs if self._exact else self._sig_figs if other._exact else sig_float._round_precision(
        self._precision, other._precision)

    # If both numbers are exact
    if sum_precision == None:
      return sig_float(str(sum), units=self._units, exact=True, float_num=sum)

    # Round to correct precision
    temp_str = str(round(sum, sum_precision))

    # Remove trailing decimal python adds
    if sum_precision <= 0:
      temp_str = temp_str[:-2]

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

    # Choose difference precision
    diff_precision = None if self._exact and other._exact else other._sig_figs if self._exact else self._sig_figs if other._exact else sig_float._round_precision(
        self._precision, other._precision)

    # If both numbers are exact
    if diff_precision == None:
      return sig_float(str(diff), units=self._units, exact=True, float_num=diff)

    # Round to correct precision
    temp_str = str(round(diff, diff_precision))

    # Remove trailing decimal python adds
    if diff_precision <= 0:
      temp_str = temp_str[:-2]

    return sig_float(temp_str, units=self._units, float_num=diff)

  def __pow__(self, other):  # -> sig_float
    """
    Raises a sig_float to a power. Intended to be used with floats and ints
    """
    if isinstance(other, sig_float):
      product = math.pow(self._float, other._float)
      other = other._float
    else:
      product = math.pow(self._float, other)
    other = int(other) if other - int(other) == 0 else other

    # Construct new units
    new_units = {unit: self._units.get(unit, 0) * other for unit in self._units}

    # Choose sig figs for answer
    product_sig_figs = None if self._exact else self._sig_figs

    # If both numbers are exact, build return product
    if product_sig_figs == None:
      return_product = sig_float(str(product), units=new_units, exact=True, float_num=product)
    else:
      # Build return product as a sig_float
      return_product = round_sig(product, product_sig_figs)  # Rounds to proper sig figs
      return_product._units = new_units
    return_product._clear_units()

    return return_product

  def __str__(self) -> str:
    """
    Returns a string representation of the number with correct sig figs and units
    """
    # temp = self._str + " " + " ".join(
    #     unit if exponent == 1 else unit + "^" + str(exponent) for unit, exponent in self._units.items())
    # return temp.strip()
    return self.latex()

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
      self._exact = other._exact
    else:
      self = sig_float(other)


if __name__ == "__main__":
  pass