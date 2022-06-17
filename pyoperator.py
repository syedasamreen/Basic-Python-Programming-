import operator

#Arithemetic operator
print(operator.add(5,6))
print(operator.__add__(5,6))

print(operator.sub(10,6))
print(operator.__sub__(5,6))

print(operator.mul(5,6))
print(operator.__mul__(5,6))


print(operator.pow(5,6))
print(operator.__pow__(5,6))

print(operator.truediv(5,6))
print(operator.__truediv__(5,6))

print(operator.floordiv(5,6))
print(operator.__floordiv__(5,6))

print(operator.mod(5,6))
print(operator.__mod__(5,6))


#assignment operator

print(operator.iadd(5,6))   # +=
print(operator.__iadd__(5,6))

print(operator.isub(5,6)) # -=
print(operator.__isub__(5,6))

print(operator.imul(5,6))  # *=
print(operator.__imul__(5,6))

print(operator.itruediv(5,6))   # /=
print(operator.__itruediv__(5,6))

print(operator.ifloordiv(5,6))  # //=
print(operator.__ifloordiv__(5,6))

print(operator.imod(5,6)) #  %=
print(operator.__imod__(5,6))

print(operator.iand(5,6)) # &=
print(operator.__iand__(5,6))

print(operator.ior(5,6)) #|=
print(operator.__ior__(5,6))

print(operator.ixor(5,6)) # ^=
print(operator.__ixor__(5,6))

print(operator.irshift(5,6)) # >>=
print(operator.__irshift__(5,6))

print(operator.ilshift(5,6)) # <<=
print(operator.__ilshift__(5,6))

### comparision operator

print(operator.gt(5,6)) # >
print(operator.gt(6,5))

print(operator.lt(5,6))
print(operator.lt(6,5)) #<

print(operator.eq(5,6)) # ==
print(operator.eq(1,1))

print(operator.ne(1,1)) # !=
print(operator.eq(1,2))

print(operator.ge(5,6)) # >=
print(operator.ge(6,4))

print(operator.le(7,8)) #<=
print(operator.le(1,1))

#idendtity operator

print(operator.is_(5,6))
print(operator.is_not(5,6))

# membership operator
#print(operator.contains(5,6))
nms = [1,2,3,4,5,6]
#print(not operator.contains(nms,7))

# bitwise operator

print(operator.and_(5,10))

print(operator.or_(5,10))

print(operator.xor(5,10))

print(operator.invert(5))


print(operator.lshift(5,10))

print(operator.rshift(5,10))
