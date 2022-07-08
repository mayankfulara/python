          #IN THIS PROGRAM WE ARE GOING TO CHECK WHETHER A WORS I PRESENT IN THE LOGS
with open ("log.txt")as f:
    content=f.read()
if 'pyhon' or 'Python' in content:
    print("Yes python is present")
else:
    print("No sorry python is not present")