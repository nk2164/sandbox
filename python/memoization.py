memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        memo[n] = result
        return result

print (fibonacci(10))
