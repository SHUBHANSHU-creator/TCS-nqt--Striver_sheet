s = 'Take u forward is Awesome'
counter = {'v':0, 'c':0, 'w':0 }
vowels = 'aeiouAEIOU'
for i in s:
    if i in vowels:
        counter['v']+=1
    elif i == ' ':
        counter['w']+=1
    else:
        counter['c']+=1
print(counter)    
