tpl = ()
print(tpl)

 
mytpl = ("jeff", "bill", "steve","mohan")
print(mytpl)

nums = (1,2,3,4,5)
print(nums)

employee = (1,'sam', True, 25, 12000)
print(employee)


mytpl = "jeff", "bill", "steve","mohan"
print(mytpl)

nums = 1,2,3,4,5
print(nums)

employee =1,'sam', True, 25, 12000
print(employee)

print(type(mytpl))

print(mytpl[0])
print(mytpl[1])
print(mytpl[2])
print(mytpl[-1])



a,b,c,d,e = employee
print(a,b,c,d,e)

print(type(employee))

stpl = tuple('hello sam')
print(stpl)


dtpl = tuple({1:'one',2:'two'})
print(dtpl)

nums = tuple({100,200,300})
print(nums)

ltpl = tuple([1,2,3,4])
print(ltpl)

print(ltpl + (5,))
