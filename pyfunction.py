def greet():
    """This function display the hello world"""
    print("hello world")
    
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return
   
#help(greet)


def greet(name):
    print('hello',name)
    
greet('sam')

def greet(name1, name2, name3):  
    print ('Hello ', name1, ' , ', name2 , ', and ', name3)
    
greet('Steve', 'Bill', 'Yash')


def greet(*names):
	i=0
	print('Hello ', end='')
	while len(names) > i:
		print(names[i], end=', ')
		i+=1

greet('Steve', 'Bill', 'Yash') 
greet('Steve', 'Bill', 'Yash', 'Kapil', 'John', 'Amir')


def greet(firstname, lastname):
    print ('Hello', firstname, lastname)

greet(lastname='Jobs', firstname='Steve')

def greet(**person):
	print('Hello ', person['firstname'],  person['lastname'])
	
	
def greet(name = 'Guest'):
    print ('Hello', name)

greet()
greet('Steve')
	
	
def sum(a, b): 
    return a + b
    
total=sum(10, 20) 
print(total)
total=sum(5, sum(10, 20))
print(total)

def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return
	
	
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;
   
printme("I'm first call to user defined function!")
printme("Again second call to the same function")	

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme('sam')

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme( str = "My string")

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )

# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
