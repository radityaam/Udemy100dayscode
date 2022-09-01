from logo import stages
import random
import logo
print(logo.logo)
                                                       

lives = 6
word_list = ["coffee", "cappucino", "piccolo","caffelatte"]


word = random.choice(word_list)
wordg = []
for i in word:
  wordg.append("_")
print(wordg)
fword =[]
for a in word:
  fword.append(a)
end_of_game = True
guess1 = []

while end_of_game == True :
  guess = input("Guess the word : ").lower()
  index = 0

  if guess not in fword:
    lives = lives -1
    print("\nYou got the wrong answer\n")
  if guess in guess1:
    print("\nYOU ALREADY ASNWER THIS SIR\n")
    
  for letter in word:
    if guess == letter:
      wordg[index] = letter
      guess1.append(guess)
    index+=1

  print(wordg)
  print(stages[lives])
  if lives == 0:
    end_of_game = False
    print("GAME OVER")
  if "_" not in wordg:
    end_of_game = False
    print(f"You win!!! the words is {word}, congratulation!")
