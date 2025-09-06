# 🧷 Linked List 链表结构

在数据结构中，**链表（Linked List）** 是一种非常基础但强大的结构，它通过递归的方式组织数据，使得插入和删除操作比数组更高效。

---

## 🧠 为什么学习链表很重要？

- 支持动态增长：不需要预先指定长度；
- 插入删除高效：无需移动其他元素；
- 与递归天然契合：结构递归，处理递归；
- 是栈、队列、树、图等高级结构的基础。

---

## 🧱 链表的定义结构

> A linked list is either **empty** or a **first value** and the **rest of the list**.

| 字段名     | 描述说明                     |
|------------|------------------------------|
| `first`    | 当前节点的值                 |
| `rest`     | 剩余的链表部分（Link或empty）|

链表中的每个节点都是 `Link` 类的一个实例。它包含 `first` 和 `rest` 两个属性，前者是当前的值，后者是剩下的链表。

---

## 🖼️ 图示结构

### 示例：`Link(3, Link(4, Link(5, Link.empty)))`

```text
┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────┐
│ first: 3   │ -> │ first: 4   │ -> │ first: 5   │ -> │ Link.empty │
│ rest: ─────┘    │ rest: ─────┘    │ rest: ─────┘    └────────────┘
```

# 🧠 `assert` 与 `isinstance()` 学习笔记

---

## 🔎 为什么学习这两个函数很重要？

- `assert` 是调试阶段常用的断言工具，可快速定位逻辑错误。
- `isinstance()` 是 Python 中进行**类型判断**的推荐方式，确保传参正确、避免类型错误。
- 在面向对象结构中，如**链表（Linked List）**，这两个函数常一起用于验证数据结构的合法性。

---

## 🧪 `assert` 函数：断言语句

### 📌 定义说明：

> `assert` 语句用于检查表达式是否为真，如果为假则抛出异常。常用于开发阶段的错误检测。

### 🧠 语法：

```python
assert 条件表达式[, 错误信息]
```

✅ 使用示例：
```python
x = 5
assert x > 0  # 条件成立，不报错

assert x < 0, "x 必须为负数"  # 条件不成立，抛出 AssertionError
```

## 🧬 isinstance() 函数：类型判断
📌 定义说明：
isinstance() 用于判断一个对象是否是指定类型（或其子类）的实例。
```python
isinstance(对象, 类型) → 返回布尔值
```
✅ 使用示例：
```python
isinstance(3, int)          # True
isinstance("hello", str)    # True
isinstance([], list)        # True
isinstance({}, list)        # False
```

# 🧠 `map()` 函数学习笔记

---

## 🤔 为什么学习 `map()` 很重要？

- 它是 Python 中处理**批量数据转换**的常用工具；
- 避免使用繁琐的 for 循环，使代码更加 **简洁、函数式、可读性强**；
- 搭配 `lambda` 表达式使用，威力更大 💥！

---

## 🧬 函数定义与语法

> `map()` 会将传入的函数依次作用到给定序列的每个元素上，并返回一个新的可迭代对象。

### 📌 语法：

```python
map(function, iterable)
```


# 🧠 `Link` 链表中的循环引用示例

---

## 🤔 代码行为解读：为什么 `s.first` 输出是 `5`？

```python
s = Link(1, Link(2, Link(3)))  # 创建链表：1 → 2 → 3
s.first = 5                    # 把第一个值改成 5
t = s.rest                     # t 指向第二个节点（值为 2 的节点）
t.rest = s                     # 让 t 的 rest 指回 s（产生循环）
s.first                       # 输出 s 的 first 值
```
# 图示结构（简略）：

s ─┐
   ↓
  [5] → t → [2] → s (again) → ...



  # 🧠 `Tree` 🌲 类学习笔记

---

## 🤔 为什么学习 `Tree` 很重要？

- 它是处理递归结构的典型例子；
- 比链表更复杂，能够更好地抽象现实问题；
- 出现在很多 CS 结构题目、算法与人工智能中；
- 掌握树之后可以更轻松学习图、搜索等内容！

---

## 🌳 `Tree` 的递归定义与类结构

> 每棵树都有一个 **根标签** `label` 和 **分支列表** `branches`

### 📌 类定义：

```python
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)
```

### 🧪 创建一棵树的示例:
```python
t = Tree(3, [
        Tree(2, [Tree(0), Tree(1)]),
        Tree(1)
    ])
```
🤖 代码行为解读：这棵树长什么样？
```text
        3
       / \
      2   1
     / \
    0   1
```
```python
t.label                      # 输出根节点 3
t.branches[0].label         # 第一个分支是 2
t.branches[0].branches[1]   # 是值为 1 的叶子节点
```
### 📎 如何判断是否是叶子节点？
```python
def is_leaf(t):
    return not t.branches
```
### 🖨 树结构打印函数（缩进法）
```python
def print_tree(t, indent=0):
    print('  ' * indent + str(t.label))
    for b in t.branches:
        print_tree(b, indent + 1)
```
运行后输出：
```text
3
  2
    0
    1
  1