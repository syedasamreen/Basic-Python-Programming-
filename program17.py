#list Comprehensions

squares =[]
for x in range(15):
    squares.append(x ** 2)
    
print(squares)
 
# using lambda functions

squares = list(map(lambda x: x ** 2, range(15)))
print(squares) 
 
# another way

squares = [x ** 2 for x in range(15)]
print(squares)
 
 
 # Example
combs =[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
           combs.append((x,y))
print(combs)


#Lc
combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs) 

vc = [-4,-2,0,2,4]
vic = [x * 2 for x in vc]
print(vic)

vic1 = [x for x in vc if x>=0]
print(vic1)

vic2 = [abs(x) for x in vc]
print(vic2)


##
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print([(x, x**2) for x in range(6)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])



## basic way
matrix = [
          [1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          ]

transposed=[]
for i in range(4):
     transposed_row = []
     for row in matrix:
         transposed_row.append(row[i])
     transposed.append(transposed_row)
print(transposed)    


# using For

transposed=[]
for i in range(4):
     transposed.append([row[i] for row in matrix])
print(transposed)

## nested list comprehension

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)




