# Return two values
# Function can return the multiple values.
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(f"largest Value is : {largest(100,200)}")
print(f"largest Value is : {largest(300,200)}")


result = largest(786,586)
print(f"{result}")
print(type(result))