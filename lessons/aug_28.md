# Lesson Title #
## Aug 28 2023 ##

Lesson Notes
```.py
def name_of_function(arguments): #How to define a function
    variables = 'When you call a function, imagine it as a box, where inputs get into the box, and the inputs get passed through the process defined in the function and returned as an output.'
    return variables #Output of a function

#For example:
def square(x:int): #Type hint: gives an idea as to what data type the argument should be
    return x * x

def larger_Integer(A:int, B:int)->int:
    output = 'A'
    if A<B:
        output = 'B'
    return output

    r= larger_Integer(2012, 15) #Calling the function and saving the return value as variable r
    print (r) #Printing the variable

#inputs to the function are different from inputs from the user.
```
