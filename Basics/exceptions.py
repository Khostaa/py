# Errors happen in program which we need to handle in clean way

#Exceptions provide a way of catching erros and then handling them 

try:
    x = 10/0
except:
    print("Well that didn't work")

#You can catch specific exceptions
try: 
    answer = input("what should I divide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
except ValueError as e:
    print("You didn't give me a valid number")
    print(e)
finally:
    print("This code always run")