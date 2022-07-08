                 #FINDING A WORD IN THE FILE
'''THINKING PROCESS
STEP1. OPEN THE FILE YOU WANT TO READ
STEP2. TAKE THE WORD WHICH YOU WANT TO READ AS AN INPUT FROM THE USER
STEP3. COMPARE THE WORD GIVEN BY THE USER '''
with open("POEMS.txt")as f:
  t=f.read()
word=input("Enter the word: ")
if word in t:
    print("The word is present")
else:
    print("We are sorry ")

