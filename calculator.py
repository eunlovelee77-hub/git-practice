def add(a,b):
  return a+b
def multiply(a, b):
    return a * b
def substract(a,b):
    return a-b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
print(add(10,5))
print(substract(10,5))
print(divide(10, 2))