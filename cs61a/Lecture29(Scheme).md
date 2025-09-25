# 列表结构（Scheme Lists）

## 🧩 1. 列表基础：cons、car、cdr 与 nil
•cons：用于构造一对值（pair），通常用于构建链表
•car：返回 cons 生成的第一个值（相当于 Python 的 x[0]）
•cdr：返回 cons 生成的第二个值（相当于 Python 的 x[1:]）
•nil：表示空列表（类似 Python 中的 []）

## ✅ 2. 列表示例对比（Scheme vs Python）

```scheme
(cons 1 (cons 2 nil)) ; 输出: (1 2)
```

```python
(1, (2, None))              # Python 中类似的链表结构表示
```