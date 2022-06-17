a,b = 0,1
while a<1000:
      print(a, end=',')
      a,b = b, a+b
      
#defining a functions for fibonacci series

def fib(n):
    """Print a fibonacci series up to n."""
    a,b = 0,1
    while a < n:
         print(a)
         a,b = b, a+b
    print()
fib(10)

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
          result.append(a)    # see below
             a, b = b, a+b
    return result   
