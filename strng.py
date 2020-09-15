'''str='we\'ll to the alexa'
st="yello \"colour\""
string=\'''python's "learning"\'''
s="https:\\oreo.com\\"
strng="{i} {z} {i}".format(i='viz',z='love')
digit="{0:e}".format(12)
print(str)
print(st)
print(string)
print(s)
print(strng)
del(strng)
string="edited string"
print(string)
print(str[4:-1].center(30,'-'),end=" ")
print(s[7])
print(digit)'''

'''list=[1,2,3,4,5,6]
lt=[1,'yes',2,3,4,'no']
lst=[['multi','digit'],['list','hai']]
list1=['simple','words','list','hai']
print(list)
print(lt)
print(lst)
print([lt[1]])
sliced=lt[3:-1]
print(sliced)
list.append((8,10))
print("after tuple appending:",end=" ")
print(list)
list.append(11)
for i in range(12,16):
    list.append(i)
print("appending in range:",end=" ")
print(list)
list.append(list1)
print("appending another list:",end=" ")
print(list)
list1.insert(2,'ki')
print("using insert method:",end=" ")
print(list1)
lst.extend(['ye'])
print("extend method can take arguments more than 1 unlike append:",end=" ")
print("lst")
list.pop(6)
print(list)
print(lst[1][1])
print(list)
for i in range(11,16):
    list.remove(i)
print(list)
print(list[::-1])
list.clear()
print(list)'''

'''list=[1,2,3,4,5,6]
print(tuple(list))
tuple2=(1,2,3,4,5)
tuple=('viz','grover')
print(tuple)
tul=('geeks',1,2,'for','geeks',3,4,5)
tuple1=('grover',)*10
print(tuple1)
for i in range(4):
    tuple=('viz',)
    print(tuple)
print(tul[3:9])
print(tul[::-1])
tuple3=(tuple2,tuple)
tuple4=tuple+tuple2
print(tuple3)
print(tuple4)'''

'''set1=set(["hello","world"])
string=('this is a string')
print(set(string))
list=set([1,2,3,4,5,6])
print(list)
mix=set(["mix",1,2,3,"set",7,8])
list.add(7)
for i in range(8,11):
    list.add(i)
list.add((11,12))
print(list)
list.update([13,14])
print(list)
list.remove(14)
list.discard((11,12))
print(list)
for i in set1:
    print(i,end=" ")
print('world' in set1)
list.clear()
print(list)
string=('v','i','v','e','n','c','y')
fzn=frozenset(string)
print(fzn)
print(frozenset())'''

'''dict={1:'letter',3:'box'}
print(dict)
dict={'name':'viz',1:[1,2,3,4]}
print(dict)
dict=dict({1:'letter',2:'box'})
print(dict)
pair=dict([(1,'for'),(2,'this')])
print(pair)
multi=dict({1:'letter',2:'box',3:{'a':'apple',4:'no'}})
dict[2]='circle'
print(dict)
dict['value_set']=6,7,8
print(dict)
dict[4]={'nest':{'bird':1}}
print(dict)
print(dict['name'][1])
print(multi[3][4])
del dict[1]
print(dict)
del multi[3]['a']
print(multi)'''

import array as arr

a=arr.array('i',[1,2,3,4])
d= arr.array('d',[2.3,3.4,6.9])
print("integer array: ",end=" ")
for i in range(0,4):
    print(a[i],end=" ")
print()    
print("decimal array: ",end=" ")
for i in range(0,3):
    print(d[i],end=" ")
print()
a.insert(5,6)
print("integer array after insettion: ",end=" ")
for i in a:
    print(i,end=" ")
print()
d.append(4.4)
print("decimal array after insertion: ",end=" ")
for i in d:
    print(i,end=" ")
print()
a.remove(3)
print("removing 1st occurance of 3",end=" ")
for i in a:
    print(i,end=" ")
print()
sarr=a[1:5]
print("sliced array",sarr)
a.pop(2)
print("after popping out element in array:",end=" ")
for i in a:
    print(i,end=" ")
print()
print(d[3])
print("index of 1st occurance of 6.9: ",end=" ")
print(d.index(6.9))
a[2]=9
for i in a:
    print(i,end=" ")
