a = [1,2,3,4,5]
def reverse(a):
    i = 0
    j = len(a) -1
    while i<j:
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1
    return a
print(reverse(a))