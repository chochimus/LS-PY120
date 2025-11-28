"""
Which of the following are objects in Python? If they are objects, 
how can you find out what class they belong to?

True
'hello'
[1, 2, 3, 'happy days']
142
{1, 2, 3}
1.2345

All of these are objects in python. One way to find the class is to use the type function
followed by .__name__. We can also use the direct .__class__.__name__ instance variables,
but with integers you must use parentheses to avoid an error where the interpreter interprets
the . as a decimal
"""
print(type(True).__name__)
print(type('hello').__name__)
print(type([1, 2, 3, 'happy days']).__name__)
print(type(142).__name__)
print(type({1, 2, 3}).__name__)
print(type(1.2345).__name__)

print((142).__class__.__name__)