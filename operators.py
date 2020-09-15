'''a="viz grover"
b="oreo milk"
red="green"
yellow="green"
print(a is not b)
print(red is yellow)
print('viz' in a)
print('viz' in b)
print('viz ' not in red)'''

'''l1=[1,2,3,4]
l2=[2,4,6,8,10,12]
for i in l1:
    i%2==0
for i in l2:
    i%2==0
print(any(l1))
print(all(l1))'''

'''import operator

li=[1,2,3,4,5,6]
print("original list: ",end=" ")
for i in range(0,len(li)):
    print(li[i],end=" ")
print("\r")
operator.setitem(li,slice(0,7),[7,8,9,0,12,13])
print("new list: ",end=" ")
for i in range(0,len(li)):
    print(li[i],end=" ")
print("\r")
operator.delitem(li,slice(1,2))
print("del list: ",end=" ")
for i in range(0,len(li)):
    print(li[i],end=" ")
print("\r")
print("item: ",end=" ")
print(operator.getitem(li,slice(1,3)))'''

import operator
'''a="viz grover"
b="grover"
c=0
print(operator.concat(a,b))
if(operator.contains(a,b)):
    print("true")
else:
    print("false")'''

a=0
b=1
print(operator.and_(a,b))
print(operator.or_(a,b))
print(operator.xor(a,b))
print(operator.invert(b))
