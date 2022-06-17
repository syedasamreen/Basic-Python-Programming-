def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
           
def foo(name, /, **kwds):
    return 'name' in kwds
foo(1, **{'name': 2})


# lambda function
def make_incrementor(n):
     return lambda x: x + n
f = make_incrementor(42)
f(0)
