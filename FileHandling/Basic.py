#f=open('D:\Python\FileHandling\sample.txt','r')
f=open('D:\Python\FileHandling\sample.txt')#by default it will read the file
text=f.read()
print(text)
f.close()