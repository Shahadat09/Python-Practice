def greet():
    print("Hello, My name Shahadat")
greet() 

#print([greet() for i in range(10)])
def add():
    s1=20
    s2=10
    print(s1+s2)
add()
def sub(s1,s2):
    print(s1-s2)
sub(30,23)


'''def mult():
    m1 = int(input("Enter a number: "))  # Convert input to integer
    m2 = int(input("Enter another number: "))  # Convert input to integer
    print (m1 * m2)
mult()'''

#Return

def arith(a,b):
    return a+b,a*b,a-b,a/b
result=arith(5,10)
print(result)

#Calling different functions
lst=[1,2,3,4,5,6]
def sqr(lst):
    return [i**2 for i in lst]
def cub(lst):
    return[i**3 for i in lst]
print(sqr(lst))
print(cub(lst))

def final(lst):
    lst_1=sqr(lst)
    lst_2=cub(lst)
    return lst_1+lst_2
ans=final(lst)
print(ans)
