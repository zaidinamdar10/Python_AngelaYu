line1 = ["⬜️","️⬜","️⬜"]
line2 = ["⬜️","⬜️","️⬜"]
line3 = ["⬜️","⬜️","⬜  "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
letter = input() #take the input from user where u want to hide the tresure
first_letter = letter[0].lower() #make the first letter of the input to lower case to maintain uniformity and comparibility
abc = ["a","b","c"] #new list to compare the letter
comp_1 = abc.index(first_letter) #will print the position of the letter after comparing with the first_letter
numb_2 = int(letter[1])-1  #will check the 2nd letter in the input that is the number/ we are using -1 beacuse if the last digit is 1 then its posi must be 0
map [comp_1][numb_2] = "x"

print(f"{line1}\n{line2}\n{line3}")