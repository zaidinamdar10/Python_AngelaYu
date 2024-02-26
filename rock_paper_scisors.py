import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
rps = [""" 
    _______
---|   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
    ________
---|    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---|   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]                                                    #
option = int(input("Choose your option: "))
if option == 0:
    print(rps[0])
elif option == 1:
    print(rps[1])
elif option== 2:
    print(rps[2])
else:
    print("Invalid Input")

print("Computer Chooses:")
comp = len(rps)
comp_ch = random.randint(0,comp-1)
if comp_ch == 0:
    print(rps[0])
elif comp_ch == 1:
    print(rps[1])
elif option >= 3:
    print("Invalid IP by user please re-try ")
else:
    print(rps[2])

print("Result:")

if option == comp_ch:
    print("draw")
elif option == 0 and comp_ch == 1:
    print("You Loose")
elif option == 0 and comp_ch == 2:
    print("You Win")
elif option == 1 and comp_ch == 0:
    print("You Win")
elif option == 1 and comp_ch == 2:
    print("You Loose")
elif option == 2 and comp_ch == 0:
    print("You Loose")
elif option == 2 and comp_ch == 1:
    print("You Win")