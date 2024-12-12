'''dict={1:'Aslam',2:'Asif',3:'Salman'}
print(dict)

print("*" * 20)

#Accessing the elements in dictionary
print(dict[2])

print(dict.get(1))

#Update and add the elements in dictionary

dict[6]="Pushpa"
dict[4]='Mohan'
dict[5]="Rohan"
print(dict)
del dict[6]
print(dict)
print(dict.keys())
print(dict.values())
dict[5]="Tipu"
print(dict)

print("*"*30)

#iterating through the dictionary

for k in dict.keys():
    print(k,dict[k])

print(dict.items())

for k,v in dict.items():
    print(k,v)
print("_"*30)

#check that key is present or not 
print(dict)
print(1 in dict)
print(10 in dict)

#Merging the dictionaries

d={1:'A',2:'B',3:'C'}
d_2={1:'a',2:'b',3:'c'}
d.update(d_2)
print(d)'''

list=[1,2,3,4,5]
print(list)
print(list[2])
list.append(9)
print(list)
list.remove(2)
print(list)
print(len(list))
list[2]=10
print(list)
print(sorted(list))
print(list[2:4])
print(list[::-1])
print(max(list))
print(min(list))
for i in list:
    print(i)
ls=[[22,11,333,211],
[12,67,87,32],
[10,76,543,87]]
print(ls)
print(ls[0])
print(ls[2])
print(ls[2][3])
ls[2][0]=13
print(ls[2][0])
dict={1:"Shaddu",2:"Nabil",3:"Mod"}
print(dict)
print(dict.get(1))
print(dict[1])