"""Global and Local Variables
Global Variables: The Variables created outside of functions are called as Global Variables.
Local Variables: The Variables created inside the functions are called as Local Variables."""

global_var = 20 # This is a Global Variable

def function_variable():
    local_var = 70 #This is local variable because it is inside the function.
    print(f"local_var: {local_var}")
    print(f"global_var: {global_var}")
function_variable()

print(f"global_var: {global_var}")
# print(f"local_var: {local_var}") it will give an error as Local Variable can NOT access outside the function.
