# 🧠 CS61A 学习笔记：Lists in Environment Diagrams

## 📌 主题说明  
本节课主要讲解 Python 中 **列表（list）对象**的行为与环境图（Environment Diagrams）之间的关系，帮助我们理解变量绑定、引用、浅拷贝与深拷贝的区别。

---

## ✅ 初始状态

```python
s = [2, 3]
t = [5, 6]
```
我们有两个列表 s 和 t，它们分别指向两块不同的内存空间。

## 🧪 操作与结果对比（行为实验）
![alt text](image-1.png)

## 📎 对比分析
✅ append vs extend 区别:
•	append(x)：将 x 整体作为一个元素添加进去。
•	extend(x)：把 x 拆开来添加，适用于列表合并。
✅ 引用 vs 拷贝:
类型                     表现             说明
引用（reference）修改一个变量会影响另一个     如：t = s
拷贝（copy）     修改原始列表不会影响新列表   如：t = s[:]、t = list(s)

## 🧠 编程思想（CS61A 重点）
•	所有列表变量其实是指针 / 引用。
•	多个变量可能指向同一个列表对象。
•	使用切片、list() 等方式可实现“新对象”的创建，避免副作用。
•	环境图帮助你分析变量、值、引用之间的关系。

🎯 总结：环境图的用途
•	✅ 理清变量和对象的绑定
•	✅ 帮助 debug（查找意外共享引用）
•	✅ 理解 Python 内存模型（可变对象 vs 不可变对象）
•	✅ 为理解函数调用、递归和对象导论打基础



# 🧠 CS61A 学习笔记：列表结构与引用逻辑

## 🧪 示例分析：嵌套列表 append 的行为

### ✅ 示例代码

```python
t = [[1, 2], [3, 4]]
t[0].append(t[1:2])
```
#### 🔍 第一步：初始化列表
t = [[1, 2], [3, 4]]
此时 t 是一个包含两个列表的列表：
	•	t[0] → [1, 2]
	•	t[1] → [3, 4]
#### 🧩 第二步：切片操作 t[1:2]:
t[1:2] → [[3, 4]]
	•	注意：这是一个新的列表，里面只有一个元素 [3, 4]
	•	它和 t[1] 不同：
	•	t[1] 是 [3, 4]
	•	t[1:2] 是 [[3, 4]]（嵌套一层）
#### 🔧 第三步：执行 append:
t[0].append(t[1:2])
•等价于：
[1, 2].append([[3, 4]])
•所以 t[0] 变成：
[1, 2, [[3, 4]]]

#### 🧱 最终结构
t = [
    [1, 2, [[3, 4]]],  # t[0]
    [3, 4]             # t[1]
]
### 🧠 知识点总结
	•	append(x) 是将 x 作为一个整体添加到列表末尾。
	•	list[a:b] 返回的是新的列表，不是原始元素。
	•	对列表的引用和嵌套，要注意每一层结构。


# 🧠 CS61A 学习笔记：Land Owners —— 类属性 vs 实例属性

## 📌 核心概念

- **类属性（Class Attribute）**：属于类本身，所有实例共享。
- **实例属性（Instance Attribute）**：属于对象（实例）自身，优先级高于类属性。
- **继承（Inheritance）**：子类会继承父类的属性和方法，若有相同名称的属性，则覆盖。

---

## 👨‍🏫 示例代码分析

```python
class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'
```
 ## 🔍 属性查找规则
	•	jack.greeting → 优先查找实例属性 → jack.greeting = 'Maam' → ✅ 'Maam'
	•	john.greeting → 实例没有 greeting，查找类属性 → Bourgeoisie.greeting = 'Peon' → ✅ 'Peon'

 ## 📦 方法行为解析
 ```python
 print(john.work())
 ```
 	•	john.work() 调用的是 Bourgeoisie 重写的 work 方法。
	•	print(Worker.work(self)) 会调用父类 work 方法：
	•	self.greeting 是 john 实例查找 → Bourgeoisie.greeting → 'Peon'
	•	返回 'Peon, I work'
	•	然后返回 'I gather wealth'
🧾 输出如下：
```text
Peon, I work
I gather wealth
```

## 🧠 额外说明

__repr__ 方法
•	repr(jack) 会返回 Bourgeoisie.greeting，即 'Peon'。
•	即使 jack 是 Worker 的实例，__repr__ 中显式引用了子类 Bourgeoisie.greeting。



# 🧠 Python 列表索引函数 min_abs_indices 学习笔记

⸻

📌 目标

实现一个函数 min_abs_indices(s)，返回 列表 s 中绝对值最小的所有元素的索引列表。

⸻

✨ 示例

>>> min_abs_indices([-4, -3, -2, 3, 2, 4])
[2, 4]  # -2 和 2 的绝对值最小，都是 2，在索引 2 和 4

>>> min_abs_indices([1, 2, 3, 4, 5])
[0]  # 最小绝对值是 1


⸻

✅ 方法1：列表推导式

def min_abs_indices(s):
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]

步骤解释：
	1.	map(abs, s)：对每个元素求绝对值
	2.	min(...)：找出最小绝对值
	3.	range(len(s))：生成所有索引
	4.	[i for i in ... if abs(s[i]) == min_abs]：筛选满足条件的索引

⸻

✅ 方法2：使用 filter() 函数

def min_abs_indices(s):
    min_abs = min(map(abs, s))
    def f(i):
        return abs(s[i]) == min_abs
    return list(filter(f, range(len(s))))

与列表推导式等价：

列表推导式	filter() 方式
[i for i in ... if 条件]	list(filter(lambda i: 条件, ...))


⸻

🎯 类比理解（适合初学者）

filter 相当于“面试筛选”，列表推导式像“简历筛选”。

结果相同，都是留下满足条件的候选人（即索引）。

### 🔍 CS61A - Adjacent Pair Max Sum 总结笔记

#### ✅ 问题描述：
给定列表 `s`，找出所有相邻元素的和中最大的那个值。

#### ✅ 示例：
```python
s = [-4, -3, -2, 3, 2, 4]
# 相邻和：[ -7, -5, 1, 5, 6 ]
# 最大和：6
```
✅ 解法一：使用 range + 索引
```python
max([s[i] + s[i+1] for i in range(len(s) - 1)])
```
✅ 解法二：使用 zip
```python
max([a + b for a, b in zip(s[:-1], s[1:])])
```
