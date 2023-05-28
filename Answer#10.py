# Write a Python program to reverse a tuple.

def reverse(tuple_collection):
    new_tuple=tuple_collection[::-1]
    return new_tuple

tuple_collection=("apple","orange","tomato",4,5,6,"lotus","rose","lilly","jasmine")
print(reverse(tuple_collection))

