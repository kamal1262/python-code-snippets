def fibonacchi(n):
    if n<=1:
        return 1
    else:
        return fibonacchi(n-2)+fibonacchi(n-1)

def factorial (n):
    if n == 0: 
        return 1
    else:
        return n * factorial(n-1)


# fibonacchi(0)
# fibonacchi(10)

# factorial(0)
# factorial(1)