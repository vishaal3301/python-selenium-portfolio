# Multiple except blocks to handle different types of exceptions -> try,except, else and finally blocks
print(f"Starting of the program")
try:
    print(100/0)
except ZeroDivisionError:
    print(f'ZeroDivisionError has occured and Handled')
except ValueError:
    print(f'ValueError has occured and Handled')
except Exception as e:
    print(f'Unexpected error occurred: {e}')