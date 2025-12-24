
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a+b
operations_dict={
    '+':add,
    '-':substract,
    '*':multiplication,
    '/':division
    }
def calculator():
    continue_flag=True
    number1=int(input("enter the 1st number:"))
    for keys in operations_dict:
        print(keys)
    continue_flag=True
    while continue_flag:
        op_symbol=input("enter the operation:")
        number2=int(input("enter next number:"))
        calculator_function=operations_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2 } = {output}")
        
        should_continue=input("enter 'Y' to continue with the output 'n' to start a new calculation 'x' to exit ")
        if should_continue=='y':
            number1=output
        elif should_continue=='n':
            continue_flag=False
            
            calculator()  
        elif should_continue=='x':
            continue_flag=False
            print("BYE!")
calculator()