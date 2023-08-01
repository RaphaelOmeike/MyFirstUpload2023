
def FibonacciSequence(n :int):
    if n <= 2:
        return 1
    return FibonacciSequence(n - 1) + FibonacciSequence(n - 2)
print(FibonacciSequence(6))
 
def Factorial(n :int):
    if n <= 1:
        return 1
    return n * Factorial(n - 1)
print(Factorial(7))
