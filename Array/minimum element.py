a = [2,5,1,3,0]
mn = a[0]
for i in a:
    if i < mn:
        mn = i
print(mn)


#method2 
a.sort()
print(a[0])