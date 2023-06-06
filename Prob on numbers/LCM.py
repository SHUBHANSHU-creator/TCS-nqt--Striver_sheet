def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
print(gcd(4,8))
n1,n2 = 4,8
g= gcd(n1,n2)
print((n1*n2)//g)

# n1,n2 = 3,6
# def fact(n,counter):
#     while n:
#         for i in range(2,n+1):
#             if n%i == 0:
#                 counter[i] = n//i
#                 n = n%i

# counter1 = {}
# counter2 = {}
# fact(n1,counter1)
# fact(n2,counter2)
# print(counter1,counter2)
# lcm =1
# visit = set()
# for i in counter1:
#     if i in counter2:
#         visit.add(i)
#         lcm *= i*max(counter1[i],counter2[i]) if max(counter1[i],counter2[i])!=0 else 1
#     else:
#         visit.add(i)
#         lcm *= i*counter1[i] if counter1[i]!=0 else 1

# for i in counter2:
#     if i not in visit:
#         lcm *= i*counter2[i] if counter2[i]!=0 else 1
# print(lcm)
    