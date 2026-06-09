ab = 100
def fun_var():
    global ab
    ab = 200
    print(ab)

fun_var()
print(f"global ab: {ab}")