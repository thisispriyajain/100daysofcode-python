import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Rock beats scissors
#Paper beats rock
#Scissors beats paper
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
compChoice = random.randint(0,2)
print(f"Computer chose {compChoice}")

if userChoice == compChoice:
    print("It's a draw!")
elif userChoice == 0 and compChoice == 2:
    print("Rock beats scissors. You win!")
elif userChoice == 1 and compChoice == 0:
    print("Paper beats rock. You win!")
elif userChoice == 2 and compChoice == 1:
    print("Scissors beats paper. You win!")
elif userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number. You lose!")
else:
    print("You lose!")
