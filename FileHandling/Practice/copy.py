          #THIS PROGRAM IS TO CREATE A COPY OF THE TEXT FILE
'''THINKING PROCESS
STEP1. WE NEED TO READ THE FILE THAT WE WANT TO PRINT
STEP2. AFTER READING THE FILE WE NEED TO COPY THE CONTENTS OF THE FILE AND THEN PRIBNT THEM'''

with open("another.txt")as f:
    content=f.read()
with open("copy.txt",'w')as f:
    f.write(content)