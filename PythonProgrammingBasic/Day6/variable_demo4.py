def foo():
    global x
    x = 700
    print(f"Inside foo, x = {x}")

foo()
print(f"Outside foo, x = {x}")