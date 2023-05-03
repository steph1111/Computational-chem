"""
Module comment
"""
__author__ = "Stephanie L'Heureux"

# from sig_float import round_sig
import sys
sys.path.insert(0, "/Users/stephanie/Documents/PERCISE/sig_float")
import sig_float

def generate_sig():

  return sig_float("9888")

if __name__ == "__main__":
  print(generate_sig())