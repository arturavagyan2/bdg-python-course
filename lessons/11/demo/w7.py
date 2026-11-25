def apply(value, operation):
    return operation(value)

print(apply(4, lambda value: value + 3))
print(apply(4, lambda value: value * 2))
