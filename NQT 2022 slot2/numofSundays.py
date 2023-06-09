d = input()
n = int(input())
hmap = {
    'mon':1,
    'tue':2,
    'wed':3,
    'thu':4,
    'fri':5,
    'sat':6,
    'sun':0
}

first = 1+(7-hmap[d])
lastday = 1+n
count = 0
while first <= lastday:
    count+=1
    first+=7
print(count)