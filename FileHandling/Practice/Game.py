                       #FUN GAME PROGRAM
'''THINKING PROCESS
THE MAIN FOCUS OF THIS PROGRAM IS TO GENERATE A HIGH SCORE AND IF THE SCORE IS GREATER THAN THE SCORE
ALREADY PRESENT THEN THE NEW HIGHER WILL BE SWAPPED WITH THE SCORE
STEP1. TO GENERATE THE SCORE WE WILL BE TAKING THE HELP OF RANDOM FUNCTION
STEP2. WE WILL MAKE A FUNCTION TO STORE THE SCORE GENERATED
STEP3. WE WILL THEN COMPARE THE TWO SCORE
STEP4. IF THE SCORE WILL BE GREATER WE WILL SWAP OTHERWISE A MESSAGE WILL BE GIVEN'''
import random
def game():
    return score
score=random.randint(10,300)
fscore=game()
print(fscore)
with open("highscore.txt") as f:
    highscore=int(f.read())
if fscore>highscore:
    with open("highscore.txt",'w') as f:
        f.write(str(fscore))
else:
    print(f"Sorry {fscore} is not the highest score :((((")

