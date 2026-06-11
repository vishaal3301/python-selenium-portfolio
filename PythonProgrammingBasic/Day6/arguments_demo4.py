def my_func(a,b,c):
    print(f"a={a},\tb={b},\tc={c}")

my_func(10,20,30) # Positional Arguments
my_func(a=10,b=20,c=30) # Keyword Arguments
my_func(c=30,a=10,b=20)
my_func(10,20,c=40) # Combination of Keyword Argument and Positional Arguments
my_func(10,b=10.5,c=78) # Combination of Keyword Argument and Positional Arguments
# my_func(11,b=22,33)my_func # It is a Syntax Error
# my_func(11,22,b=33) # It is Logical Error
my_func(11,22,c=33) # Positional Argument is appear before Keyword Arguments

"""Positional Argument must appear before any Keyword Argument"""
