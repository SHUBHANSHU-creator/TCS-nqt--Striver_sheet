n = 10
n = bin(n).replace('0b',"")
a =''
for i in n:
    if i=='1':
        a+='0'
    else:
        a+='1'
print(int(a,2))