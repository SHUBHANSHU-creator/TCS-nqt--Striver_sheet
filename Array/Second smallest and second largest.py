a = [2,5,1,3,0]
def second(a):
    if len(a) < 2:
        return -1
    a.sort()
    return [a[1],a[-2]]
print(second(a))