try:
    a=int(input("Enter the number: "))
    i=a+23
    print(i)
except Exception as e:
    print(e)
    exit()

finally:
    print("We are done")