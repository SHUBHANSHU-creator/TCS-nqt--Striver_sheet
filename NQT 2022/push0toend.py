a = [4,5,0,1.9,0,5,0]
count = 0
for i in a:
    if i == 0:
        count+=1
b = [i for i in a if i!=0]
b+=[0 for i in range(count)]
print(b)
