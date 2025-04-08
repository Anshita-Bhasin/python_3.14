#Conditional statements let you run different blocks of code based 
# on whether a condition is True or False.

# In Python, we use - if, elif and else

# if => The if statement is used to test a condition. 
# If the condition is True, the code block under if is executed.


# True, False
"""
age=10
if age>18:
    print("You are an adult...")
"""

#elif -> else if     
"""
age=1
if age>18:
    print("You are an adult...")
elif age<2:
    print("You are a toddler.")
elif age>5:
    print("You are a child, but no longer a toddler.")


# Multiple If Condition
# Using multiple if statements means each condition 
# is checked independently, even if a previous one is true.

age=22

if age>28:#False
    print(" You can vote ....")

elif age>20: # True
    print("You can drive....")

elif age>21: #True
    print("You can rent a car....")        
  
  
"""

# if -elif -else

# The else block runs only if none of the previous conditions were True. 

age=22

if age>18:#True
    print(" You can vote ....")

elif age<20: # False
    print("You can drive....")

elif age<21: #False
    print("You can rent a car....")        
  

else:
  print("You're in else block!")

# Multiple Conditions (and, or)

username="admin"
password="12345"

if username=="admin" and password =="1234": # True and False - False
    print("Login Successful")

else:
    print("Invalid credentials...") 


day="Saturday"

if day=="Saturday" or day=="Sunday": #True or False - True
    print("It's the weekend...")

else:
    print("It's the week day...")    


 # Nested if statements
 
score = 55
has_passed = False

if has_passed: #False
    if score>80:#55>80 - False
        print("You passed with distinction!")
    else:
        print("You passed!")
else:
    print("You failed.")




# 
x = 1 
if x: #False
    print("Non-zero")
else:
    print("Zero")



# if , elif and else
# Multiple If statements
# Nested if conditions

# Don’t forget colons (:) at the end of conditions.
#Keep your indentations consistent (typically 4 spaces).