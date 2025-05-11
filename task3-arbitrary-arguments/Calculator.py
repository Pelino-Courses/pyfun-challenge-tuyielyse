def validate_numbers(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"Invalid input:{arg} is not a number") 
        
def calculate(*args, **kwargs):
    validate_numbers(*args)
    Operations = {
    'add':kwargs.get('add', False),
    'multiply':kwargs.get('multiply', False),
    'subtract':kwargs.get('subtract', False),
    'divide':kwargs.get('divide', False)
    }
    # Ensure only one operation is selected
    if sum(Operations.values())  !=1:
        raise ValueError("you must specify exactly one operation (add,multiply, subtract, divide)")
    if not args:
        raise ValueError("please input atleast one number.")
    if Operations['add']:
        return sum(args)
    
    if Operations['multiply']:
        result = 1 
        for num in args: 
            result*=num
        return result
    
    if Operations['subtract']:
        result = args[0]
        for num in args [1:]:
            result -= num 
        return result
    
    if Operations['divide']:
        result = args[0]
        for num in args [1:]:
            if num == 0 :
               raise ZeroDivisionError("Division by zero is not allowed")
        result /= num
    return result

print(f"Sum = {calculate(5,6,45, add=True)}")
print(f"Product = {calculate(5,9, multiply=True)}")
print(f"Difference = {calculate(8, 5, subtract=True)}")
print(f"Quotient = {calculate(50,2, divide=True)}")
    