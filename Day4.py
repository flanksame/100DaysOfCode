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

#Write your code below this line 👇
Game_images=(rock,paper,scissors)
user_choice=int (input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors. "))
if user_choice>=3 or user_choice<0:
  print("You choose invalid input!")
else:  
 print("user choose:\n")
print(Game_images[user_choice])

computer_choice=random.randint(0,2)
print("computer choose:\n")
print(Game_images[computer_choice])

if user_choice==2 and computer_choice==0:
  print("You Lose!")
elif user_choice > computer_choice:
  print("You win !!!")
elif computer_choice==2 and  user_choice==0:
  print("You Win !!")
elif user_choice==computer_choice:
  print("Draw!!")


