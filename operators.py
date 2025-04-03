# Arithmetic Operators 

# + - * / // % **


x=10
y=3

print("Addition : ",x+y) #10+3
print("Subtraction : ", x-y) #10-3
print("Multiplication: " ,x*y ) #10*3 = 30
print("Division : ", x/y) #10/3 = 3.33333
print("Floor Division: ", x//y) #10/3=3
print("Modulus : ", x%y) # 10%3 =1
print(x**y) # 10**3 = 10*10*10 = 1000

a =50
b=5

print(a/b) #50/5 = 10.0
print(a//b) #10

# Comparison Operators

x=10
y=50

print(x==y) #10==5 => False
print(x!=y) #10!=5 => True
print(x>=y) # 10>=5 => True
print(x<=y) # 10<=5 =>False
print(y>x) # 50>10 => True
print(x>y) # 10>50 => False
print(y<x) # 50<10 => False
print(x<y) # 10<50 => True



# Logical Operators - and, or not

a=10
b=15
c=25

print(a>b and c>b) #10>15 and 25>15 => False and True =>False
print(a<b and c>b) # True

print(a>b or a>c) #10>15 or 10>25 => False or False => False
print(a>b or c>b) # False or True => True

print(not(a>b)) #10>15 - not False  => True

print(not(a>b or c>b)) #not True  => False


#Assignment Operators  =,+=, -=, *=, /=

x=10
y=x

x+=5 #  x=x+5 => 10+5 = 15
print(" add and assign : ", x)
x-=2 # x=x-2 => 15-2 = 13
print(" subtract and assign : ", x)
x*=2 # x=x*3 => 13 * 2 = 26
print(" multiply and assign : ", x)
x/=2 # x=x/2 => 26/2 = 13.0
print(" divide and assign : ", x)


print(x)
print(y)



# Membership Operators - in , not in

x =[1,2,5,8,22]

print(3 in x) # False
print(5 in x) # True

print(3 not in x) # True

print(5 not in x) #False

#Identity Operators - is, is not



x=10
y=10

print(x is y) #True
print(x is not y)  #False

a="Hello"
b="hello"

print(a is b)