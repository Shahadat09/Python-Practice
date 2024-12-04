'''#Square all the element of the list
list=[1,2,3,4,5,6,7,8]
print(list)
list=[i**2 for i in list]
print(list)

print("*"*80)

l=[2,5,8,12,18]
ls=[]
for i in l:
    print(i**2, end=" ")

check=[2,10,17,29,30]
for i in check:
    if(i%2==0):
        print(i, end =" ")
print("*"*60)

#Finding the first 10 even no
print([i for i in range(21) if i%2==0])
print("*"*60)


#First 10 no square root
print([i**2 for i in range(21) if i%2==0])

#Multidimensional list
print([[j for j in range(5) ]for i in range(3)])

#To upper 
words=["apple","mango","grapes"]
uppercase_words=[word.upper() for word in words]
print(uppercase_words)'''

#to search the element in the list
check = [2, 10, 17, 29, 30]
print(check.index(10))
a = 17  


for index, value in enumerate(check):
    if value == a:
        print(f"Element {a} found at index {index}")






    