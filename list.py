lst=["Adnan","Sharib","Saim","Abdul","Shaddu"]
print(lst)
print(lst[1]) #Access the elemnt through indexing
print(lst[-2])
print(lst[3])

print("_"*20)

#Modify the List
lst[1]="Talib"
print(lst)

print("_"*20)

#Slicing
print(lst[1:4])

print("_"*20)

#reverse
print(lst[::-1])
print(lst[::-2])

print("_"*20)

#appending
lst.append("Nabil")
print(lst)

print("_"*20)

#Remove
lst.remove("Talib")
print(lst)

print("_"*20)

#length
print(len(lst))

print("_"*20)

#Sorting
list=[4,7,2,9,3]
print(sorted(list))

print("_"*20)

#To Find the Element
lst=['Adnan', 'Saim', 'Abdul', 'Shaddu', 'Nabil']
print(lst.index('Saim'))

#To count the element
print(lst.count("Saim"))

# Extending 
lst.extend(["Arav","Salman"])
print(lst)

#Maximum value and minimum value 
print(max(list))
print(min(list))    

print("_"*20)

#iterating the element to the list /Direct way 

for i in lst:
    print(i)

print("_"*20)

#iterating the element to the list /indexing

for i in range(len(lst)):
    print(lst[i])

print("_"*20)

# to reverse the list through loop
for i in range(len(lst)-1,-1,-1):
    print(lst[i])





