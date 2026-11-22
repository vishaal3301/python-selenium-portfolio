print(f"Starting of the program")
print(f"Program is in progress")
try:
    print(100/0)
except ZeroDivisionError:
    print(f'Exception has occured and Handled')
print(f'After divide by zero')
print(f"Program has completed")