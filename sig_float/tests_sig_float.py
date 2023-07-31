from sig_float import sig_float
from sig_float import round_sig

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

print("Sig fig count tests:" + GREEN)
num = sig_float("00122.9800")
print(f"1) 00122.9800 -> {num.sig_figs()}")

num = sig_float("12000")
print(f"2) 12000 -> {num.sig_figs()}")

num = sig_float("12000.")
print(f"3) 12000. -> {num.sig_figs()}")

num = sig_float("0012000.")
print(f"4) 0012000. -> {num.sig_figs()}")

num = sig_float("2536.000")
print(f"5) 2536.000 -> {num.sig_figs()}")

num = sig_float("1.000")
print(f"6) 1.000 -> {num.sig_figs()}")

num = sig_float("0.00033")
print(f"7) 0.00033 -> {num.sig_figs()}")

num = sig_float("12.09")
print(f"8) 12.09 -> {num.sig_figs()}")

num = sig_float("-000001")
print(f"9) -000001 -> {num.sig_figs()}")

num = sig_float("-10.")
print(f"10) -10. -> {num.sig_figs()}")

num = sig_float("0.2000")
print(f"11) 0.2000 -> {num.sig_figs()}")

print(RESET + "\nAddition and subtraction tests:" + GREEN)
num1 = sig_float("13.0198")
num2 = sig_float("1.2")
print(f"1) {num1} + {num2} = {num1 + num2}")

num1 = sig_float("94")
num2 = sig_float("15")
num3 = sig_float("182.113")
print(f"2) {num1} + {num2} + {num3} = {num1 + num2 + num3}")

num1 = sig_float("59.21")
num2 = sig_float("18.8722")
print(f"3) {num1} - {num2} = {num1 - num2}")

num1 = sig_float("8.679")
num2 = sig_float("0.3")
num3 = sig_float("5.88")
print(f"4) {num1} + {num2} + {num3} = {num1 + num2 + num3}")

num1 = sig_float("2.36")
num2 = sig_float("5.4")
print(f"5) {num1} + {num2} = {num1 + num2}")

num1 = sig_float("7.2361")
num2 = sig_float("8.42")
print(f"6) {num1} + {num2} = {num1 + num2}")

num1 = sig_float("420.")
num2 = sig_float("3.51")
print(f"7) {num1} + {num2} = {num1 + num2}")

num1 = sig_float("500")
num2 = sig_float("1.365")
print(f"8) {num1} + {num2} = {num1 + num2}")

num1 = sig_float("-420.")
num2 = sig_float("3.51")
print(f"9) {num1} + {num2} = {num1 + num2}")

num1 = sig_float("-50")
num2 = sig_float("-3.2")
print(f"10) {num1} + {num2} = {num1 + num2}")

num1 = sig_float("300")
num2 = sig_float("47.465")
print(f"11) {num1} - {num2} = {num1 - num2}")

num1 = sig_float("0.0007")
num2 = sig_float("0.775")
print(f"12) {num1} - {num2} = {num1 - num2}")

print(RESET + "\nMultiplication and division tests:" + GREEN)
num1 = sig_float("6")
num2 = sig_float("0.30")
print(f"1) {num1} * {num2} = {num1 * num2}")

num1 = sig_float("0.03")
num2 = sig_float("7")
num3 = sig_float("210")
print(f"2) {num1} * {num2} * {num3 } = {num1 * num2 * num3}")

num1 = sig_float("11.6")
num2 = sig_float("6.24")
print(f"3) {num1} * {num2} = {num1 * num2}")

num1 = sig_float("0.004")
num2 = sig_float("5280")
print(f"4) {num1} * {num2} = {num1 * num2}")

num1 = sig_float("500.55")
num2 = sig_float("5.11")
print(f"5) {num1} / {num2} = {num1 / num2}")

num1 = sig_float("1000")
num2 = sig_float("8.2")
print(f"6) {num1} / {num2} = {num1 / num2}")

num1 = sig_float("51.6")
num2 = sig_float("31.4")
print(f"7) {num1} * {num2} = {num1 * num2}")

num1 = sig_float("8088")
num2 = sig_float("0.4")
print(f"8) {num1} * {num2} = {num1 * num2}")

num1 = sig_float("204.17")
num2 = sig_float("3.2")
print(f"9) {num1} / {num2} = {num1 / num2}")

num1 = sig_float("8000")
num2 = sig_float("9.7")
print(f"10) {num1} / {num2} = {num1 / num2}")

num1 = sig_float("10.0")
num2 = sig_float("0.200")
print(f"11) {num1} * {num2} = {num1 * num2}")

num1 = sig_float("1", exact=True)
num2 = sig_float("3", exact=True)
print(f"12) {num1} / {num2} = {num1 / num2}")

print(RESET + "\nMixed operations tests:" + GREEN)
num1 = sig_float("15.803")
num2 = sig_float("4.76")
num3 = sig_float("9.3")
print(f"1) ({num1} - {num2}) / {num3 } = {(num1 - num2) / num3}")

num1 = sig_float("0.91")
num2 = sig_float("1.2")
num3 = sig_float("8.4")
num4 = sig_float("3.700")
print(f"2) ({num1} + {num2} + {num3}) / {num4} = {(num1 + num2 + num3) / num4}")

num1 = sig_float("2.8")
num2 = sig_float("4.532")
num3 = sig_float("12.690")
print(f"3) ({num1} * {num2}) + {num3} = {num1 * num2 + num3}")

num1 = sig_float("55")
num2 = sig_float("55")
num3 = sig_float("1.0")
num4 = sig_float("1.0")
print(f"4) {num1} * {num2} * {num3} + {num4} = {num1 * num2 * num3 }") # Should be overlined??

print(RESET + "\nRounding tests:" + GREEN)
print(f"1) round_sig(8712082, 2) -> {round_sig(8712082, 2)}")
print(f"2) round_sig(8000, 2) -> {round_sig(8000, 2)}")
print(f"3) round_sig(980, 2) -> {round_sig(980, 2)}")
print(f"4) round_sig(120000, 6) -> {round_sig(120000, 6)}")
num1 = sig_float("120000", {"kg":1, "m":1, "s":-2})
print('5) round_sig(("120000", {"kg":1, "m":1, "s":-2}), 4) ->' , round_sig(num1, 4))

print(RESET + "\nUnits tests:" + GREEN)
num2 = sig_float("2.8", {"kg":2, "m":5})
num3 = sig_float("2.2", {"kg":2, "m":1})
print(f"1) ({num2}) / ({num3}) = {num2 / num3}")

V1 = sig_float("2.00", {"L":1})
P1 = sig_float("752.0", {"mmHg":1})
T1 = sig_float("293", {"K":1})
P2 = sig_float("2943", {"mmHg":1})
T2 = sig_float("273", {"K":1})
V2 = (T2 * P1 * V1) / (P2 * T1)
print(f"2) V2 = {V2}")

F1 = sig_float("28.4", {"kg":1, "m":1, "s":-2})
g = sig_float("9.80", {"m":1, "s":-2})
F2 = sig_float("17.0", {"kg":1, "m":1, "s":-2})
density_fluid = sig_float("1000.", {"kg":1, "m":-3})

density_obj = (F1 / g) / ((F1 - F2)/(density_fluid * g))
print(f"3) density_object: {density_obj}")

R = sig_float("0.08206", {"L":1, "atm":1, "mol":-1, "K":-1}, exact=True)
print(f"4) R: {R}")

Ts = sig_float("20.", {"kg":1, "m":1, "s":-2})
L = sig_float("2.0", {"m":1})
delta_x = sig_float("2.0", {"m":1})
delta_t = sig_float("0.05", {"s":1})
m = (Ts * L) / ((delta_x / delta_t) * (delta_x / delta_t))
print(f"5) mass (m): {m}")

print(RESET + "\nLaTeX tests:" + GREEN)
print(f"1) density_obj in format=1: {density_obj.latex(format=1)}")
print(f"2) density_obj in format=2: {density_obj.latex(format=2)}")
print(f"3) R in format=1: {R.latex(format=1)}")

print(f"4) R in format=2: {R.latex(format=2)}")
print(f"5) R in format=3: {R.latex(format=3)}")

print(f"6) V2 in format=1: {V2.latex(format=1)}")
print(f"7) V2 in format=2: {V2.latex(format=2)}")

f = sig_float("300.0", {"s":-1})
f = round_sig(f, 4)
print(f"8) f in format=2: {f.latex(format=2)}")
print(f"9) f in format=3: {f.latex(format=1)}")

print(RESET + "\nScientific tests: " + GREEN)
print(f"1) {f.latex(sci=True)}")
print(f"2) {num1.latex(sci=True)}")
d = sig_float("123.000", {"m":1})
print(f"3) {d.latex(sci=True)}")

print(RESET)
