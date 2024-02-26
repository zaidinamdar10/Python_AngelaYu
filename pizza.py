print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
if size == 'S':
    print("Pay $15 ")
    Bill = 15
elif size == 'M':
    print("Pay $20 ")
    Bill = 20
elif size == 'L':
    print("Pay $25")
    Bill = 25
add_pepperoni = input("Do you want pepperoni: [Y/N]: ")
if add_pepperoni == 'Y':
    if size == 'S':
        Bill += 2
        print("The total bill is:", Bill)
    elif size != 'S':
        Bill += 3
        print("The total bill is:", Bill)
extra_cheese = input("Do you want Extra Cheese: [Y/N]:")
if extra_cheese == 'Y':
    Bill += 1
    print("The total bill is:", Bill)
else:
    print("The total bill is:", Bill)