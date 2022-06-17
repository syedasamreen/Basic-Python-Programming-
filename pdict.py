capitals = {"usa":"washington D.C", "France":"paris","india":"new delhi"}
print(capitals)


for key in capitals:
    print("key = " +key + ",  value =" + capitals[key])
    
capitals['india']= "DELHI"
capitals['usa'] = "washington"
print(capitals)


numNames = {1:"One", 2:"Two", 3:"Three", 2:"Two", 1:"One"}
print(numNames)
print(type(numNames))

emptydict = dict()
print(emptydict)
emptydict

numdict = dict(I='one', II='two', III='three')
print(numdict)


print(numdict.keys())
print(numdict.values())


d1={"name":"Steve","age":25, "marks":60}
d2={"name":"Anil","age":23, "marks":75}
d3={"name":"Asha", "age":20, "marks":70}
students={1:d1, 2:d2, 3:d3}
print(students)


