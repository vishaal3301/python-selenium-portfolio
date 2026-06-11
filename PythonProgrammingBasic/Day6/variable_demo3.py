ab = 100
def fun_var():
    global ab
    print(f"global ab inside the function: {ab}")
    ab = 200
    print(f"Global ab reassign inside the function: {ab} ")

fun_var()
print(f"global ab outside the function: {ab}")