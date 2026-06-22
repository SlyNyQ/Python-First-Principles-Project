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

your_choice = int(input("Please select the rock(0), paper(1), or scissors(2): \n"))
computer_choice = random.randint(0,2)

# #My Method
# #Your choice conditions
# if your_choice == 0:
#     print("Your choice is rock")
#     print(rock)
#     # Computer Choice conditions
#     if computer_choice == 0:
#         print("Computer choice:")
#         print(rock)
#         print("Draw")
#     elif computer_choice == 1:
#         print("Computer choice:")
#         print(paper)
#         print("You lose")
#     elif computer_choice == 2:
#         print("Computer choice:")
#         print(scissors)
#         print("You win")
# elif your_choice == 1:
#     print("Your choice is paper")
#     print(paper)
#     # Computer Choice conditions
#     if computer_choice == 0:
#         print("Computer choice:")
#         print(rock)
#         print("You win")
#     elif computer_choice == 1:
#         print("Computer choice:")
#         print(paper)
#         print("Draw")
#     elif computer_choice == 2:
#         print("Computer choice:")
#         print(scissors)
#         print("You lose")
# elif your_choice == 2:
#     print("Your choice is scissors")
#     print(scissors)
#     # Computer Choice conditions
#     if computer_choice == 0:
#         print("Computer choice:")
#         print(rock)
#         print("You lose")
#     elif computer_choice == 1:
#         print("Computer choice:")
#         print(paper)
#         print("You win")
#     elif computer_choice == 2:
#         print("Computer choice:")
#         print(scissors)
#         print("Draw")
# else:
#     print("You typed an invalid number \n You lose!!")

#Alternate method: According to instructor
game_images = [rock, paper, scissors]
if your_choice <= 2 and your_choice >=0:
    print(game_images[your_choice])

print(f"Computer choice is {computer_choice}")
print(game_images[computer_choice])

if your_choice >= 3 or your_choice < 0:
    print("You typed an invalid number \n You lose!!")
elif your_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and your_choice == 2:
    print("you lose")
elif computer_choice > your_choice:
    print("you lose")
elif computer_choice < your_choice:
    print("you lose")
elif computer_choice == your_choice:
    print("draw")
