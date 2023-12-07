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

# Write your code below this line 👇
import random
choices = [rock, paper, scissors]
options = len(choices) - 1

player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n")
print(choices[int(player)])

computer = str(random.randint(0,options))
print(f"Computer chose: \n {choices[int(computer)]}")

if player == "0":
    if computer == "0":
        print("Tie")
    elif computer == "1":
        print("You lose")
    elif computer == "2":
        print("You win")
elif player == "1":
    if computer == "0":
        print("You win")
    elif computer == "1":
        print("Tie")
    elif computer == "2":
        print("You lose")
elif player == "2":
    if computer == "0":
        print("You lose")
    elif computer == "1":
        print("You win")
    elif computer == "2":
        print("Tie")
else:
    print("You typed an invalid number, you lose!")




