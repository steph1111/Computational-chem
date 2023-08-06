#!/usr/bin/env python3
import textwrap, random
from sigfig import round
from math import log10

random.seed()
for x in range(1, 51, 1):
	a = random.uniform(1, 14)		#mantissa
	
	g = round(a, sigfigs=3)

	calculation = pow(10, -g)
	
	r = round(calculation, sigfigs=3, notation='sci')
	
	qwe = str(r)
	
	m = qwe.split('E')

	rty = "$" + m[0] + "\\times 10^{" + m[1] + "}$"
	
	n = round(float(m[0]) + random.uniform(-2,2), sigfigs=3)
	o = int(m[1]) + random.randint(-4, 4)
	p = "$" + str(n) + "\\times 10^{" + str(o) + "}$"

	q = round(float(m[0]) + random.uniform(-2,2), sigfigs=3)
	r = int(m[1]) + random.randint(-4, 4)
	s = "$" + str(q) + "\\times 10^{" + str(r) + "}$"
	
	t = round(float(m[0]) + random.uniform(-2,2), sigfigs=3)
	u = int(m[1]) + random.randint(-4, 4)
	v = "$" + str(t) + "\\times 10^{" + str(u) + "}$"
	
	w = round(float(m[0]) + random.uniform(-2,2), sigfigs=3)
	z = int(m[1]) + random.randint(-4, 4)
	y = "$" + str(w) + "\\times 10^{" + str(z) + "}$"

	print(textwrap.dedent(rf"""
		{x}. Calculate the $[\text{{H}}_3\text{{O}}^{{+}}]$ of a solution with pH ${g}$.
		[*] {rty}
		[] {p}
		[] {s}
		[] {v}
		[] {y}
		"""))
	