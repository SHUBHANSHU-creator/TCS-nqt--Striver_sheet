n1 = 3
n2 = 6
gcd = 1
for i in range(1,min(n1,n2)+1):
    if n1%i == 0 and n2%i==0:
        gcd = i
print(gcd)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
print(gcd(4,8))

a = ["a","b","c"]
b='/'.join(a)
b = b.strip('/').split()
print(b)