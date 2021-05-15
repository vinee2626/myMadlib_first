import random
# create a var to store the random no.
x = random.randint(1, 10)
# set t =5 for 5 trials
t = 5

# inititate a while loop until x =0 and a and y are not equal
while(t > 0):
    y = int(input("Guess a no.: "))
    t -= 1
    if (y == x):
        print("YOU WON")
        break
    else:
        print("YOU LOOSE")
    if (x > y):
        print("TOO LOW")
    elif (x < y):
        print("TOO HIGH")

# create a var y to store the input from user
# decrement the sentry by 1 foreah input
# if they are equal then print and if not- print
# if the input is too high or too low then tell the user about it to improve their guess
