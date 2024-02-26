n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))

for number in range (n1,(n2+1)):
    if number >1:
        for i in range (2,number):
            if (number % i) == 0:
                break
        else:
            print("THE NUMBER IS PRIME: ",number)

