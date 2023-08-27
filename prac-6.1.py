l=[1,2,4,8,2.4]
for i in l:
    print(i)    
l.append(5)
l.remove(2.4)
for i in l:
    print(i)
print(l[1:4]) 
l.sort()
print(l)
l.reverse()
print(l)
x=tuple(l)
print(x) 
y=list(l)
print(l)  
