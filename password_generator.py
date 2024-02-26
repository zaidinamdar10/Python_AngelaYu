import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
l = int(input("How many letters would you like in your password?"))
n = int(input("How many symbols would like?"))
s = int(input("How many numbers would like?"))

password = ""
for char in range(0,l+1):
    password += random.choice(letters)
for char in range(0,n+1):
    password += random.choice(numbers)
for char in range(0,s+1):
    password += random.choice(symbols)

print(password)
my_string = password
my_list = [char for char in my_string]
random.shuffle(my_list)
print(my_list)

up_pass = ""
for i in my_list:
    up_pass += i
print(up_pass)

