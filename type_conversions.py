# Implicit / Automatic Type Conversion

num_int=5
num_float=2.5
result=num_int+num_float #5+2.5 = 7.5 #

print("value of result is ", result) 
print("data type of result is ", type(result) ) # float

num_boolean=False 
int_num=10
output=num_boolean+int_num #0+10 = 10
print(" output is ", output) #10
print(" data type of output is ", type(output)) #int


#Explicit Type Conversion (Typecasting)

num_str="100"
print("num_str ", num_str," and data type is ", type(num_str) ) #str- value
output_int= int(num_str) # 100
print(" data type of output_int " ,output_int, type(output_int)) # int

#manual + automatic
x="12" #string
y=int(x) #12
add=y+10.5 #float
int_add=int(add) #22

print(int_add, type(int_add)) #12+10 = 22.5

# Common Issue 1
i="AB Automation Hub" 
j=10
#z = int(i)
#print(z)

# Common Issue 2

age="25"
print("My age is "+ age) #


"""
1. Type conversion is the process of converting a data type into another data type.
2. Implicit type conversion is performed by a Python interpreter only.
3. Explicit type conversion is performed by the user by explicitly using type conversion functions.
4. Explicit type conversion is also known as typecasting.
5. Python, when performing implicit type casting, avoids the loss of data.
int + float = float ( prevents data loss)


"""

