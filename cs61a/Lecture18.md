面向对象程序设计 (Object-Oriented Programming)
# 💻 面向对象 OOP — 类和对象的概念

1. 什么是 面向对象程序设计 (OOP)?
核心思想: 一种组织程序的方法，它将 数据 和 操作数据的行为 捆绑在一起。

与普通函数处理分散的数据不同，OOP将数据和行为打包成一个个****对象 (object)****。

这种打包的方式被称为 **封装 (Encapsulation)**。

2. 核心概念：类、对象、方法
**类 (Class)**:
一个用来创建对象的 蓝图 或 模板。
它定义了一类事物共同拥有的 属性 (attributes) 和 方法 (methods)。

**对象 (Object)**:
根据 类 这个蓝图创建出来的具体 实例 (instance)。
每个对象都拥有自己独立的数据（属性值）。

**方法 (Method)**:

定义在类中的函数，是对象可以执行的 行为。
必须通过 . 操作符由对象来调用。

3. 示例代码
# 1. 定义一个“汽车”的蓝图 (Class)
```python
class Car:
    # 构造方法：当一个对象被创建时自动执行
    # self 代表对象实例本身
    def __init__(self, brand, color):
        self.brand = brand      # 属性：品牌
        self.color = color      # 属性：颜色

    # 一个普通方法：定义了汽车的行为
    def drive(self):
        # 方法内部可以访问对象的属性
        print(f"一辆{self.color}的{self.brand}车正在行驶。")


# 2. 根据蓝图创建两个具体的“汽车”实例 (Object)
my_car = Car("特斯拉", "红色")      # 创建第一个对象
your_car = Car("比亚迪", "白色")    # 创建第二个对象

# 3. 操作对象
print(my_car.brand)             # 访问对象的属性，输出: 特斯拉
your_car.drive()                # 调用对象的方法，输出: 一辆白色的比亚迪车正在行驶。
```

# Example：列表 (List)

## 1. 列表的本质
- 在 Python 中，`list` 是一个 **内建类 (class)**。
- 使用 `list()` 可以创建一个新的列表对象。

示例：
```python
>>> list
<class 'list'>
```
说明：list 其实就是一个类。

## 2. 创建列表
	•	列表可以从任何 可迭代对象 (iterable) 创建。
	•	常见方法是用 range() 生成序列，再转成列表。
```python
>>> s = list(range(3))
>>> s
[0, 1, 2]
>>> type(s)
<class 'list'>
```
逻辑：
	1.	range(3) 生成一个迭代对象：0, 1, 2。
	2.	list(range(3)) 把迭代对象转成真正的列表。
	3.	s 就是一个 list 类型的对象。

## 3. 列表能做什么？
列表是一个类（class），它定义了各种行为，比如：

（1）方法（Methods）
	•	append(x) → 在末尾添加元素
	•	extend([a, b]) → 扩展列表
	•	insert(i, x) → 在指定位置插入
	•	`pop