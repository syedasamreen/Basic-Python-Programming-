# search of prime numbers
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
           print(n , 'equals', x, '*', n//x)
           break
    else:
         print(n, 'is prime number')
# continue
for num in range(2,10):
     if num % 2 == 0:
         print("Found an even number", num)
         continue
     print("Found on odd number", num)
     

