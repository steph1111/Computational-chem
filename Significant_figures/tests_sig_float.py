from sig_float import sig_float

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
print(f"11) {num1} - {num2} = {num1 - num2}")

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

print(RESET)