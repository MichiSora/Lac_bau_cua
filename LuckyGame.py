import random
i = 0
guesses =["shrimp", "crab", "chicken", "deer", "fish", "drink"]

guess = ["shrimp","shrimp","shrimp"]  #Write your guesses here

choices =["shrimp", "crab", "chicken", "deer", "fish", "drink", "shrimp", "crab",
   "chicken", "deer", "fish", "drink", "shrimp", "crab", "chicken", "deer",
   "fish", "drink"] 
   
profit = 0
TRIES = 50000. 						#Change this to see how many games you play
while (i < TRIES):
  i = i + 1
  profit = profit - len(guess)
  outcome = random.sample (choices, 3)
  
  for item in outcome:
    for g in guess:
        if (item == g):
            profit = profit + 2
print("You made $" + str(profit))
print("You made $" + str(profit/TRIES) + " per round.")
