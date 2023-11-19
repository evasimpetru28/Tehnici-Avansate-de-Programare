def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 10
f = fibonacci(n)
print(f"fib({n}) = {f}")

###########

fib = [0] * (n + 1)
fib[1] = 1
for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]

print(fib)
