def basic_operations(a, b):
    return {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b
    }

print(basic_operations(15, 5))
def power_operation(base, exponent, **kwargs):
    result = base ** exponent  # Calculate power operation
    
    if 'modulo' in kwargs:
        modulo = kwargs['modulo']
        result = result % modulo  # Calculate modulo if provided
    
    return result

print(power_operation(2, 3))  # Output: 8
print(power_operation(2, 3, modulo=5))  # Output: 3


def basic_operations(a, b):
    try:
        add = a + b 
        sub = a - b
        mul = a * b
        div = a / b
        return add, sub, mul, div
    except ZeroDivisionError:
        print("Division by zero error")
        return None
    except TypeError:
        print("please enter numbers only")
        return None

def power_operation(base, exponent, **kwargs):
    try:
        result = base ** exponent  # Calculate power operation
        
        if 'modulo' in kwargs:
            modulo = kwargs['modulo']
            result = result % modulo  # Calculate modulo if provided
        
        return result
    except Exception as e:
        print("Error:", str(e))
        return None

def apply_operations(operation_list):
    try:
        return list(map(lambda x: x[0](*x[1]), operation_list))
    except Exception as e:
        print("Error:", str(e))
        return None

try:
    # Test basic_operations
    result_basic = basic_operations(10," k")
    print("Basic Operations Result:", result_basic)
except NameError:
    print("Error: Variable 'k' is not defined")
except TypeError as te:
    print("Error:", str(te))

try:
    # Test power_operation
    result_power = power_operation(2, 3)
    print("Power Operation Result:", result_power)
except TypeError as te:
    print("both base and exponent must be integers")

try:
    # Test power_operation with modulo
    result_power_modulo = power_operation(2, 3, modulo=5)
    print("Power Operation with Modulo Result:", result_power_modulo)
except TypeError as te:
    print("both base and exponent must be integers")

try:
    # Test apply_operations
    operations = [
        (lambda x, y: x + y, (3, 4)),
        (lambda x, y: x * y, (2, 5)),
    ]

    result_apply = apply_operations(operations)
    print("Apply Operations Result:", result_apply)
except TypeError as te:
     print("both base and exponent must be integers")
