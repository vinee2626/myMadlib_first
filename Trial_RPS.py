import random

round = 6

x = ['ROCK', 'PAPER', 'SCISSOR']

while(round != 1):
    y = input("THROW!!!!: ")
    user = y.upper()
    comp = random.choice(x)
    print("COMPUTER: " + comp)
    round = round - 1

    if (comp == user):
        print("IT IS A TIE!!!!, BETTER LUCK NEXT TIME DARLING in round " + str(round))
    elif (user == 'ROCK' and comp == 'SCISSOR'):
        print('YOU WON in round!!! ' + str(round))
    elif (user == 'ROCK' and comp == 'PAPER'):
        print('YOU LOST in round!! ' + str(round))
    elif (user == 'PAPER' and comp == 'ROCK'):
        print('YOU WON in round!! '+str(round))
    elif (user == 'PAPER' and comp == 'SCISSOR'):
        print('YOU LOST!! in round ' + str(round))
    elif (user == 'SCISSOR' and comp == 'ROCK'):
        print('YOU LOST!! in round ' + str(round))
    elif (user == 'SCISSOR' and comp == 'PAPER'):
        print('YOU WON!! in round '+str(round))
    else:
        print("invalid")
