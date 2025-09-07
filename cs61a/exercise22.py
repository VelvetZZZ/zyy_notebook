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
def memo(f):
    cache = {}  # 🗂️ 创建缓存字典，key 是参数，value 是返回值

    def memoized(n):
        if n not in cache:             # ❓ 如果没算过 n
            cache[n] = f(n)            # ✅ 计算并保存结果
        return cache[n]                # 🚀 返回缓存结果
    
    return memoized  # 返回“带缓存功能”的函数
fib = memo(fib)
print(fib(30))
print(fib(300))



def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


fib = count(fib)#count(f) 是用来包装一个函数，让它具有 call_count 属性，用于统计被调用的次数。
fib = memo(fib)     # 先加缓存（返回一个新的函数）
fib = count(fib)    # 再包装这个函数，加上 call_count 属性
print(fib(30))
print(fib.call_count)
