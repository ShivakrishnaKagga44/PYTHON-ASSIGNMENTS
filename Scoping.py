'''
Declare a global variable and assign it a value
Create a function that declares a local variable with the same name as the global variable and assigns it a different value
Inside the function, print both the global and local variables to demonstrate their accessibility and values
Call the function to test the scope of the variables
'''
c=50
def first():
    c=60
    
    print("Local Variable",c)
    print("global variable ",globals()['c'])
first()
print("Outside of the function: ",c)