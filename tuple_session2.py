
# Tuple Packing  => Packing means grouping multiple values into a single tuple

tuple1=10,20,30

print(tuple1)

print(type(tuple1))

tuple2=(10,20,30)
print(tuple2)

print(type(tuple2))

# Unpacking Tuple => It means extracting values from a tuple into individual variables

a1,b1,c1=tuple1

print(a1)

print(b1)

print(c1)

x,y,z=("Python","JS","Java")
print(x)
print(y)
print(z)

# The number of variables on the left must match the number of elements in the tuple. Otherwise, Python will throw a ValueError."


# i,j=(10,20,30)

# *
tuple3=(1,2,3,4,4,5)
a,*b,c=tuple3

print (a)
print(b)
print(c)

one,two,*three =(1,2,3,4,4,5)

print(one)
print(two)
print(three)


# Swap Values without Temp Variable

x1=5
x2=10

print("Before swap , value of x1 is : " , x1) #x1=5
print("Before swap , value of x2 is : ", x2) #x2=10

x1,x2=x2,x1

print("After swap , value of x1 is : " , x1) #x1=10
print("After swap , value of x2 is : ", x2) #x2 =5
