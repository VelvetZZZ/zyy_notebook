# 🧠 Memoization（记忆化）

## 📌 核心思想
Memoization 是通过缓存之前的结果，来避免重复计算递归函数的技术。
	•	用字典 cache = {} 保存已经计算过的结果。
	•	如果一个输入值之前出现过，直接从 cache 中取结果，不再递归调用。

## ✅ Python 实现模板

```python
def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized
```
## 图解：Memoized Tree Recursion
### 🎬 示例：fib(5) 的递归调用图
本图展示了使用 Memoization 优化后的 Fibonacci 递归过程。
![alt text](image.png)

图例元素          含义
🔵 蓝点        实际进行了递归调用（没有缓存）
🔴 红点        从缓存中获取的值，避免了递归
⚪️ 白点        因为前面已经缓存过，所以这个分支直接 跳过了，没有任何递归调用

## 💡 学习要点总结
✅ 什么时候用 Memoization？
•	当你有重叠子问题（如斐波那契）时，memoization 可以大大减少重复调用。



# ⚡️ 指数运算优化与记忆化理解

## 🎯 问题目标：计算 b^n

---

## ✅ 方法一：朴素递归（线性复杂度）

```python
def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n - 1)
```
•	每次递归都将 n 减 1
•	时间复杂度：O(n)
•	缺点：效率低，调用深度大

## 🚀 方法二：快速幂（Exponentiation by Squaring）
```python
def exp_fast(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n // 2))
    else:
        return b * exp_fast(b, n - 1)

def square(x):
    return x * x
```
•	利用数学性质将指数减半
•	时间复杂度：O(log n)
•	适合大指数幂运算


# 🔢 Order of Growth Notation（增长阶表示法）

---

## 📚 什么是 Order of Growth？

- 用于描述**算法效率随输入规模增长的趋势**
- 常用两种记法：
  - **Θ（Theta）**：准确增长率（tight bound）
  - **O（Big-O）**：上界（最坏情况）

---

## 🎯 判断效率的常见复杂度阶

| 增长类型              | 数学表示     | 举例函数      | 说明                         |
|-----------------------|--------------|---------------|------------------------------|
| 🟢 Constant            | Θ(1) / O(1)  | 字典查找      | 不随输入变化                 |
| 🔵 Logarithmic         | Θ(log n)     | `exp_fast`    | 每次操作减半，增长慢         |
| 🟡 Linear              | Θ(n)         | `exp`         | 输入变大，时间成比例增加     |
| 🟠 Quadratic           | Θ(n²)        | `overlap`     | 两层嵌套循环，增长更快       |
| 🔴 Exponential         | Θ(2ⁿ)        | `fib` 原始递归 | 每多一项调用，翻倍递归       |

---

## 🧠 例子解析

###  🔴 指数增长（Exponential Growth）

```python
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)
```
•	每个 fib(n) 会递归调用 fib(n-1) 和 fib(n-2)
•	会造成大量重复计算
•	时间复杂度：Θ(2ⁿ)

### 🟢 对数增长（Logarithmic Growth）

```python
def exp_fast(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(exp_fast(b, n // 2))
    else:
        return b * exp_fast(b, n - 1)

def square(x):
    return x * x
```
•	如果是偶数指数：只需递归一半 n//2
•	减少了大量重复乘法
•	时间复杂度：Θ(log n)