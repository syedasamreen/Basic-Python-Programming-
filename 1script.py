num = 0
count = 0
sum = 0

while num>=0:
     num = int(input("enter any number ..-1 to exit:"))
     if num >=0:
        count = count +1
        sum = sum +num
avg = sum/count
print('total numbers: ',count, ', Average: ',avg)
