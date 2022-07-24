# make a Rock Paper Scissors game

from click import prompt
import random
import os
user = ''
space = '##########################'
#the clear variable works on linux systems only (wrote this on ubuntu)
clear = lambda: os.system('clear')
score = 0
cpuScore = 0

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
        global score
        global cpuScore
        
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
            score += 1
            return score

        else:
            clear()
            print(space)
            print("User chose: ", weapons[str(player)])
            print("Computer chose: ", weapons[str(cpu)])
            print("You suck!")
            print(space)
            cpuScore += 1
            return cpuScore

    if user == 'q':
        clear()
        print("You quit.")
        print("Your score is ", score)
        print("The computer's score is ", cpuScore)
        if score > cpuScore:
            print(space)
            print("You beat the computer!!!")
            print(space)
        else:
            print(space)
            print("The computer wins and told me to tell you; \n110100010101100010110010101")
            print(space)
        break

    elif not (user == '1' or user == '2' or user == '3'):
        print(space)
        print(user + " is not a valid choice")
        print(space)
    else:
        shoot(user, computer)
