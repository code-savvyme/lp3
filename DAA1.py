# Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Example
n = int(input("Enter a number: "))
print("Fibonacci (recursive) =", fib_recursive(n))
# TC = O(2^n)
# SC = O(n)


# Non-recursive (Iterative) Fibonacci
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b

# Example
n = int(input("Enter a number: "))
print("Fibonacci (iterative) =", fib_iterative(n))
# TC => O(n)
# SC => O(1)
