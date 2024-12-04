lls=[[1,2,3,4],
[5,6,7,8],
[9,10,11,12]]

print("Original matrix:",lls)
print(lls[0])
print(lls[0][1])
print(lls[1][0])
lst=[2,4,8,9,["Ashish",9]]
print(lst)
print(lst[0])
print(lst[4][1])
#Accessing the Elements
list=[[1,2,6,9,5],[20,4,34,8,1],[8,38,18,2,7]]
print(list)
print(list[1][1])
print(list[1][0])
print(list[2][2])
#Modify the values

print(list)
list[1][1]=9
print(list)
list[1]="Shahadat Rahman"
print(list)

#Appending the values
print(list)
print(list.append([4,4,8,8]))
print(list)

#Delete the element

print(list)
del(list[1])
print(list)

#To know the Length
print(len(list))


print("_"*20)
#To reverse
print(list[::-1])

print("_"*20)

print(list)
list[1][0]=7
print(list)
print("*"*30)

for i in list:
    for j in i:
        print(j,end=" ")