fn = input("First Name: ")
sn = input("Second Name: ")
print("The Love Calculator is calculating your score...")
cn = fn + sn
low_case = cn.lower()

T = low_case.count("t")
R = low_case.count("r")
U = low_case.count("u")
E = low_case.count("e")
TRUE = T + R + U + E

L = low_case.count("l")
O = low_case.count("o")
V = low_case.count("v")
E = low_case.count("e")
LOVE = L + O + V + E

calc = str(TRUE) + str(LOVE)
if int(calc) < 10 or int(calc) > 90:
    print(f"Your score is {calc}, you go together like coke and mentos.")
elif int(calc) >= 40 and int(calc) <= 50:
    print(f"Your score is {calc}, you are alright together.")
else:
    print(f"Your score is {calc}.")

