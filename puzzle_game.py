#Guess a number
from random import randint

def puzzle_game():
    my_rand = randint(1,100)
    print "**************Guess A Number(1-100)**************"
    for i in range(0,5):
        usr_in = int(input("Guess a number of your choice"))
        if(usr_in == my_rand):
            print("You won the game!!")
            break;
        elif(i == 4):
            print("Sorry you lost the game. Actual number is:",my_rand)
            break;
        elif(usr_in > my_rand):
            print("Your guess is greater than the actual value, chances left: ",(4-i))
        elif(usr_in < my_rand):
            print("Your guess is less than the actual value, chances left: ",(4-i))
