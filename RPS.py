# make a Rock Paper Scissors game

from click import prompt
import random
import os
user = ''
space = '##########################'
clear = lambda: os.system('clear')
while user != 'q':
    prompt = "Choose your weapon!"
    prompt += "\nor press 'q' to quite"
    prompt += "\n1) Rock"
    prompt += "\n2) Paper"
    prompt += "\n3) Scissors"
    prompt += "\n:"

    user = input(prompt)
    computer = random.randint(1, 3)


    def shoot(player, cpu):
    
        
        weapons = {
            "1" : "Rock",
            "2" : "Paper",
            "3" : "Scissors"
            }
        player = int(player)

        if player == cpu:
            clear()
            print(space)
            print("User chose: ", weapons[str(player)])
            print("Computer chose: ", weapons[str(cpu)])
            print("Draw!")
            print(space)
        elif player == cpu + 1 or player == cpu - 2:
            clear()
            print(space)
            print("User chose: ", weapons[str(player)])
            print("Computer chose: ", weapons[str(cpu)])
            print("YOU WIN!!!!")
            print(space)

        else:
            clear()
            print(space)
            print("User chose: ", weapons[str(player)])
            print("Computer chose: ", weapons[str(cpu)])
            print("You suck!")
            print(space)

    if user == 'q':
        clear()
        print("You quit.")
        break
    
    else:

        shoot(user, computer)
