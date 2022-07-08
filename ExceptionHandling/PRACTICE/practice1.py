#THE PROBLEM WAS WE HAVE TO OPEN MULTIPLE TEXT FILES AND IF A TEXT FILE IS NOT PRESENT THAN WE HAVE 
#TO HANDLE THAT ERROR 
'''SO IN ORDER TO DO SO WE ARE GOING TO USE THE TRY AND EXCEPT'''

def readfile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{filename} file not found")

readfile("1.txt")
readfile("2.txt")
readfile("3.txt")
