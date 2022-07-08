def increment(num):
    try:
        return (num)+1
    except:
        raise ValueError("Error in the input please check:(( ")

a=increment('a34')
print(a)
