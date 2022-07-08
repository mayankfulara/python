import os
with open("newbait.txt") as f:
    content=f.read()
with open("ogbait.txt",'w')as f:
    f.write(content)
os.remove("bait.txt")