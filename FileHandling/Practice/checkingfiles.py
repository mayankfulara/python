            #COPYING ONE FILE TO ANOTHER
'''THINKING PROCESS
STEP1. WE NEED TWO FILES
STEP2. READ AND COMPARE THE TWO FILES
STEP3. IF THE CONTENTS ARE SAME PRINT THE OUTPUT'''            
            
file1="another.txt"
file2="copy.txt"
with open(file1)as f:
    f1=f.read()
with open(file2)as f:
    f2=f.read()
if f1==f2:
    print(f"{file1}and{file2} are identical")
else:
    print(f"{file1} and {file2} are not identical")