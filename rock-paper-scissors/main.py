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
import random

choice = int(input("Wha do you choose 0 for Rock, 1 for Paper, 2 for Scissors "))
print("\nPLAYER")
rps = [rock,paper,scissors]
rps2 = ["rock","paper","scissors"]
if choice == 0:
  print(rps[0])
if choice == 1:
  print(rps[1])
if choice == 2:
  print(rps[2])
player1 = choice

print("COMPUTER")
computer_choice = random.randint(0,2)
if computer_choice == 0:
  print(rps[0])
if computer_choice == 1:
  print(rps[1])
if computer_choice == 2:
  print(rps[2])
computer = computer_choice

print(f"{rps2[choice]} VS {rps2[computer_choice]}")

if choice==0 and computer_choice ==0:
  print("draw")
if choice == 0 and computer_choice ==1:
  print("You Lose")
if choice == 0 and computer_choice ==2:
  print("You Win")
if choice==1 and computer_choice ==0:
  print("draw")
if choice == 1 and computer_choice ==1:
  print("You Win")
if choice == 1 and computer_choice ==2:
  print("You Lose")
if choice==2 and computer_choice ==0:
  print("You Lose")
if choice == 2 and computer_choice ==1:
  print("You Win")
if choice == 2 and computer_choice ==2:
  print("Draw")