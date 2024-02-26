print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
l_r = input("left or right?")
if l_r == "left":
    s_w = input("swim or wait?")
    if s_w == "wait":
        door = input("Which door?(red,blue,yellow)")
        if door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif door == "yellow":
            print("you win!!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")