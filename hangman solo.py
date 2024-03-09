import random
import time

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word = ['messi','neymar','suarez']
rcw = random.choice(word)
print(rcw)
lrcw = len(rcw)
disp = []
lives = 6


for i in range(lrcw):
    disp += '_'
print(disp)


def xyz():
    global lives
    global end_of_game
    for i in rcw:
        print("Guess the letter: ")
        ucl = input()

     #displaying the blank list
        for pos in range(lrcw):
            if ucl == rcw[pos]:
                disp[pos] = ucl

        print(' '.join(disp))

        if ucl not in rcw:
                lives = lives - 1
                print(lives)
                if lives == 0:
                    end_of_game = True
                    print("You loose!!")
                    break

    if "_" not in disp:
        end_of_game = True
        print("you win")
        #print(disp)

end_of_game = False
while end_of_game == False:
    xyz()





