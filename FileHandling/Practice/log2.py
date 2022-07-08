# IN THIS PROGRAM WE ARE GOING TO FIND IN WHICH LINE THE WORD IS PRESENT
content = True
i = 1
word = input("Enter the word which you are searching for: ")
with open("log.txt")as f:
    while content:
        content = f.readline()
        if word in content:
            print(content)
            print(f"{word} is present")
            print(i)
            i+=1
        if word not in content:
            print("Sorry the word you entered is not present ")
            break    