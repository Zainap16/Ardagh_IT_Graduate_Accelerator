import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

# 0 - Rock, 1 - Paper, 2 - Scissors

print("What do you choose? Type: 0 - Rock, 1 - Paper, 2 - Scissors")
user_choice = int(input())

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Invalid Input!!")
    
computer_choice = random.randint(0,2)

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
else:
    print("Invalid Input!!")

if user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif user_choice == 2 and computer_choice == 0:
    print("you lose")
elif user_choice > computer_choice:
    print("you lose")
elif computer_choice > user_choice:
    print("you win")



