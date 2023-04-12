from sig_float import *

if __name__ == "__main__":
  num1 = sig_float("1.457")
  num2 = sig_float("83.2")
  print(f"1. {num1} + {num2} = {num1 + num2}")

  num1 = sig_float("0.0367")
  num2 = sig_float("0.004322")
  print(f"2. {num1} - {num2} = {num1 - num2}")

  # Not working
  num1 = sig_float("30000.")
  num2 = sig_float("35")
  num3 = sig_float("13")
  print(f"2. {num1} + {num2} - {num3} = {num1 + num2 - num3}")
