# Create Tuple using () , even without brackets

tuple1=(1,2,4,5)
print(tuple1)
print(type(tuple1))
tuple2="NewYork","Dubai","Singapore"
print(type(tuple2))

# Accessing Tupple Items - Index starts from 0
print(tuple1[1])
print(tuple2[2])

#Negative Indexing -> It starts from end -1, -2
print(tuple1[-2])

#Slicing - part of tuple -> : tuple[start:stop]

languages=("java","js","python","go","php")
print(languages[1:4])

#Tuple with One Item => pass comma (,)

single_tuple=(1,)
print(type(single_tuple))

# Tuple is Immutable => we cannot change, add or remove items after the tuple has been created
#languages[0]="groovy"
# print(languages)

# Length of Tuple -> len()

print(len(languages)) #5

#Tuple Methods => count() and index()
books=("The Alchemist","The Secret","Atomic Habits","Ikigai","The Secret")
print(books.count("The Secret")) #2
print(books.index("Ikigai")) #2

# Join Two Tuples
book1=("The Power","Think")
final_book=books+book1
print(final_book)

# Multiply  * => repeating the items
multiply=book1*3
print(multiply)