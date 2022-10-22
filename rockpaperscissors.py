#Name: Aditya Pisharoty
#Assignment Name: Rock Paper Scissors
#Date: January 22nd 2021
#Description: Player plays rock paper scissors against computer.
import math
import random
username = input("Enter a username: ")
#Challenge 1: Cool user interface with images of rock, paper and scissors
print("Hello {}!".format(username))
#welcoming player to the game
print("")
print("                WELCOME TO ADITYA'S:                   ")
print("                                         /\         ")
print("                                         ||         ")
print("      ooooooo                            ||         ")
print("     ooooooooo       __________          ||         ")
print("    ooooooooooo     |_|________|         ||         ")
print("    ooooooooooo     |o|________|        //\\\       ")
print("    ooooooooooo     |_|________|       //  \\\      ")
print("     ooooooooo      |o|________|      //    \\\     ")
print("      ooooooo       |_|________|     oo      oo     ")
print("                    |o|________|    o  o    o  o    ")
print("                    |_|________|    o  o    o  o    ")
print("                                     oo      oo     ")
print("")
print("        ROCK           PAPER          SCISSORS!      ")
#large image of rock, paper, and scissors
print("")
input("Press ENTER to continue. ")
print("")
#Challenge 2: Multiple different gamemodes
print("There are four gamemodes to choose from:")
print("(1) Showdown:")
print("One round.")
print("(2) First to X Points")
print("Player will play against computer until either one reaches X points.")
print("Both gain one point for every win.")
print("Player will decide value of X.")
print("(3) Unlimited Play:")
print("Player can play against computer unlimited times.")
print("(4) Best of 3")
print("Player will play against computer 3 times.")
print ("")
gamemode = int(input("Please choose a gamemode: "))
if gamemode == 1:
#showdown: only one game
    print("")
    print('You chose "Showdown"!')
    computer = random.randint(1, 3)
    #1 is rock, 2 is paper, 3 is scissors
    print("For reference: 1 = Rock, 2 = Paper and 3 = Scissors.")
    print(
        "To choose an option, please enter the option's corresponding number.")
    print("")
    player = int(input("Rock, Paper, Scissors? "))
    if player == computer:
        if player == 1:
            print("You threw rock!")
#display what player threw
        elif player == 2:
            print("You threw paper!")
        elif player == 3:
            print("You threw scissors!")
        if computer == 1:
            print("Computer threw rock!")
#display what computer threw
        elif computer == 2:
            print("Computer threw paper!")
        elif computer == 3:
            print("Computer threw scissors!")
        print("It's a tie!")
        print("Thanks for playing!")
    elif player == 1:
        print("You threw rock!")
        if computer == 2:
            print("Computer threw paper!")
            print("You lose!")
            print("Thanks for playing!")
        elif computer == 3:
            print("Computer threw scissors!")
            print("You win!")
            print("Thanks for playing!")
    elif player == 2:
        print("You threw paper!")
        if computer == 3:
            print("Computer threw scissors!")
            print("You lose!")
            print("Thanks for playing!")
        elif computer == 1:
            print("Computer threw rock!")
            print("You win!")
            print("Thanks for playing!")
    elif player == 3:
        print("You threw scissors!")
        if computer == 1:
            print("Computer threw rock!")
            print("You lose!")
            print("Thanks for playing!")
        elif computer == 2:
            print("Computer threw paper!")
            print("You win!")
            print("Thanks for playing!")
    else:
        print(
            "You did not enter a valid option. To choose an option, please enter the option's corresponding number."
        )
elif gamemode == 2:
#first to x Points
#player will choose value of X
    print("")
    print('You chose "First to X Points"!')
    maxpoint = int(input("What do you want to set as the X value? "))
    print("You have chosen: First to {} Points!".format(maxpoint))
    print("")
    print("For reference: 1 = Rock, 2 = Paper and 3 = Scissors.")
    print(
        "To choose an option, please enter the option's corresponding number.")
    print("")
#Challenge 3: Keeping a point system
    playerpoints = 0
    computerpoints = 0
#list how many points each side has after each round
    quit = 0
    while quit == 0:
        computer2 = random.randint(1, 3)
        player2 = int(input("Rock, Paper, Scissors? "))
        if player2 == computer2:
            if player2 == 1:
                print("You threw rock!")
#display what player threw
            elif player2 == 2:
                print("You threw paper!")
            elif player2 == 3:
                print("You threw scissors!")
            if computer2 == 1:
                print("Computer threw rock!")
#display what computer threw
            elif computer2 == 2:
                print("Computer threw paper!")
            elif computer2 == 3:
                print("Computer threw scissors!")
            print("It's a tie!")
            print("You: {} points".format(playerpoints))
            print("Computer: {} points".format(computerpoints))
        elif player2 == 1:
            print("You threw rock!")
            if computer2 == 2:
                print("Computer threw paper!")
                print("You lost!")
                computerpoints += 1
                print("You: {} points".format(playerpoints))
                print("Computer: {} points".format(computerpoints))
                if computerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
                if playerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
            if computer2 == 3:
                print("Computer threw scissors!")
                print("You won!")
                playerpoints += 1
                print("You: {} points".format(playerpoints))
                print("Computer: {} points".format(computerpoints))
                if computerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
                if playerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
        elif player2 == 2:
            print("You threw paper!")
            if computer2 == 3:
                print("Computer threw scissors!")
                print("You lost!")
                computerpoints += 1
                print("You: {} points".format(playerpoints))
                print("Computer: {} points".format(computerpoints))
                if computerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
                if playerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
            if computer2 == 1:
                print("Computer threw rock!")
                print("You won!")
                playerpoints += 1
                print("You: {} points".format(playerpoints))
                print("Computer: {} points".format(computerpoints))
                if computerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
                if playerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
        elif player2 == 3:
            print("You threw scissors!")
            if computer2 == 1:
                print("Computer threw rock!")
                print("You lost!")
                computerpoints += 1
                print("You: {} points".format(playerpoints))
                print("Computer: {} points".format(computerpoints))
                if computerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
                if playerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
            if computer2 == 2:
                print("Computer threw paper!")
                print("You won!")
                playerpoints += 1
                print("You: {} points".format(playerpoints))
                print("Computer: {} points".format(computerpoints))
                if computerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
                if playerpoints == maxpoint:
                    print("Thanks for playing!")
                    quit += 1
        else:
            print(
                "You did not enter a valid option. To choose an option, please enter the option's corresponding number."
            )
elif gamemode == 3:
#Unlimited 
    print("")
    print('You chose "Unlimited Play"!')
    print("For reference: 1 = Rock, 2 = Paper and 3 = Scissors.")
    print(
        "To choose an option, please enter the option's corresponding number.")
    print('Type 4 to quit game.')
#adding option to quit the game
    print("")
    quit2 = 0
    while quit2 == 0:
        computer3 = random.randint(1, 3)
        player3 = int(input("Rock, Paper, Scissors? "))
        if player3 == 4:
            print("Thanks for playing!")
            quit2 += 1
        elif player3 == computer3:
            if player3 == 1:
                print("You threw rock!")
#display what player threw
            elif player3 == 2:
                print("You threw paper!")
            elif player3 == 3:
                print("You threw scissors!")
            if computer3 == 1:
                print("Computer threw rock!")
#display what computer threw
            elif computer3 == 2:
                print("Computer threw paper!")
            elif computer3 == 3:
                print("Computer threw scissors!")
            print("It's a tie!")
        elif player3 == 1:
            print("You threw rock!")
            if computer3 == 2:
                print("Computer threw paper!")
                print("You lost!")
            if computer3 == 3:
                print("Computer threw scissors!")
                print("You won!")
        elif player3 == 2:
            print("You threw paper!")
            if computer3 == 3:
                print("Computer threw scissors!")
                print("You lost!")
            if computer3 == 1:
                print("Computer threw rock!")
                print("You won!")
        elif player3 == 3:
            print("You threw scissors!")
            if computer3 == 1:
                print("Computer threw rock!")
                print("You lost!")
            if computer3 == 2:
                print("Computer threw paper!")
                print("You won!")
        else:
            print(
                "You did not enter a valid option. To choose an option, please enter the option's corresponding number."
            )
elif gamemode == 4:
#best of 3
    print("")
    print('You chose "Best of 3"!')
    print("")
    print("For reference: 1 = Rock, 2 = Paper and 3 = Scissors.")
    print(
        "To choose an option, please enter the option's corresponding number.")
    print("")
    playerwin = 0
    computerwin = 0
    bestof3 = 0
    stop = 0
    while stop == 0:
        player4 = int(input("Rock, Paper, Scissors? "))
        computer4 = random.randint(1, 3)
        if player4 == computer4:
#ties will not count towards the 3 rounds
            if player4 == 1:
                print("You threw rock!")
#display what player threw
            elif player4 == 2:
                print("You threw paper!")
            elif player4 == 3:
                print("You threw scissors!")
            if computer4 == 1:
                print("Computer threw rock!")
#display what computer threw
            elif computer4 == 2:
                print("Computer threw paper!")
            elif computer4 == 3:
                print("Computer threw scissors!")
            print("It's a tie!")
        elif player4 == 1:
            print("You threw rock!")
            if computer4 == 2:
                if computer4 == 1:
                    print("Computer threw rock!")
                elif computer4 == 2:
                    print("Computer threw paper!")
                elif computer4 == 3:
                    print("Computer threw scissors!")
                print("You lose!")
                computerwin += 1
                bestof3 += 1
                if bestof3 == 3:
                    if playerwin > computerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You won!")
                        print("Thanks for playing!")
                        stop += 1
                    if computerwin > playerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You lost!")
                        print("Thanks for playing!")
                        stop += 1
            if computer4 == 3:
                if computer4 == 1:
                    print("Computer threw rock!")
                elif computer4 == 2:
                    print("Computer threw paper!")
                elif computer4 == 3:
                    print("Computer threw scissors!")
                print("You win!")
                playerwin += 1
                bestof3 += 1
                if bestof3 == 3:
                    if playerwin > computerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You won!")
                        print("Thanks for playing!")
                        stop += 1
                    if computerwin > playerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You lost!")
                        print("Thanks for playing!")
                        stop += 1
        elif player4 == 2:
            print("You threw paper!")
            if computer4 == 3:
                if computer4 == 1:
                    print("Computer threw rock!")
                elif computer4 == 2:
                    print("Computer threw paper!")
                elif computer4 == 3:
                    print("Computer threw scissors!")
                print("You lose!")
                computerwin += 1
                bestof3 += 1
                if bestof3 == 3:
                    if playerwin > computerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You won!")
                        print("Thanks for playing!")
                        stop += 1
                    if computerwin > playerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You lost!")
                        print("Thanks for playing!")
                        stop += 1
            if computer4 == 1:
                if computer4 == 1:
                    print("Computer threw rock!")
                elif computer4 == 2:
                    print("Computer threw paper!")
                elif computer4 == 3:
                    print("Computer threw scissors!")
                print("You win!")
                playerwin += 1
                bestof3 += 1
                if bestof3 == 3:
                    if playerwin > computerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You won!")
                        print("Thanks for playing!")
                        stop += 1
                    if computerwin > playerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You lost!")
                        print("Thanks for playing!")
                        stop += 1
        elif player4 == 3:
            print("You threw scissors!")
            if computer4 == 1:
                if computer4 == 1:
                    print("Computer threw rock!")
                elif computer4 == 2:
                    print("Computer threw paper!")
                elif computer4 == 3:
                    print("Computer threw scissors!")
                print("You lose!")
                computerwin += 1
                bestof3 += 1
                if bestof3 == 3:
                    if playerwin > computerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
#list how many games each side has won before
                        print("You won!")
                        print("Thanks for playing!")
                        stop += 1
                    if computerwin > playerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You lost!")
                        print("Thanks for playing!")
                        stop += 1
            if computer4 == 2:
                if computer4 == 1:
                    print("Computer threw rock!")
                elif computer4 == 2:
                    print("Computer threw paper!")
                elif computer4 == 3:
                    print("Computer threw scissors!")
                print("You win!")
                playerwin += 1
                bestof3 += 1
                if bestof3 == 3:
                    if playerwin > computerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You won!")
                        print("Thanks for playing!")
                        stop += 1
                    if computerwin > playerwin:
                        print ("")
                        print("Computer won {} games.".format(computerwin))
                        print("You won {} games.".format(playerwin))
                        print("You lost!")
                        print("Thanks for playing!")
                        stop += 1
#end 
