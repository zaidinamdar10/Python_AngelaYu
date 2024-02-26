print("Thank you for choosing Python Pizza Deliveries!")
size = input()
if size == 'S':
    Bill = 15
elif size == 'M':
    Bill = 20
elif size == 'L':
    Bill = 25
add_pepperoni = input("")
if add_pepperoni == 'Y':
    if size == 'S':
        Bill += 2
    elif size != 'S':
        Bill += 3
extra_cheese = input("")
if extra_cheese == 'Y':
    Bill += 1
    print(f"Your final bill is: ${Bill}.")
else:
    print(f"Your final bill is: ${Bill}.")