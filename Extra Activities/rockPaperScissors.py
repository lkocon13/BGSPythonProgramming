import random
import sys
import time

# computer selects random interger from 1 - 3
computer_Number = random.randint(1, 3)


# assigning computer choice to string - easier to read for programmer
if computer_Number == 1:
    computer_Choice = "Rock"
elif computer_Number == 2:
    computer_Choice = "Paper"
elif computer_Number == 3:
    computer_Choice = "Scissors"
else:
    print("[-] Program Error, contact admin")

print(computer_Choice)

# score keeping system
user_Score = 0
computer_Score = 0


# user input
userInput = input("Please choose Rock, Paper or Scissors:\n")


if userInput == ("Rock" or "rock") and computer_Choice == "Scissors":
    print("You win...")
    user_Score = user_Score + 1
    print("Your new score is " + str(int(user_Score)))
    return user_Score
elif userInput == ("Rock" or "rock") and computer_Choice == "Paper":
    print("You lose...")
    user_Score = user_Score - 1
    print("Your new score is" + user_Score)
    return user_Score

if userInput == ("Scissors" or "scissors") and computer_Choice == "Paper":
    print("You win")
    user_Score = user_Score + 1
    print("Your new score is " + str(int(user_Score)))
elif userInput == ("Scissors" or "scissors") and computer_Choice == "Rock":
    print("You lose...")
    user_Score = user_Score - 1
    print("Your new score is" + user_Score + "!")

if userInput == ("Paper" or "paper") and computer_Choice == "Rock":
    print("You win")
    user_Score = user_Score + 1
    print("Your new score is " + str(int(user_Score)))
elif userInput == ("Paper" or "paper") and computer_Choice == "Scissors":
    print("You lose...")
    user_Score = user_Score - 1
    print("Your new score is" + str(int(user_Score)))
