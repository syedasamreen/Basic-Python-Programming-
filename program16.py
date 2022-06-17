# Data structure
fruits = ['orange','apple','papaya','pomegranet','banana','grapes','mango']
print(fruits.count('apple'))
print(fruits.index('banana'))
print(fruits.count('apple'))
print(fruits.reverse())
print(fruits.append('kiwi'))
print(fruits.sort())
print(fruits.pop())


#using list as stacks

stack = [3,4,5,6]
print(stack.append(7))
print(stack.append(8))
print(stack.pop())
print(stack)


# queues in list

from collections import deque
queue = deque(['eric','sam','lab'])
print(queue.append('john'))
print(queue)
print(queue.popleft())
print(queue)


