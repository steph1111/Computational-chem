import random
import math

# set number of tests to generate
num_tests = 100

# list of arithmetic operators
ops = ["+", "-", "*", "/"]

# generate sig fig count tests
print("Sig fig count tests:")
for i in range(num_tests):
    num = round(random.uniform(0.0001, 500), random.randint(0, 4))
    sig_figs = int(math.log10(abs(num))) + 1
    print(str(num))

# generate addition and subtraction tests
print("\nAddition and subtraction tests:")
for i in range(num_tests):
    num1 = round(random.uniform(-1000, 1000), random.randint(0, 4))
    num2 = round(random.uniform(-1000, 1000), random.randint(0, 4))
    op = random.choice(ops[:2])
    print(str(num1) + " " + op + " " + str(num2) + " = " + str(eval(str(num1) + op + str(num2))))

# generate multiplication and division tests
print("\nMultiplication and division tests:")
for i in range(num_tests):
    num1 = round(random.uniform(-1000, 1000), random.randint(0, 4))
    num2 = round(random.uniform(-1000, 1000), random.randint(0, 4))
    op = random.choice(ops[2:])
    print(str(num1) + " " + op + " " + str(num2) + " = " + str(eval(str(num1) + op + str(num2))))


# generate mixed operation tests
print("\nMixed operation tests:")
for i in range(num_tests):
    num1 = round(random.uniform(-1000, 1000), random.randint(0, 4))
    num2 = round(random.uniform(-1000, 1000), random.randint(0, 4))
    num3 = round(random.uniform(-1000, 1000), random.randint(0, 4))
    op1 = random.choice(ops)
    op2 = random.choice(ops)
    op3 = random.choice(ops[2:])
    expr = str(num1) + " " + op1 + " " + str(num2) + " " + op2 + " " + str(num3) + " " + op3 + " " + str(random.choice([10**-6, 10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3, 10**4]))
    try:
        result = round(eval(expr), random.randint(0, 4))
    except ZeroDivisionError:
        continue
    print(expr + " = " + str(result))
