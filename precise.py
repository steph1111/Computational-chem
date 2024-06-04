"""
Module SigFloat contains the SigFloat class, 
of numbers that behave according to sig fig rules.
"""
from itertools import chain
from math import floor, log10, pow

__author__ = "Stephanie L'Heureux"


class SigFloat:
    """
    Defines a numerical float-like type that abides to significant figure rules:
    - All non-zero digits are significant.
    - All captive zeros are significant.
    - Trailing zeros are only significant if they follow a decimal point
    - Leading zeros are never significant.
    """

    def __init__(self, str_num: str = "0", units: dict[str, int] = None, exact: bool = False):
        """
        Initializes a SigFloat object.

        Args:
            str_num: A string of the number to make a SigFloat out of
            units: A dictionary of units and the power to which they are raised.
                Keys are units and values are powers. (optional)
            exact: If True, the number is exact and sig figs are infinite. Otherwise (False),
                sig figs are determined by standard rules. (optional)
        """
        if not isinstance(str_num, str):
            raise TypeError("Error: Argument str_num must be of type str")

        # Replace over-lined zeros with `O` internally
        str_num.replace("\u03050", "O")
        str_num.replace("\\bar{0}", "O")
        str_num.replace("\bar{0}", "O")

        self._units = units if units is not None else {} 
        self._exact = exact

        temp = str_num
        self._float = float(str_num.replace("O", "0"))
        str_num = temp

        # If the number is given in scientific notation
        if str_num.find("e") != -1:
            # Count the number of digits in the coefficient. All are significant
            self._sig_figs = SigFloat._digits(str_num.split("e")[0])
            self._str = SigFloat._suppress_sci(str_num, self._sig_figs)
        else:
            self._str = str_num
            self._sig_figs = self.sig_figs()

        self._precision = self.precision()

    def sig_figs(self) -> int:
        """
        Count the number of sig figs of a `SigFloat` object.
        And cleans the string representation.

        Return:
            An integer specifying the number of sig figs in a number.
        """
        neg = self._str[0] == "-"
        
        # Remove leading zeros and negative
        self._str = self._str.lstrip("-0O")

        # Count the initial sig figs from the front
        count = len(self._str.lstrip(".0"))

        # Count the sig figs from the back
        if self._str[0] != ".":
            if self._str.find(".") != -1:
                count -= 1
            else:
                count -= len(self._str) - len(self._str.rstrip("0"))
        
        # Re-build the string representation
        if self._str[0] == ".":
            self._str = "0" + self._str
        if neg:
            self._str = "-" + self._str
        
        return count

    def precision(self):
        """
        The number of decimal places to which the number is precise to
        Number:      138828.9823
        Place:     -(543210)1234

        Returns:
          A integer value in which the precision of decimals is positive,
          and a negative number is returned if precise to a whole number value.
          Refer to the convention above.
        """
        if (index:= self._str.find(".")) != -1:
            return len(self._str) - index - 1

        index = 0
        for digit in reversed(self._str):
            if digit != "0":
                break
            index -= 1
        return index

    @staticmethod
    def round_sig(num, sig_figs: int):
        """
        Rounds a number to a certain number of significant figures

        Args:
            num: The number to round
            sig_figs: The number of sig figs to round `num` to

        Return:
            `num` rounded to have `sig_figs` sig figs as a SigFloat object.
        """
        # Float representation
        float_num = float(num)

        # Rounds the number to the correct number of sig figs
        rounded_num = str(
            round(
                float_num, sig_figs - int(floor(log10(abs(float_num)))) - 1
            )
        )

        # Remove trailing decimal python adds
        if rounded_num[-2:] == ".0" and sig_figs != len(rounded_num) - 1:
            rounded_num = rounded_num[:-2]
        
        # Notes if the number has a decimal place
        no_decimal = rounded_num.find(".") == -1

        # If there should be trailing significant zeros
        if len(rounded_num) < sig_figs:
            # No decimal point
            if no_decimal:
                rounded_num += "." + (sig_figs - len(rounded_num)) * "0"
                no_decimal = False
            else:
                rounded_num += "0" * (sig_figs - len(rounded_num) - 1)

        digits = SigFloat._digits(rounded_num)
    
        # Decimal place after the number
        if digits == sig_figs and rounded_num[-1] == "0" and no_decimal:
            rounded_num += "."
        
        # Distinguish significant digit with overline placeholder O
        if digits > sig_figs and rounded_num[sig_figs - 1] == "0" and sig_figs - 1 != 0:
            rounded_num = rounded_num[: sig_figs - 1] + "O" + rounded_num[sig_figs:]

        # Create new SigFloat object of the resultant
        if isinstance(num, SigFloat):
            temp = SigFloat(rounded_num, num._units, num._exact)
        else:
            temp = SigFloat(rounded_num)
        temp._float = float_num
        temp._sig_figs = sig_figs

        return temp
    
    # TODO: Refactor
    def latex(self, format: int = 1, sci: bool = False) -> str:
        """
        String formatted using LaTeX

        Parameters:
          format : int = 1
            format=1 (default): Units represented on one line using negative exponents
            format=2: Units represented as a fraction
            format=3: Units represented on one line using a fraction
          sci : bool = False
            If True, uses scientific notation. If False, does not use scientific. If not
            provided, scientific is used when the number contains more than `MAX=6`
            trailing/leading zeros

          Returns:
            A string representation of the SigFloat formatted with LaTeX
        """
        if not sci:
            digits = SigFloat._digits(self._str)
            leading = digits - len(self._str.lstrip("0."))
            trailing = digits - len(self._str.rstrip("0."))
            zeros = (
                leading if leading > trailing else trailing
            )  # Maximum number of trailing/leading zeros before sci=True is applied
            MAX = 6
            # Determine if scientific notation should be used
            sci = zeros >= MAX

        # If there are any overlined digits, replace them with LaTeX format
        latex_str = self._str.replace("O", "\\bar{0}")

        if sci:
            latex_str = self._scientific()

        # Join positive units around " \cdot ". Formatted as unit^{exponent} or unit (if exponent is 1)
        pos_units = " \cdot ".join(
            unit if exponent == 1 else unit + "^{" + str(exponent) + "}"
            for unit, exponent in [
                (filtered_unit, filtered_exponent)
                for filtered_unit, filtered_exponent in self._units.items()
                if filtered_exponent > 0
            ]
        )
        if format == 1:
            # Join negative units around " \cdot ". Formatted as unit^{exponent}
            neg_units = " \cdot ".join(
                unit + "^{" + str(exponent) + "}"
                for unit, exponent in [
                    (filtered_unit, filtered_exponent)
                    for filtered_unit, filtered_exponent in self._units.items()
                    if filtered_exponent < 0
                ]
            )
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
                unit if exponent == -1 else unit + "^{" + str(abs(exponent)) + "}"
                for unit, exponent in [
                    (filtered_unit, filtered_exponent)
                    for filtered_unit, filtered_exponent in self._units.items()
                    if filtered_exponent < 0
                ]
            )
            if len(pos_units) == 0 and len(neg_units) == 0:  # If there are no units
                return latex_str
            elif len(pos_units) == 0:  # If there are only negative units
                return (
                    latex_str + " \\frac {" + "1" + "}{" + neg_units + "}"
                    if format == 2
                    else latex_str + " \; 1 / " + neg_units
                )
            elif len(neg_units) == 0:  # If there are only positive units
                return latex_str + " \; " + pos_units
            else:  # Both negative and positive unit
                return (
                    latex_str + " \\frac{" + pos_units + "}{" + neg_units + "}"
                    if format == 2
                    else latex_str + " \; " + pos_units + " / " + neg_units
                )

    # TODO: Refactor
    def _scientific(self) -> str:
        """
        Helper function that converts to scientific notation

        Returns:
          A string of the SigFloat in scientific notation
        """
        scientific_notation = "{:e}".format(
            self._float
        )  # Python's builtin scientific notation conversion
        temp_coef, temp_exp = scientific_notation.split(
            "e"
        )  # Split coefficient and exponent on e character
        if self._sig_figs > 1:
            rounded_coef = str(
                round(float(temp_coef), self._sig_figs - 1)
            )  # Round coefficient
            coef = (
                rounded_coef
                if len(rounded_coef) - 1 == self._sig_figs
                else rounded_coef + "0" * (self._sig_figs - (len(rounded_coef) - 1))
            )  # Add extra zeros if needed
        else:
            coef = str(int(float(temp_coef)))
        exp = str(int(temp_exp))  # Exponent

        return coef + " \\times 10^{" + exp + "}" if exp != "0" else self._str


    def __add__(self, other):
        """
        Adds two numbers of type SigFloat with + using sig fig rules.

        Return:
            The sum of the values.
        """
        # Ensures both operands are of type SigFloat
        if not isinstance(other, SigFloat):
            raise TypeError("Error: Arguments must be of type SigFloat")

        # Ensures both operands units are the same
        if self._units != other._units:
            raise Exception("Error: Units must match")

        return self._sum_diff_calc(other, self._float + other._float)

    def __sub__(self, other):
        """
        Subtracts two numbers of type SigFloat with - using sig fig rules

        Return:
            The difference of the values.
        """
        # Ensures both operands are of type SigFloat
        if not isinstance(other, SigFloat):
            raise TypeError("Error: Arguments must be of type SigFloat")

        # Ensures both operands units are the same
        if self._units != other._units:
            raise Exception("Error: Units must match")

        return self._sum_diff_calc(other, self._float - other._float)

    def __mul__(self, other):
        """
        Multiplies two numbers of type SigFloat with * using sig fig rules

        Return:
            The product of the values
        """
        # Ensures both operands are of type SigFloat
        if not isinstance(other, SigFloat):
            raise TypeError("Error: Arguments must be of type SigFloat")

        return self._prod_quotient_calc(other, self._float * other._float, "*")
    
    def __truediv__(self, other):
        """
        Divides two numbers of type SigFloat with / using sig fig rules

        Return:
            The quotient of the values.
        """
        # Ensures both operands are of type SigFloat
        if not isinstance(other, SigFloat):
            raise TypeError("Error: Arguments must be of type SigFloat")

        return self._prod_quotient_calc(other, self._float / other._float, "/")

    # TODO: This does not work correctly for two SigFloats
    def __pow__(self, other: int):
        """
        Raises a SigFloat to a power. Intended to be used with SigFloat and ints.

        Return:
          The resultant of a SigFloat raised to an int.
        """
        # If instance of SigFloat, use the float attribute
        if isinstance(other, SigFloat):
            other = other._float
        
        resultant = pow(self._float, other)
        other = int(other) if other - int(other) == 0 else other

        # Construct new units
        new_units = {unit: self._units.get(unit, 0) * other for unit in self._units}

        # Choose sig figs for answer
        sig_figs = None if self._exact else self._sig_figs

        # Both numbers are exact
        if sig_figs is None:
            temp = SigFloat(str(resultant), units=new_units, exact=True)
            temp._float = resultant
        else: # Round the resultant correctly
            temp = SigFloat.round_sig(resultant, sig_figs)
            temp._units = new_units
        
        temp._clear_units()
    
        return temp


    def exact(self) -> bool:
        """
        Determines if a SigFloat is exact

        Returns:
          True if the SigFloat is exact, otherwise False
        """
        return self._exact

    def __bool__(self) -> bool:
        """
        Applies standard numeric to bool conventions.

        Return:
            Zero is False, non-zero is True.
        """
        return bool(self._float)

    def __float__(self) -> float:
        """
        Float representation of the number, may have improper sig figs. Use with caution!!

        Return:
            Float representation
        """
        return self._float
    
    def __str__(self) -> str:
        """
        String representation of the number with correct sig figs and units.
        Enables usage of print()

        Returns:
          The return value of the .latex()
        """
        return self.latex()

    def __repr__(self) -> str:
        """
        Representation of SigFloat for REPL usage

        Returns:
          A string formatted as SigFloat('value')
        """
        return f"{type(self).__name__}('{self}')"
    
    def __lt__(self, other) -> bool:
        """
        Evaluates if a number is less than another number.
        Numbers should be of type SigFloat
        """
        if not isinstance(other, SigFloat):
            raise TypeError("Error: Arguments must be of type SigFloat")

        return self._float < other._float

    def __le__(self, other) -> bool:
        """
        Evaluates if a number is less or equal to than another number.
        Numbers should be of type SigFloat
        """
        if not isinstance(other, SigFloat):
            raise TypeError("Error: Arguments must be of type SigFloat")

        return self._float <= other._float

    def __gt__(self, other) -> bool:
        """
        Evaluates if a number is greater than another number.
        Numbers should be of type SigFloat
        """
        if not isinstance(other, SigFloat):
            raise TypeError("Error: Arguments must be of type SigFloat")

        return self._float > other._float

    def __ge__(self, other) -> bool:
        """
        Evaluates if a number is greater than or equal to another number.
        Numbers should be of type SigFloat
        """
        if not isinstance(other, SigFloat):
            raise TypeError("Error: Arguments must be of type SigFloat")

        return self._float >= other._float

    def __assign__(self, other):
        """
        Assigns an object to an object of type SigFloat
        """
        if not isinstance(other, SigFloat):
            raise TypeError("Error: Arguments must be of type SigFloat")
        self._str = other._str
        self._sig_figs = other._sig_figs
        self._precision = other._precision
        self._float = other._float
        self._units = other._units
        self._exact = other._exact

    # TODO: Double check that this seems reasonable
    def _clear_units(self) -> None:
        """
        Helper function that clears units with power 0.
        """
        for unit in list(self._units):
            if self._units[unit] == 0:
                del self._units[unit]
    
    def _sum_diff_calc(self, other, ans: float):
        """
        Given an addition or subtraction calculation, determines the result
        with proper precision.

        Args:
            other: SigFloat to add or subtract from this object.
            ans: Answer of float arithmetic of the two numbers.
        Return:
            A new SigFloat object of the sum or difference.
        """
        # Choose precision to use in calculation
        if (both_exact:=self._exact and other._exact):
            precision = None
        elif self._exact:
            precision = other._sig_figs
        elif other._exact:
            precision = self._sig_figs
        else:
            precision = SigFloat._round_precision(self._precision, other._precision)

        # Round to correct precision
        temp_str = str(ans) if both_exact else str(round(ans, precision))

        # Remove trailing decimal python adds
        if precision is not None and precision <= 0:
            temp_str = temp_str[:-2]

        # Create new SigFloat object of the resultant
        temp = SigFloat(temp_str, units=self._units, exact=both_exact)
        temp._float = ans
        return temp

    def _prod_quotient_calc(self, other, ans: float, opp: str):
        """
        Given an multiplication or division calculation, determines the result
        with proper sig figs.

        Args:
            other: SigFloat to multiply or divide from this object.
            ans: Answer of float arithmetic of the two numbers.
        Return:
            A new SigFloat object of the product or quotient.
        """
        # Create new units
        if opp == "*":
            new_units = {
                unit: self._units.get(unit, 0) + other._units.get(unit, 0)
                for unit in chain(self._units, other._units)
            }
        else:
            new_units = {
                unit: self._units.get(unit, 0) - other._units.get(unit, 0)
                for unit in chain(self._units, other._units)
            }

        # Choose sig figs to use 
        if self._exact and other._exact:
            figs = None
        elif self._exact:
            figs = other._sig_figs
        elif other._exact:
            figs = self._sig_figs
        else:
            figs = min(self._sig_figs, other._sig_figs)
        
        # Create new SigFloat object of the resultant
        if figs is None:
            temp = SigFloat(str(ans), units=new_units, exact=True)
            temp._float = ans
        else:
            # Helper function which rounds a number to a certain number of sig figs.
            temp = SigFloat.round_sig(ans, figs)
            temp._units = new_units

        temp._clear_units()

        return temp

    @staticmethod
    def _digits(num: str) -> int:
        """
        Helper function that counts the number of valid digits in a string
        representation of a number

        Args:
            num: The number to count the digits of.

        Return:
            The number of digits in `num`.
        """
        return len(num) - num.count(".") - num.count("-")

    @staticmethod
    def _suppress_sci(x: str, sig_figs: int) -> str:
        """
        Format a string representation of a number with scientific notation suppressed.

        Args:
            x: The value to be formatted.
            sig_figs: The number of sig_figs `x` has.

        Returns:
          A formatted string representation of `x` in standard notation.
        """
        x.replace("E", "e") # If e is capitalized, replace it with lower case
        coef, exp = x.split("e")  # Split coefficient and exponent on e character
        exp = int(exp)

        # Precision for string formatter
        prec = (
            sig_figs + abs(exp) - 1
            if exp < 0
            else sig_figs - exp - 1 if exp < sig_figs else 0
        )

        # Format x as a string without scientific notation
        str_num = "{num:.{precision}f}".format(num=float(x), precision=prec)

        if coef[-1] == "0":
            if exp >= sig_figs:
                # Insert `O` as  placeholder for over-lined zero ("\u03050")
                # because over-lined zero is two characters and makes the computations harder later
                str_num = str_num[: sig_figs - 1] + "O" + str_num[sig_figs:]
            elif  exp + 1 == sig_figs:
                str_num += "."
        
        return str_num
    
    @staticmethod
    def _round_precision(x: int, y: int) -> int:
        """
        Given two place values, helper function determines which to round to.
        Uses the place convention defined in precision()
        Number:      138828.9823
        Place:     -(543210)1234

        Args:
            x, y: Precisions

        Return:
            The precision that takes precedence in an operation
        """
        if x <= 0 and y <= 0:  # Rounding with two whole numbers
            return -max(abs(x), abs(y))
        else:  # Rounding with a decimal and a whole number, or two decimals
            return min(x, y)
