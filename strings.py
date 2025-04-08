# 3 ways to create a string in python

# 1st way - ''
name='Anshita'

# 2nd way - ""
greeting="Hello World!"

# 3rd way - """ """
mutiline= """This is
a multiline
string. """

print(name)
print(greeting)
print(mutiline)

# Indexing in Python  - 0 , left to right
word = "Python"
print(word[0])
# word[0]='J'

str="AB Automation Hub"
print(str[2])

#Index starts from 0
# Negative Indexing - Right to Left, -1
print(word[-1])
print(word[-4])
print(str[-5])

#Slicing - Extract some part of the string
text="Automation" 
print(text[0:5]) #Autom
print(text[:2]) #Au
print(text[3:]) #omation
print(text[:]) #Automation
print(text[-4:-1])   # tio -2+1 = -1

# str[starting_index: ending_index] - 

# String Methods

# .lower() -> Converts to lowercase

message="Hello, Python Learners!"

print(message.lower())

# .upper() -> Converts to uppercase

print(message.upper())

# .endswith(substring) # returns true if string ends with passed substring

print(message.endswith("ers"))

# .replace(old,new) #replaces all occurences of old with new

print(message.replace("Python","Code")) #
print(message.replace("o","i"))


# .find() method finds the first occurrence of the specified value.

print(message.find("l"))

# len() function returns the length of a string
print(len(message))

# String Concatenation +

x="Python is "
y="awesome language"
z=x+y
print(z)

first="AB Automation"
second="Hub"
print(first+" "+second)

# String Repetition *

print(second*2) #HubHub


 # String, Create , Access, Slice , Some useful string methods 
 

# Here are a few practice problems for you to try out after this video:

"""
Create a string "coding" and print only the middle three characters.
Hint: Use slicing

2. Take the string "DataScience" and print every second character.
Hint: Use step in slicing

3. Concatenate the strings "Learn", "Python", and "Now" with - in between.
Expected Output: Learn-Python-Now

4. Use .find() to get the index of "o" in the string "Hello World".

5. Print "ABCD" three times using a single line of code.
Expected Output: ABCDABCDABCD

6. From the string "coder", print the last 4 characters using slicing.

7. Convert the string "ABAutomationHub" to all lowercase, then all uppercase.

8. Replace "AB" with "XY" in the string "ABAutomationHub" and print the result.


"""



