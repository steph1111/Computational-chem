#!/usr/bin/env python3
import textwrap, random
from sigfig import round

def generate_choice(base, exponent, variation=2, exp_variation=4):
	mantissa_variation = round(base + random.uniform(-variation, variation), sigfigs=3)
	exponent_variation = exponent + random.randint(-exp_variation, exp_variation)
	return f"${mantissa_variation} \\times 10^{{{exponent_variation}}}$"

random.seed()
for question_number in range(1, 51):
	mantissa = random.uniform(1, 14)
	pH_value = round(mantissa, sigfigs=3)
	H3O_calculation = pow(10, -pH_value)
	scientific_notation = round(H3O_calculation, sigfigs=3, notation='sci')
	mantissa_str, exponent_str = str(scientific_notation).split('E')
	correct_answer = f"${mantissa_str} \\times 10^{{{exponent_str}}}$"
	mantissa_float = float(mantissa_str)
	exponent_int = int(exponent_str)
	
	incorrect_answers = [generate_choice(mantissa_float, exponent_int) for _ in range(4)]
	
	print(textwrap.dedent(rf"""
		{question_number}. Calculate the $[\text{{H}}_3\text{{O}}^{{+}}]$ of a solution with pH ${pH_value}$.
		[*] {correct_answer}
		[] {incorrect_answers[0]}
		[] {incorrect_answers[1]}
		[] {incorrect_answers[2]}
		[] {incorrect_answers[3]}
		"""))
	