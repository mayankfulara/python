#IN THIS PROGRAM WE ARE GOING TO PRINT TABLES AND DISTRIBUTE THEM IN MULTIPLE FILES AND GIVE THEM UNDER 1 FOLDER
'''THINKING PROCESS
WE NEED TO GENERATE TABLE AND STORE THEM IN A FOLDER
STEP1. ASK THE USER THE RANGE OF THE TABLES THAT NEEDS TO BE GENERATED
STEP2.  '''
r=int(input("Enter the range till you want tables generated: "))
for i in range (2,r+1):
    with open(f"tables/Multiplication table of{i}.txt",'w') as f:
        for j in range (1,11):
            f.write(f"{i}X{j}={i*j}\n")