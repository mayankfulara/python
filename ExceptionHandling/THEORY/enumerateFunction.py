#PRINTING THE INDEX OF THE LIST USING TWO WAYS CONVENTIONAL AND USING ENUMERATE
list1=[23,True,5.6,"Mayank"]
#index=0
#for item in list1:
#    print(item,index)
#    index+=1
for index,item in enumerate(list1):
    print(item,index)