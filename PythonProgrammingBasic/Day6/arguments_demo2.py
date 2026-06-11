# Default values to Positional Arguments
def add(i,j=10):
     print(f"add(i = {i},j = {j}) -> add({i},{j}) = {i+j}")

add(20)
add(200,300)
add(j=1.5,i=2.5)