#  Multiple except blocks to handle different types of exceptions -> try,except, else and finally blocks

try:
    num1,num2 = 10,5
    result =  num1/num2
    print(f'result is: {result}')

except ZeroDivisionError:
    print(f'ZeroException exception occured')
except SyntaxError:
    print(f'Syntax error exception occured')
except:
    print(f'Exception handled')
else:
    print(f'Inside else block, No exception occured')
finally:
    print(f'Inside finally block, which always executes whether exceptoin occured or NOT ')
