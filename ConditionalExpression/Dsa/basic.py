numbers=[2,4,5,4,5,4,5,90,7,8]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]==numbers[j]:
            print(" Duplicte number is",numbers[i])
        
            break