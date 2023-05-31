n = 18
sm = ''
while n:
    sm+= str(n%2)
    n = n//2
print(sm[::-1])

#method2 - using right shift

flag = 0
for i in range(32,-1,-1):
    if ((n>>i)&1):
        flag = 1
        sm+='1'
    else:
        if flag:
            sm+='0'
print(sm)