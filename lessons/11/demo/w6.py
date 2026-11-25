def double(value):
    return value * 2

def apply(value, operation):
    return operation(value)

print(apply(4, double))
