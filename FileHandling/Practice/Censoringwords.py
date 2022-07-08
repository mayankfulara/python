             #IN THIS CODE WE ARE GOING TO CENSOR THE WORDS GIVEN BY THE USER
'''TAKE THE INPUT FROM THE USER THAT HE WANTS TO HIDE'''



cword=input("Enter the word to hide: ")
with open("this.txt")as f:   #OPENING THE FILE WHERE THE TEXT IS PRESENT
    content=f.read()         #READING THE CONTENS OF THE FILE
if cword not in content:     #CHECKING THE CONDITION WHETHER THE WORD GIVEN BY USER 
                             #IS PRESENT OR NOT
    print("Sorry this qword is not present")
for word in cword:           #REPLACING THE WORD WITH CENSORED WORD
    content=content.replace(cword,"@#%@#%$#$#$")
with open("this.txt",'w')as f:  #TELLING THE PUTHON INTERPRETER TO SWAP THE WORDS
    f.write(content)