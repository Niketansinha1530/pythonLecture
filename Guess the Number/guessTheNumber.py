import random


print("****************** GUESS THE NUMBER GAME ********************")

randomeGenerated= random.randint(1,100)

print("Guess the number between 1 to 100")



count =0
while(True):
   
    try:
         count +=1
         playerNumber=int(input("Enter your number:  "))

         if(playerNumber>randomeGenerated):
           print("Guess smaller Number Please")
         elif(playerNumber<randomeGenerated):
            print("Guess Bigger Number Please")
         elif playerNumber < 1 or playerNumber > 100:
            print("Please guess a number between 1 and 100!")
         else:
            print("You Guess the correct Number")
         break
    except ValueError:
         print("Invalid input! Please enter an integer.")


print(f"You guess the Number after {count} times")

