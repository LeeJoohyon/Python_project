level = 0
def outter():
    level = 50

     def inner():
        nonlocal level
        level += 3
        print(level)
     return inner

 func = outter()
 print(func)
