#!/usr/bin/env python3

def find_sigfigs(number):
	"""Returns the number of significant digits in a number"""
	"""number = repr(float(number))"""
	
	tokens = number.split('.')
	whole_num = tokens[0].rstrip('0')
	
	if len(tokens) > 2:
		raise ValueError('Invalid number "%s" only 1 decimal allowed' % (number))
		
	if len(tokens) == 2:
		decimal_num = tokens[1].rstrip('0')
		return len(whole_num) + len(decimal_num)
	
	return len(whole_num)

import textwrap, random
random.seed()
for x in range(1, 51):
	a = random.uniform(600, 800)	#pressure
	b = random.uniform(20, 40)	#temperature
	c = random.uniform(2, 4)	#number of moles
	
	d = random.uniform(30, 50)	#volume
	e = random.uniform(10, 30)	#temperatue2
	f = random.uniform(90, 120)  #mass
	
	gasconstant = 8.3145
	
	g = "{:.0f}".format(round(a,2))
	h = "{:.1f}".format(round(b,2))
	i = "{:.2f}".format(round(c,2))
	
	j = "{:.1f}".format(round(d,2))
	k = "{:.1f}".format(round(e,2))
	l = "{:.2f}".format(round(f,2))
	
	m = find_sigfigs(g)
	n = find_sigfigs(h)
	o = find_sigfigs(i)
	
	p = min(m,n,o)
	
	kelvin1 = b + 273.15
	kelvin2 = f + 273.15
	mmHg1 = c + 760
	
	calculation = (f)/(((a/760)*(d))/(0.08206*kelvin1))
	calculation2 = (c*b*kelvin1)/(a/kelvin2)
	
	q = f"{calculation:.{p}f}"
	r = q.rstrip('0')
	marginoferror = float(q) * 0.05
	s = "{:.3f}".format(round(marginoferror,3))
	t = s.rstrip('0')
	
	u = f"{calculation2:.{p}f}"
	v = q.rstrip('0')
	marginoferror = float(u) * 0.01
	w = "{:.3f}".format(round(marginoferror,3))
	y = w.rstrip('0')
	
	z = o = "{:.1f}".format(round(mmHg1,3))
	
	print(textwrap.dedent(rf"""
		{x}. A gas with a mass of ${l}\text{{g}}$ occupies ${j}\text{{L}}$ at ${g}\text{{mmHg}}$ and ${h}\text{{°C}}$. What is its molecular weight?<br /> <br /> Use $0.08206\cdot\text{{L}}\cdot\text{{atm}}\cdot\text{{K}}^{{-1}}\cdot\text{{mol}}^{{-1}}$ for your gas constant.<br /><br />Express your answer in the correct units, but enter only the numeric portion into Canvas. <br /> <br /> **Be sure to use correct sig. figs!**
		= {r} +- {t}
		"""))