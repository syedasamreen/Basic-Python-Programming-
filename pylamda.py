# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print("Inside the function : ", total)
   return total;

# Now you can call sum function
total = sum( 10, 20 );
print("Outside the function : ", total) 

total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print("Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print("Outside the function global total : ", total)


square = lambda x : x * x
print(square(5))

def square(x):
    return x * x
    
sum = lambda x, y, z : x + y + z
print(sum(5, 10, 15))

greet = lambda : print('Hello World!')
print(greet())

print((lambda x: x*x)(5))

sqrList = map(lambda x: x*x, [1, 2, 3, 4])
print(next(sqrList))

name = 'Steve'
def greet():
    name = 'Bill'
    print('Hello ', name)
