# 学习笔记：迭代器 (Iterators) in Python

## 1. 定义与目的

* **迭代器 (Iterator)**：一个对象，代表一个数据流。它允许程序员逐个访问集合中的元素，而无需暴露该集合的底层表示。迭代器一次返回一个数据元素。
* **作用**：提供一种统一的、按顺序访问集合（如列表、字符串等容器）中元素的方法。
* **核心特性**：
    * **有状态 (Stateful)**：迭代器会记住当前遍历到了哪个位置。
    * **按需获取 (Lazy Evaluation)**：只有在请求时才返回下一个元素。

## 2. 核心内置函数

### a. `iter(iterable)`

* **输入 (Argument)**：一个 **可迭代对象 (iterable)**。
    * **可迭代对象 (Iterable)**：任何可以被逐个访问其组成部分的对象。它们通常实现了 `__iter__()` 特殊方法。
    * 常见例子：列表 (`list`)、元组 (`tuple`)、字符串 (`str`)、字典 (`dict`)（遍历键、值或项）、集合 (`set`)、文件对象等。
* **输出 (Return Value)**：一个与该可迭代对象关联的 **迭代器 (iterator)** 对象。
* **功能**：为可迭代对象创建一个新的迭代器实例。

### b. `next(iterator)`

* **输入 (Argument)**：一个 **迭代器 (iterator)** 对象（由 `iter()` 函数返回）。
* **输出 (Return Value)**：迭代器指向的序列中的 **下一个元素**。
* **副作用 (Side Effect)**：调用后，迭代器的内部状态会更新，使其指向序列中的再下一个元素，为下一次调用 `next()` 做准备。
* **`StopIteration` 异常**：
    * 当迭代器中没有更多元素可供返回时（即已到达序列末尾），再次调用 `next()` 会引发 `StopIteration` 异常。
    * 这个异常是迭代协议的一部分，通常被 `for` 循环用来自动侦测并结束循环。

## 3. 关键行为与特性

* **一次性使用 (Single Pass)**：
    * 标准的迭代器通常只能完整地从头到尾遍历其关联的数据序列一次。
    * 一旦所有元素都被访问过（即 `next()` 已引发 `StopIteration`），该迭代器就被认为是“耗尽 (exhausted)”了。
    * 若要重新从头遍历，必须从原始的可迭代对象重新获取一个新的迭代器实例（即再次调用 `iter()` 函数）。

* **独立性 (Independence)**：
    * 对同一个可迭代对象多次调用 `iter()` 函数会产生多个独立的迭代器实例。
    * 每个迭代器都维护其自身的遍历状态（当前位置）。
    * 一个迭代器的 `next()` 操作不会影响其他独立迭代器的状态。
    * *PPT 示例说明*：
        ```python
        s = [3, 4, 5]
        t = iter(s)  # 迭代器 t
        u = iter(s)  # 迭代器 u，独立于 t
        next(t)  # 返回 3 (t 指向 4)
        next(u)  # 返回 3 (u 指向 4)
        next(t)  # 返回 4 (t 指向 5)
        next(u)  # 返回 4 (u 指向 5)
        ```

* **惰性求值 / 延迟加载 (Lazy Evaluation)**：
    * 元素仅在调用 `next()` 时才被实际获取或（在某些情况下，如生成器）计算出来。
    * 这对于处理非常大的数据集或概念上的无限序列非常高效，因为它显著降低了内存消耗，避免了一次性加载所有数据。

## 4. 与 `for` 循环的紧密关系

* `for` 循环是 Python 中使用迭代器最自然、最常见也是推荐的方式。
* 当我们写下如下 `for` 循环时：
    ```python
    my_iterable = [10, 20, 30]
    for item in my_iterable:
        print(item)
    ```
* Python 在幕后大致会执行以下操作：
    1.  **获取迭代器**：调用 `temp_iterator = iter(my_iterable)` 来获取与 `my_iterable` 关联的迭代器。
    2.  **循环调用 `next()`**：进入一个内部循环，重复以下步骤：
        a.  尝试调用 `item = next(temp_iterator)` 来获取下一个元素。
        b.  **执行循环体**：如果成功获取到 `item`，则执行 `for` 循环体内的代码（在此例中是 `print(item)`）。
        c.  **处理 `StopIteration`**：如果调用 `next(temp_iterator)` 时引发了 `StopIteration` 异常，表明序列中已无更多元素，Python 会捕获此异常并优雅地终止 `for` 循环。

## 5. 示例回顾

```python
# 原始数据 (可迭代对象)
data_list = ['apple', 'banana', 'cherry']

# 获取第一个迭代器
iterator1 = iter(data_list)
print(f"Iterator 1, 1st next: {next(iterator1)}")  # 输出: apple
print(f"Iterator 1, 2nd next: {next(iterator1)}")  # 输出: banana

# 获取第二个、独立的迭代器
iterator2 = iter(data_list)
print(f"Iterator 2, 1st next: {next(iterator2)}")  # 输出: apple (iterator2 从头开始)

# 继续使用第一个迭代器
print(f"Iterator 1, 3rd next: {next(iterator1)}")  # 输出: cherry (iterator1 继续它之前的进度)

# 尝试再次调用 next() 在耗尽的迭代器上 (iterator1)
# try:
#     next(iterator1)
# except StopIteration:
#     print("Iterator 1 is exhausted!") # 会打印这句

# 使用 for 循环 (更简洁的方式)
print("\nUsing a for loop:")
for fruit in data_list: # 内部自动处理 iter() 和 next()
    print(fruit)
