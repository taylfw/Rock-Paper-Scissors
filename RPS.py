# make a Rock Paper Scissors game

from click import prompt
import random
import os
import time
import emoji
user = ''
space = '##########################'
#the clear variable works on linux systems only (wrote this on ubuntu)
#for windows users, just uncomment the next line & comment out line 13         
#clear = lambda: os.system(‘cls’) 
clear = lambda: os.system('clear')
score = 0
cpuScore = 0

while user != 'q':
    
    prompt = "Choose your weapon!"
    prompt += "\nor press 'q' to quit"
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

        clear()
        print("Rock!", emoji.emojize(":rock:", language='alias'))
        time.sleep(0.70)
        clear()
        print("Paper!", emoji.emojize(":scroll:", language='alias'))
        time.sleep(0.70)
        clear()
        print("Scissors!", emoji.emojize(":scissors:", language='alias'))
        time.sleep(0.70)
        clear()
        print("Shoot!")
        time.sleep(0.70)

        if player == cpu:
            clear()
            print(space)
            print(emoji.emojize(":person:", language='alias')+" chose: ", weapons[str(player)])
            print( emoji.emojize(":robot:", language='alias')+" chose: ", weapons[str(cpu)])
            print("Draw!")
            print(space)

        elif player == cpu + 1 or player == cpu - 2:
            clear()
            print(space)
            print(emoji.emojize(":person:", language='alias')+" chose: ", weapons[str(player)])
            print(emoji.emojize(":robot:", language='alias')+" chose: ", weapons[str(cpu)])
            print("YOU WIN!!!!")
            print(space)
            score += 1
            return score

        else:
            clear()
            print(space)
            print(emoji.emojize(":person:", language='alias')+" chose: ", weapons[str(player)])
            print(emoji.emojize(":robot:", language='alias')+" chose: ", weapons[str(cpu)])
            print("You lose!")
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
            print("You beat the computer!!!"+
            "\n"+emoji.emojize(":fireworks:", language='alias')
            )
            print(space)

        elif score < cpuScore:

            print(space)
            print(emoji.emojize(":robot:", language='alias')+" Computer wins..."+
            "\n"+emoji.emojize(":person_facepalming:", language='alias')+" You Lose!")
            
            print(space)
            
        else:

            print(space)
            print("Tie Game.")
            print(space)

        break

    elif not (user == '1' or user == '2' or user == '3'):

        print(space)
        print(user + " is not a valid choice")
        print(space)

    else:

        shoot(user, computer)
