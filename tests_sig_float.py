from precise import SigFloat
# from SigFloat import sig_const
# import SigFloat

print("Sig fig count tests:")
num = SigFloat("00122.9800")
print(f"1) 00122.9800 -> {num.sig_figs()}")

num = SigFloat("12000")
print(f"2) 12000 -> {num.sig_figs()}")

num = SigFloat("12000.")
print(f"3) 12000. -> {num.sig_figs()}")

num = SigFloat("0012000.")
print(f"4) 0012000. -> {num.sig_figs()}")

num = SigFloat("2536.000")
print(f"5) 2536.000 -> {num.sig_figs()}")

num = SigFloat("1.000")
print(f"6) 1.000 -> {num.sig_figs()}")

num = SigFloat("0.00033")
print(f"7) 0.00033 -> {num.sig_figs()}")

num = SigFloat("12.09")
print(f"8) 12.09 -> {num.sig_figs()}")

num = SigFloat("-000001")
print(f"9) -000001 -> {num.sig_figs()}")

num = SigFloat("-10.")
print(f"10) -10. -> {num.sig_figs()}")

num = SigFloat("0.2000")
print(f"11) 0.2000 -> {num.sig_figs()}")

print("\nAddition and subtraction tests:")
num1 = SigFloat("13.0198")
num2 = SigFloat("1.2")
print(f"1) {num1} + {num2} = {num1 + num2}")

num1 = SigFloat("94")
num2 = SigFloat("15")
num3 = SigFloat("182.113")
print(f"2) {num1} + {num2} + {num3} = {num1 + num2 + num3}")

num1 = SigFloat("59.21")
num2 = SigFloat("18.8722")
print(f"3) {num1} - {num2} = {num1 - num2}")

num1 = SigFloat("8.679")
num2 = SigFloat("0.3")
num3 = SigFloat("5.88")
print(f"4) {num1} + {num2} + {num3} = {num1 + num2 + num3}")

num1 = SigFloat("2.36")
num2 = SigFloat("5.4")
print(f"5) {num1} + {num2} = {num1 + num2}")

num1 = SigFloat("7.2361")
num2 = SigFloat("8.42")
print(f"6) {num1} + {num2} = {num1 + num2}")

num1 = SigFloat("420.")
num2 = SigFloat("3.51")
print(f"7) {num1} + {num2} = {num1 + num2}")

num1 = SigFloat("500")
num2 = SigFloat("1.365")
print(f"8) {num1} + {num2} = {num1 + num2}")

num1 = SigFloat("-420.")
num2 = SigFloat("3.51")
print(f"9) {num1} + {num2} = {num1 + num2}")

num1 = SigFloat("-50")
num2 = SigFloat("-3.2")
print(f"10) {num1} + {num2} = {num1 + num2}")

num1 = SigFloat("300")
num2 = SigFloat("47.465")
print(f"11) {num1} - {num2} = {num1 - num2}")

num1 = SigFloat("0.0007")
num2 = SigFloat("0.775")
print(f"12) {num1} - {num2} = {num1 - num2}")

print("\nMultiplication and division tests:")
num1 = SigFloat("6")
num2 = SigFloat("0.30")
print(f"1) {num1} * {num2} = {num1 * num2}")

num1 = SigFloat("0.03")
num2 = SigFloat("7")
num3 = SigFloat("210")
print(f"2) {num1} * {num2} * {num3 } = {num1 * num2 * num3}")

num1 = SigFloat("11.6")
num2 = SigFloat("6.24")
print(f"3) {num1} * {num2} = {num1 * num2}")

num1 = SigFloat("0.004")
num2 = SigFloat("5280")
print(f"4) {num1} * {num2} = {num1 * num2}")

num1 = SigFloat("500.55")
num2 = SigFloat("5.11")
print(f"5) {num1} / {num2} = {num1 / num2}")

num1 = SigFloat("1000")
num2 = SigFloat("8.2")
print(f"6) {num1} / {num2} = {num1 / num2}")

num1 = SigFloat("51.6")
num2 = SigFloat("31.4")
print(f"7) {num1} * {num2} = {num1 * num2}")

num1 = SigFloat("8088")
num2 = SigFloat("0.4")
print(f"8) {num1} * {num2} = {num1 * num2}")

num1 = SigFloat("204.17")
num2 = SigFloat("3.2")
print(f"9) {num1} / {num2} = {num1 / num2}")

num1 = SigFloat("8000")
num2 = SigFloat("9.7")
print(f"10) {num1} / {num2} = {num1 / num2}")

num1 = SigFloat("10.0")
num2 = SigFloat("0.200")
print(f"11) {num1} * {num2} = {num1 * num2}")

num1 = SigFloat("1", exact=True)
num2 = SigFloat("3", exact=True)
print(f"12) {num1} / {num2} = {num1 / num2}")

print("\nMixed operations tests:")
num1 = SigFloat("15.803")
num2 = SigFloat("4.76")
num3 = SigFloat("9.3")
print(f"1) ({num1} - {num2}) / {num3 } = {(num1 - num2) / num3}")

num1 = SigFloat("0.91")
num2 = SigFloat("1.2")
num3 = SigFloat("8.4")
num4 = SigFloat("3.700")
print(f"2) ({num1} + {num2} + {num3}) / {num4} = {(num1 + num2 + num3) / num4}")

num1 = SigFloat("2.8")
num2 = SigFloat("4.532")
num3 = SigFloat("12.690")
print(f"3) ({num1} * {num2}) + {num3} = {num1 * num2 + num3}")

num1 = SigFloat("55")
num2 = SigFloat("55")
num3 = SigFloat("1.0")
num4 = SigFloat("1.0")
print(f"4) {num1} * {num2} * {num3} + {num4} = {num1 * num2 * num3 }") # Should be overlined??

print("\nRounding tests:")
print(f"1) round_sig(8712082, 2) -> {SigFloat.round_sig(8712082, 2)}")
print(f"2) round_sig(8000, 2) -> {SigFloat.round_sig(8000, 2)}")
print(f"3) round_sig(980, 2) -> {SigFloat.round_sig(980, 2)}")
print(f"4) round_sig(120000, 6) -> {SigFloat.round_sig(120000, 6)}")
num1 = SigFloat("120000", {"kg":1, "m":1, "s":-2})
print('5) round_sig(("120000", {"kg":1, "m":1, "s":-2}), 4) ->' , SigFloat.round_sig(num1, 4))

print("\nUnits tests:")
num2 = SigFloat("2.8", {"kg":2, "m":5})
num3 = SigFloat("2.2", {"kg":2, "m":1})
print(f"1) ({num2}) / ({num3}) = {num2 / num3}")

V1 = SigFloat("2.00", {"L":1})
P1 = SigFloat("752.0", {"mmHg":1})
T1 = SigFloat("293", {"K":1})
P2 = SigFloat("2943", {"mmHg":1})
T2 = SigFloat("273", {"K":1})
V2 = (T2 * P1 * V1) / (P2 * T1)
print(f"2) V2 = {V2}")

F1 = SigFloat("28.4", {"kg":1, "m":1, "s":-2})
g = SigFloat("9.80", {"m":1, "s":-2})
F2 = SigFloat("17.0", {"kg":1, "m":1, "s":-2})
density_fluid = SigFloat("1000.", {"kg":1, "m":-3})

density_obj = (F1 / g) / ((F1 - F2)/(density_fluid * g))
print(f"3) density_object: {density_obj}")

R = SigFloat("0.08206", {"L":1, "atm":1, "mol":-1, "K":-1}, exact=True)
print(f"4) R: {R}")

Ts = SigFloat("20.", {"kg":1, "m":1, "s":-2})
L = SigFloat("2.0", {"m":1})
delta_x = SigFloat("2.0", {"m":1})
delta_t = SigFloat("0.05", {"s":1})
m = (Ts * L) / ((delta_x / delta_t) * (delta_x / delta_t))
print(f"5) mass (m): {m}")

print("\nLaTeX tests:")
print(f"1) density_obj in format=1: {density_obj.latex(format=1)}")
print(f"2) density_obj in format=2: {density_obj.latex(format=2)}")
print(f"3) R in format=1: {R.latex(format=1)}")

print(f"4) R in format=2: {R.latex(format=2)}")
print(f"5) R in format=3: {R.latex(format=3)}")

print(f"6) V2 in format=1: {V2.latex(format=1)}")
print(f"7) V2 in format=2: {V2.latex(format=2)}")

f = SigFloat("300.0", {"s":-1})
f = SigFloat.round_sig(f, 4)
print(f"8) f in format=2: {f.latex(format=2)}")
print(f"9) f in format=3: {f.latex(format=1)}")

print("\nScientific tests: ")
print(f"1) {f.latex(sci=True)}")
print(f"2) {num1.latex(sci=True)}")
d = SigFloat("123.000", {"m":1})
print(f"3) {d.latex(sci=True)}")

# # C = SigFloat("3.00e+8", {"m":1, "s":-1})
# # print(C.latex(sci=False))
# # print(C.latex(sci=True))