# 🧩 CS61A Scheme — Built-in List Processing Procedures 简明笔记

> 主题：Scheme 的常用列表处理函数（append / map / filter / apply）

---

## 1️⃣ `(append s t)` — 拼接列表
- 功能：把多个列表首尾相连。
- 示例：
  ```scheme
  (append '(1 2) '(3 4))  ; => (1 2 3 4)
  ```

---

## 2️⃣ `(map f s)` — 映射函数
- 功能：将函数 `f` 应用于每个元素，生成新列表。
- 示例：
  ```scheme
  (map (lambda (x) (* x x)) '(1 2 3 4))  ; => (1 4 9 16)
  ```

---

## 3️⃣ `(filter f s)` — 筛选元素
- 功能：保留使 `f` 返回真值的元素。
- 示例：
  ```scheme
  (filter (lambda (x) (> x 2)) '(1 2 3 4 5))  ; => (3 4 5)
  ```

---

## 4️⃣ `(apply f s)` — 展开列表调用函数
- 功能：把列表元素作为参数传入函数。
- 示例：
  ```scheme
  (apply + '(1 2 3 4))  ; => 10
  ```

---

## ✅ 总结对比

| 函数 | 功能 | 返回 |
|------|------|------|
| `append` | 拼接列表 | 合并后的列表 |
| `map` | 应用函数到每个元素 | 新列表 |
| `filter` | 挑选符合条件的元素 | 子列表 |
| `apply` | 用列表内容调用函数 | 单一结果 |

---

📘 **记忆口诀：**
> `append` 拼接，`map` 变换，`filter` 筛选，`apply` 调用。
