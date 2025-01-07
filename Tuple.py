#intitializing
tpl=(1,2,3,4,6)
print(tpl)

print("-"*30)

#accessing
print(tpl[0])
print(tpl[1])

print("_"*30)

#Slicing
print(tpl[1:3])

print("-"*30)

#Concatination

tpl1=(1,2,3,4,5,6)
tpl2=(6,5,7,8,8)
tpl=tpl1+tpl2
print(tpl)
print("-"*30)
#Tuple hold duplicate value but its immutable once we assigned the value we can not able to change 

#Iterating
print(tpl)
for i in tpl:
    print(i)
print("-"*30)

#Checking the element
print(6 in tpl)
check=5 in tpl
print(check)
print(11 in tpl)
print("-"*30)

#checking the frequency of element or count

print(tpl)
print(tpl.count(1))
print(tpl.count(4))
print("-"*30)

#Find the index of the element

print(tpl.index(4))
print(tpl.index(6))
print("-"*30)


#Multiply the tuple

print(tpl*3)
#All the value becomes three times

print("-"*30)

#We can not delete the element from the tuple because its immutable
print(type(5 // 2))
print(type(5 // 2))
print(type(5 / 2))







