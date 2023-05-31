n = '100'
cur = 0
i = len(n)-1
res = 0
while i>=0:
    if n[i] == '1':
        res += 2**cur
    cur+=1
    i-=1
print(res)