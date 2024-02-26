print("Welcome to the tip Calculator!")
total = float(input("Enter the total amount of the bill: "))
tip = int(input("What % tip would you like to give [10,12,15]: "))
tot_people = int(input("Enter the total number of people to split the bill: "))
amt_per_head = (total // tip * 100)//tot_people

print(f"Each person should pay:{amt_per_head}")