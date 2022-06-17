num =0
while num <20:
    num = num+2
    print('num =', num)
    
while num <30:
    num = num+2
    print('num =', num)
    
    
    
##

k = 0

while k < 5:
    k += 1   # num += 1 is same as num = num + 1
    print('k = ', k)
    if k == 3: # condition before exiting a loop
        break
        
##        
j = 0

while j < 5:
	j += 1   # num += 1 is same as num = num + 1
	if j > 3: # condition before exiting a loop
		continue
	print('j = ', j)   
	
	
##
num = 0

while num < 3:
	num += 1   # num += 1 is same as num = num + 1
	print('num = ', num)
else:
    print('else block executed')   
    
    
## 
numbers = [10, 20, 30, 40, 50]

for i in numbers:
    print(i,end=',')
    
    
    
##
for char in 'Hello':
    print (char)
    
##

numNames = { 1:'One', 2: 'Two', 3: 'Three'}

for pair in numNames.items():
    print(pair)
    
##
for i in range(5):
    print(i)
    
##
for i in range(1, 5):
    if i > 2:
        break
    print(i)
    
##
for i in range(1, 5):
    if i > 3:
        continue
    print(i)
    
##
for i in range(2):
    print(i)
else:
     print('End of for loop')
     
for x in range(1,4):
    for y in range(1,3):
        print('x = ', x, ', y = ', y) 
