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


    
 2. 字典 (Dictionary) 与迭代

### a. 字典的“视图 (Views)”
字典提供了几种方法来获取其内容的特定“视图”，这些视图本身也是可迭代的，并且动态反映底层字典的变化。

* **`my_dict.keys()`**: 返回一个包含字典所有**键**的视图对象。
* **`my_dict.values()`**: 返回一个包含字典所有**值**的视图对象。
* **`my_dict.items()`**: 返回一个包含字典所有**项（键值对）**的视图对象。每个“项”通常是一个 `(key, value)` 形式的元组。
* **直接迭代字典 (`for k in my_dict:`)**: 默认情况下，直接迭代一个字典等同于迭代其**键** (`my_dict.keys()`)。

### b. 字典元素的迭代顺序
* **Python 3.6+**: 字典会**保持元素的插入顺序**。因此，遍历字典的键、值或项时，元素的顺序与它们被添加到字典中的顺序一致。
* **Python 3.5 及更早版本**: 字典是无序的，迭代顺序不确定。

### c. 使用迭代器遍历字典视图 (示例)
```python
d = {'one': 1, 'two': 2}
d['zero'] = 0 # d 现在是 {'one': 1, 'two': 2, 'zero': 0} (按插入顺序)

# 遍历键
k_iter = iter(d.keys()) # 或 iter(d)
# next(k_iter) -> 'one', next(k_iter) -> 'two', next(k_iter) -> 'zero'

# 遍历值
v_iter = iter(d.values())
# next(v_iter) -> 1, next(v_iter) -> 2, next(v_iter) -> 0

# 遍历项
i_iter = iter(d.items())
# next(i_iter) -> ('one', 1), next(i_iter) -> ('two', 2), next(i_iter) -> ('zero', 0)




# Python 迭代内建函数学习笔记

本笔记总结了 Python 中用于高效迭代的关键内建函数，重点解释了它们的工作方式和使用场景。

## 核心概念

* **可迭代对象 (Iterable):** 一个能够一次返回一个其成员的对象。例如：列表 (`[]`)、元组 (`()`)、字符串 (`""`)、字典 (`{}`)、集合 (`{}`)、`range()` 对象。
* **迭代器 (Iterator):** 代表数据流的对象。它通过 `next()` 方法一次返回一个元素。迭代器是“惰性的”并且是有状态的（它们会记住当前的位置）。
    * **惰性计算 (Lazy Evaluation):** 仅在被请求时才计算值，从而节省内存和处理时间。
    * **一次性使用:** 一旦迭代器的所有元素都被检索完毕（即迭代器被耗尽），它就不能被重置或重用。你需要从原始的可迭代对象重新创建一个新的迭代器。
* **`func` (作为参数的函数):** 许多迭代函数接受另一个函数作为参数，这个函数会被应用于可迭代对象的元素上。这可以是一个预先定义的函数，也可以是一个 `lambda` 函数。

## 返回迭代器的函数

这些函数执行操作并返回一个迭代器，该迭代器会惰性地生成结果。

1.  **`map(function, iterable, ...)`**
    * **用途：** 将 `function` 应用于 `iterable` 的每个元素，并返回一个包含这些结果的迭代器。
    * **语法：** `map(我的函数, 我的列表)`
    * **示例：**
        ```python
        numbers = [1, 2, 3]
        # 为简单起见，使用 lambda 函数
        squared_iterator = map(lambda x: x**2, numbers)
        # print(list(squared_iterator)) # 输出: [1, 4, 9]
        ```

2.  **`filter(function, iterable)`**
    * **用途：** 从 `iterable` 的元素中构造一个迭代器，这些元素使得 `function` 返回 `True`。
    * **语法：** `filter(我的布尔函数, 我的列表)`
    * **示例：**
        ```python
        ages = [12, 18, 25, 30]
        adults_iterator = filter(lambda x: x >= 18, ages)
        # print(list(adults_iterator)) # 输出: [18, 25, 30]
        ```

3.  **`zip(*iterables)`**
    * **用途：** 聚合来自每个可迭代对象的元素。返回一个元组的迭代器，其中第 i 个元组包含来自每个参数可迭代对象的第 i 个元素。
    * **停止条件：** 当最短的输入可迭代对象耗尽时，迭代停止。
    * **语法：** `zip(可迭代对象1, 可迭代对象2, ...)`
    * **示例：**
        ```python
        names = ['爱丽丝', '鲍勃']
        scores = [90, 85]
        zipped_iterator = zip(names, scores)
        # print(list(zipped_iterator)) # 输出: [('爱丽丝', 90), ('鲍勃', 85)]
        ```

4.  **`reversed(sequence)`**
    * **用途：** 返回一个反向迭代器。
    * **`sequence` (序列)：** 必须是一个具有 `__reversed__()` 方法或支持序列协议（`__len__()` 方法和 `__getitem__()` 方法）的对象。常见的序列有列表、元组、字符串和范围 (range)。
    * **语法：** `reversed(我的序列)`
    * **示例：**
        ```python
        my_string = "abc"
        reversed_char_iterator = reversed(my_string)
        # print(list(reversed_char_iterator)) # 输出: ['c', 'b', 'a']
        ```

## 消耗迭代器/创建集合的函数

这些函数接受一个可迭代对象（可以是迭代器）作为输入，并通常返回一个新的集合（如列表、元组），从而在此过程中“消耗”掉迭代器。

1.  **`list(iterable)`**
    * **用途：** 从可迭代对象的元素创建一个列表。
    * **示例：** `my_list = list(map(str, [1, 2, 3])) # 得到 ['1', '2', '3']`

2.  **`tuple(iterable)`**
    * **用途：** 从可迭代对象的元素创建一个元组。
    * **示例：** `my_tuple = tuple(filter(lambda x: x > 0, [-1, 0, 1])) # 得到 (1,)`

3.  **`sorted(iterable, *, key=None, reverse=False)`**
    * **用途：** 从 `iterable` 中的元素返回一个新的已排序的**列表**。
    * **`key` (可选参数)：** 一个在进行比较之前对每个元素调用的函数。
    * **`reverse` (可选参数)：** 如果为 `True`，则按降序排序。
    * **示例：**
        ```python
        numbers = [3, 1, 4, 1, 5, 9]
        sorted_numbers = sorted(numbers) # 结果: [1, 1, 3, 4, 5, 9]
        desc_sorted_numbers = sorted(numbers, reverse=True) # 结果: [9, 5, 4, 3, 1, 1]
        ```

## “惰性计算”的重要性

* **内存效率：** 计算是按需进行的，因此无需一次将所有结果存储在内存中。这对于大型或潜在无限的数据流至关重要。
* **性能：** 如果并非所有结果都需要，则避免了不必要的计算。
