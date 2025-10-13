import random as r

attempt = 1
maxattempt = 3

number = input("Please Guess the number from 1 to 100 : ")
guess_numebr = r.randint(1,100)

while True:
    if number == guess_numebr:
        print("You guess the right number YAHOOOO! YOU win")
        break

    if guess_numebr == number:
        print("YAHOOO! You guess the right nuumber ❤️")    
        break
    if maxattempt == attempt:
        print("you hit the limit")
        break
    if guess_numebr > number:
        print("You number is Too high Guess low values")
    else:
        print("You guess number is too low value guess high values")