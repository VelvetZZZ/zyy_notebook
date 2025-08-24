# Generators 生成器  and Generator Functions

## 1. 什么是 Generator Function？
- **普通函数 (normal function)**：调用后执行，遇到 `return` 结束，只会返回一次结果。
- **生成器函数 (generator function)**：调用后不会立即执行，而是返回一个 **生成器对象 (generator)**。
  - 使用 `yield` 关键字返回值。
  - 可以多次 `yield`，每次生成一个值。
  - 每次执行会“暂停”在 `yield`，下次继续从上次中断处运行。

---

## 2. 示例代码

```python
def plus_minus(x):
    yield x      # 第一次产出正数
    yield -x     # 第二次产出负数

t = plus_minus(3)   # 创建一个生成器对象
next(t)             # 运行到第一个 yield，返回 3
next(t)             # 从上次中断继续，返回 -3
t                   # 此时 t 仍是生成器对象

# `yield from` 与生成器迭代

## 1. `yield from` 的作用
- 普通的 `yield`：一次返回一个值，需要手动写循环去遍历另一个可迭代对象。
- `yield from <iterable>`：会把 **整个可迭代对象** 中的所有值依次产出，等价于在循环里多次写 `yield`。

👉 简化了代码书写，让生成器函数更简洁。

## 2. 示例 1：合并两个序列

### 普通写法
```python
def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x

list(a_then_b([3, 4], [5, 6]))
# [3, 4, 5, 6]
```


这里觉得难的可以复习下 Lecture 10 的 inverse_cascade 函数


# 🎯 Partitions 整数分拆 —— 使用列表 vs 使用生成器

## ✅ 1. 两种实现方式的区别（列表 vs 生成器）

- **列表函数（return list）**：调用函数时，立刻计算**所有结果**，一次性返回整个列表。
- **生成器函数（generator function）**：使用 `yield`，每次产生一个结果，调用不会立即计算，返回的是一个 **生成器对象（generator）**。

---

## 🧪 2. 示例代码对比

### 📦 使用列表的版本（适合小问题，初学者容易理解）

```python
def partitions(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in partitions(n - m, m)]
        without_m = partitions(n, m - 1)
        return exact_match + with_m + without_m

for p in partitions(6, 4):
    print(p)
✅ 优点：
	•	简单直观，适合初学者入门。
	•	一次性生成所有结果，后续处理（如统计、筛选）方便。
	•	返回的是标准列表 list，可以多次遍历和使用。

❌ 缺点：
	•	所有结果必须一次性算出，内存占用大。
	•	对于组合非常多的情况，性能低、运行慢。
	•	无法只取部分结果，不能“按需取值”。

⚡ 使用生成器函数版本（yield）
def partitions(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n - m, m):
            yield p + ' + ' + str(m)
        yield from partitions(n, m - 1)
t = partitions(6, 4)     # 创建生成器对象
next(t)                  # 获取第一个结果
next(t)                  # 获取第二个结果
for x in t:              # 遍历剩下的结果
    print(x)

✅ 优点：
	•	每次只生成一个结果，按需计算，节省内存。
	•	支持 next() 逐步获取结果，适合大规模问题。
	•	执行效率高，不需等待所有结果生成完。
	•	生成器函数会在 yield 处暂停，下次再继续运行（可暂停+恢复）。

❌ 缺点：
	•	初学者需要理解 yield 的暂停机制，较难调试。
	•	返回的是生成器对象，只能遍历一次，不能重复使用。

📊 3. 总结对比表格
特性            列表函数（return）    生成器函数（yield）
返回值类型        list                generator
是否立即计算全部    ✅ 是                ❌ 否（懒加载）
内存占用           高                  非常低
是否可部分获取      ❌ 不可以            ✅可使用 next()
可否暂停继续执行    ❌ 否               ✅是（yield 暂停）
可否重复遍历       ✅ 可以              ❌ 不可以（一次性迭代）
调试/查看结果方便性 ✅ 更容易             ❌ 需要理解生成器机制
适合组合少问题      ✅ 是                ✅ 也可以
适合组合爆炸问题   ❌ 容易卡顿或内存爆炸    ✅ 非常适合


🧠 小结记忆法
	•	✅ “结果不多，就用 list（return）”
	•	✅ “结果很多，只取一部分 → 用 generator（yield）”
	•	✅ “yield = 懒加载 + 节省内存 + 高效迭代”
	•	✅ “生成器函数像是会暂停的函数，每次执行到 yield 就暂停，next 再继续”
