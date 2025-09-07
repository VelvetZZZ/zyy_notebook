#Measuring Efficiency 测量效率
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)
    
def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted
fib = count(fib)
print(fib(5))
print(fib.call_count)
print(fib(5))
print(fib.call_count)
print(fib(30))
print(fib.call_count)

#Memoization 记忆化