# 🌳 树状结构数据 (Tree-Structured Data) 学习笔记

树状结构是一种非线性数据结构，由根节点和子节点（分支）组成。学习递归 (Recursion) 的主要原因是为了处理这种天然具有层次结构的数据。

---

## I. 列表 (函数式) 表示法

在 CS 61A 中，树被抽象地表示为一个 Python 列表，约定格式为：
**`[根节点标签, 子树1, 子树2, ...]`**

### 1. 构造函数 (Constructor)

| 函数 | 代码 | 作用 |
| :--- | :--- | :--- |
| `tree` | `def tree(label, branches=[]):` | 创建一棵树。第一个元素是标签，后续元素是子树列表。 |
| - | `return [label] + list(branches)` | 返回遵循约定的列表结构。 |

### 2. 选择器 (Selectors)

选择器用于提取树（列表 `t`）中的特定部分。

| 函数 | 代码 | 作用 |
| :--- | :--- | :--- |
| `label` | `def label(t):` | 返回根节点的值。 |
| - | `return t[0]` | 返回列表的第一个元素。 |
| `branches` | `def branches(t):` | 返回一个包含所有子树的列表。 |
| - | `return t[1:]` | 返回列表中索引 1 之后的所有元素（子树列表）。 |

### 3. 条件判断

| 函数 | 代码 | 作用 |
| :--- | :--- | :--- |
| `is_leaf` | `def is_leaf(t):` | 检查树是否是叶子节点（即没有子树）。 |
| - | `return not branches(t)` | 如果 `branches(t)` 返回空列表 `[]`，则结果为 `True`。 |

---

## II. 类 (面向对象) 表示法

使用 Python 类 `Tree` 来封装树的属性（数据）和方法（操作），提供更清晰和健壮的结构。

### 1. 类定义与初始化

```python
class Tree:
    def __init__(self, label, branches=[]):
        # 属性：存储根节点的值
        self.label = label
        # 属性：存储子树的列表
        self.branches = list(branches)
```

### 2. 方法 (Method)
```python
def is_leaf(self):
        # 方法：检查是否为叶子节点
        return not self.branches
```

## III. 核心知识点：递归与树结构
递归是处理树状数据结构最自然、最优雅的方式。
- *树的递归定义*： 任何一棵树都是由一个根节点和若干个子树构成，而每个子树本身又是一棵完整的树。

递归与树的匹配： 对整个树进行操作（如求和、遍历）时，只需要遵循两个步骤：

    1. 处理根节点（非递归部分）。
    2. 对每个子树进行相同的操作（递归调用）。
因此，学习递归是理解和操作这种层次结构数据（如表达式、文件系统、HTML/XML 结构等）的主要原因。






# CS61A – Solving Tree Problems: `bigs`

## 题目描述

实现函数 `bigs(t)`：

- `t` 是一棵树（Tree），节点标签是整数
- 返回树中 **标签严格大于所有祖先节点标签的节点数量**

---

## 核心思想

对于树中的每一个节点：

> 判断  
> `node.label > max(ancestor labels)`

因此，在递归过程中需要：

- 一直 **携带“祖先中的最大标签”**
- 每往下一层就更新这个最大值

---

## 方法一：通过返回值累加（functional 风格）

```python
def bigs(t):
    def f(a, x):
        if a.label > x:
            return 1 + sum(f(b, a.label) for b in a.branches)
        else:
            return sum(f(b, x) for b in a.branches)

    return f(t, t.label - 1)
```
## 特点

- 使用递归返回值逐层累加答案
- 无副作用（pure function）
- 更偏函数式编程风格

---

## 方法二：使用外部可变变量计数（Imperative 风格）
```python
def bigs(t):
    n = [0]  # 使用列表作为可变计数器

    def f(a, x):
        if a.label > x:
            n[0] += 1

        for b in a.branches:
            f(b, max(a.label, x))

    f(t, t.label - 1)
    return n[0]
```
### 参数说明

- `a`：当前节点（Tree）
- `x`：当前节点所有祖先中的最大 label

---

### 为什么使用 `n = [0]` 而不是 `n = 0`？

- Python 不允许在内层函数中直接修改外层作用域中的不可变变量（如 `int`）
- 列表是可变对象（mutable）
- 通过修改 `n[0]`，可以在递归过程中安全地累加计数

---

### 为什么对子节点传入 `max(a.label, x)`？

对于子节点来说：

- 其祖先集合 = 原祖先 + 当前节点
- 祖先中的最大 label 应更新为：

```python
max(a.label, x)
```

### 根节点的初始化方式
```python
f(t, t.label - 1)
```
原因：
	•	根节点没有祖先
	•	传入一个比根节点 label 小的值
	•	保证根节点一定满足 a.label > x，从而被计数

⸻

## 两种方法的对比

| 方法         | 特点                   |
|--------------|------------------------|
| 返回值累加   | 无副作用，更偏函数式   |
| 外部计数器   | 逻辑直观，命令式风格   |
