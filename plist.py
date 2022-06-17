mylist = []
print(mylist)
mylist1 = ["jeff", "bill", "steve","mohan"]
print(mylist1)

item = [1,"sam", "DS", 12.50, True]
print(item)
print(mylist1[0])
print(mylist1[1])
print(mylist1[2])
print(mylist1[3])
print(mylist1[-1])
print(mylist1[-2])
print(mylist1[-3])
print(mylist1[-4])


print(item[:])
print(item[:0]);print(item[:2])
print(item[0:]);print(item[1:])


mlist = [1,2,3,[4,5,6,[7,8,[9]]],10]
print(mlist[0])
print(mlist[1])
print(mlist[2])
print(mlist[3])
print(mlist[4])
print(mlist[3][0])
print(mlist[3][3])
print(mlist[3][3][0])
print(mlist[3][3][2])


# list class

nums = [1,2,3,4,5,6]
print(type(nums))

slist = list('hello sam')
print(slist)
print(str(slist))

dlist = list({1:'one',2:'two'})
print(dlist)

nums = list({100,200,300})
print(nums)

tlist = list((1,2,3,4))
print(tlist)



#iteration of list

mylist1 = ["jeff", "bill", "steve","mohan"]
for name in mylist1:
    print(name)
    
    
mylist1[0] = "sam"
mylist1[1] = "vig"
mylist1.insert(2,"SCience")
mylist1.append("VMWARE")
print(mylist1)

