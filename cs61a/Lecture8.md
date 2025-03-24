Berkeley CS Lecture Notes: Understanding Python Print and Function Behavior

这页PPT的主要内容围绕 Python print 函数的返回值 以及 嵌套函数 (nested functions) 的作用。
⸻

1. print 函数的返回值

在 Python 中，print 函数的作用是 在终端输出内容，但它的 返回值始终是 None。这点在以下例子中体现：

表达式	    计算结果	交互式输出
5	          5	         5
print(5)    None	     5
print(print(5))	None	5，None

重点理解
	•	直接写 5，Python 解释器会返回 5。
	•	print(5) 会打印 5，但它的返回值是 None。
	•	print(print(5)) 的内部执行过程：
	1.	print(5) 先执行，输出 5，并返回 None。
	2.	print(None) 执行，输出 None。

⸻

2. Python 高阶函数：嵌套函数

PPT 中定义了一个特殊的 delay 函数：

def delay(arg):
    print("delayed")
    def g():
        return arg
    return g

	•	delay(arg) 接收一个参数，并返回一个 新的函数 g。
	•	g() 不会立即执行，只有当 g() 被调用时，才会返回 arg。

复杂表达式解析

表达式 delay(delay)()(6)

步骤	                结果
delay(delay)	       打印 “delayed”，返回 g()
delay(delay)()	       调用 g()，返回 delay
delay(delay)()(6)	   执行 delay(6)，打印 “delayed”，返回 g()
delay(delay)()(6)()	   调用 g()，返回 6

最终的交互式输出

delayed
delayed
6



⸻

1. 复杂函数调用案例

print(delay(print)()(4))

步骤	             结果
delay(print)	    打印 “delayed”，返回 g()
delay(print)()(4)	执行 g()，返回 print
print(4)	        输出 4，返回 None

最终的交互式输出

delayed
4
None



⸻

4. 重点知识点总结

(1) print 的返回值
	•	print() 仅仅是 输出，但 返回值始终是 None。

(2) 高阶函数和嵌套作用域
	•	Python 函数可以返回另一个函数，形成 闭包（closure）。
	•	调用 delay(arg) 并不会立即返回 arg，而是返回 g()，需要 g() 被调用后才会返回 arg。

(3) 函数执行顺序
	•	需要按照 从内到外 的执行逻辑分析 Python 代码。
	•	关注 函数返回值，不要被 print 语句的输出干扰。

⸻

如何提高 Python 代码理解能力？
	1.	多做分解练习：在纸上手写 每一步的执行顺序，避免盲目执行代码。
	2.	使用 print(type(x)) 辅助理解：检查返回值的数据类型，避免误解代码行为。
	3.	在 Python 解释器中调试：使用 Python Tutor（http://pythontutor.com/）可视化代码执行过程。
	4.	多做高阶函数练习：Python 的 lambda、map、filter 也是基于类似概念构建的。


***解析 delay(delay)()(6)() 的执行过程

我们先回顾 delay 函数的定义：

def delay(arg):
    print("delayed")
    def g():
        return arg
    return g

该函数的执行逻辑是：
	1.	调用 delay(arg) 会 打印 "delayed"，然后返回 内部函数 g()。
	2.	g() 被调用时，会 返回 arg。

⸻

执行 delay(delay)()(6)()

我们拆解 delay(delay)()(6)() 的执行过程：

第 1 步：delay(delay)
	•	delay 函数被调用，参数 arg 是 delay 本身。
	•	print("delayed") 输出 "delayed"。
	•	返回 g()，其中 g() 是：

def g():
    return delay



✅ 当前返回的值是 g()，它等价于一个 return delay 的函数。

⸻

第 2 步：delay(delay)()
	•	delay(delay) 返回了 g()，所以 delay(delay)() 调用 g()。
	•	g() 的定义是 return delay，所以它返回 delay。

✅ 当前返回的值是 delay 函数本身。

⸻

第 3 步：delay(delay)()(6)
	•	上一步返回 delay，所以 delay(delay)()(6) 等价于 delay(6)。
	•	delay(6) 被调用，arg=6。
	•	print("delayed") 输出 "delayed"。
	•	返回 g()，其中 g() 是：

def g():
    return 6



✅ 当前返回的值是 g()，它等价于 return 6 的函数。

⸻

第 4 步：delay(delay)()(6)()
	•	上一步返回 g()，所以 delay(delay)()(6)() 调用 g()。
	•	g() 的定义是 return 6，所以它返回 6。

✅ 最终返回 6。

⸻

完整的输出

delay(delay)()(6)()

的执行顺序和输出：

delayed
delayed
6

你可以把 delay 想象成一个“延迟返回”的机制，每次调用它，都会返回 一个函数，直到最终的 g() 被调用时，才真正返回 arg 的值。


这页 PPT 主要考察 Python 作用域与高阶函数的执行顺序，涉及以下几个知识点：

1. Python 的函数调用与返回值
	•	square(x): 计算 x * x
	•	pirate(arggg):
	•	print("matey") 直接输出 "Matey"
	•	plunder(arggg): 返回 arggg
	•	pirate(x) 总是返回 identity function（恒等函数）

2. 代码解析
	•	add(pirate(3)(square)(4), 1)
	1.	pirate(3) 执行，打印 "Matey"，返回 identity function
	2.	identity function(square) 仍然返回 square
	3.	square(4) 计算 16
	4.	add(16, 1) 计算 17
	5.	输出：“Matey” 17
	•	pirate(pirate(pirate))(5)(7)
	1.	pirate(pirate) 执行，打印 "Matey"，返回 identity function
	2.	pirate(identity function) 执行，打印 "Matey"，返回 identity function
	3.	identity function(5) 返回 5
	4.	5(7) 企图调用 5，发生错误
	5.	输出：“Matey” “Matey” Error

3. 知识点总结
	•	Python 作用域：pirate 定义了一个嵌套函数 plunder，返回 arggg，本质上是恒等函数
	•	高阶函数：pirate(x) 返回一个函数，函数可以作为参数传递
	•	函数调用顺序：外层函数 pirate 先执行并打印 "Matey"，再返回函数
	•	错误解析：尝试 5(7) 导致错误

4. 提高成绩的建议
	•	多练习 Python 作用域与高阶函数
	•	理解 返回值是函数的概念
	•	画出 调用过程图，分析执行顺序


什么是 Identity Function（恒等函数）？

Identity Function（恒等函数） 是一个返回其输入参数的函数，即：

def identity(x):
    return x

换句话说，无论传入什么参数，它都会 原样返回。

⸻

identity function 是怎么产生的？

在 pirate 函数中，它的行为如下：

def pirate(arggg):
    print("matey")
    def plunder(arggg):
        return arggg  # 这里返回传入的参数，即 identity function 的特性
    return plunder

	•	pirate(arggg) 执行后，它返回 plunder 这个函数。
	•	plunder(arggg) 的定义是 return arggg，意味着 plunder 只会返回它的输入参数，不做任何修改。
	•	这正是 identity function（恒等函数）的行为，所以 pirate(x) 相当于 identity function。

⸻

代码解析（如何产生 identity function）

例子：

f = pirate(3)  # 执行 pirate(3)，打印 "Matey"，返回 plunder 函数
print(f(10))   # f(10) 相当于 plunder(10)，所以返回 10

执行顺序：
	1.	pirate(3) 执行，打印 "Matey"，返回 plunder
	2.	f(10) 实际上是 plunder(10)，返回 10
	3.	所以 f(10) 的作用就和 identity function 一样！

⸻

在题目中的作用

在 pirate(pirate(pirate))(5)(7) 里：
	1.	pirate(pirate) 执行：
	•	打印 "Matey"
	•	返回 identity function
	2.	pirate(identity function) 执行：
	•	打印 "Matey"
	•	返回 identity function
	3.	identity function(5) 执行：
	•	返回 5
	4.	错误发生在 5(7)，因为 5 不是函数！

⸻

总结
	•	pirate(x) 不是直接返回 x，而是返回 plunder 这个 identity function。
	•	identity function 本质上是 lambda x: x，即返回自身输入的函数。
	•	在 pirate(pirate(pirate))(5)(7) 中，经过两次 pirate 调用后，最终得到 identity function，然后 identity function(5) 返回 5，导致 5(7) 时报错。



*******

代码回顾

def horse(mask):
    horse = mask
    def mask(horse):
        return horse(2)
    return horse(mask)

mask = lambda horse: horse(2)
horse(mask)



⸻

执行流程详解

Python 在执行 horse(mask) 时，会按照 环境模型（Environment Model） 逐步创建新的作用域，并跟踪变量绑定关系。

⸻

1. 全局作用域（Global Frame）

def horse(mask):  # horse 函数定义
    ...
mask = lambda horse: horse(2)  # mask 赋值
horse(mask)  # 函数调用

	•	变量：
	•	horse → func horse(mask) [parent=Global]
	•	mask → λ horse: horse(2) [parent=Global]

调用 horse(mask) 进入 f1（Frame 1）。

⸻

2. f1: horse(mask) 执行

def horse(mask):
    horse = mask  # horse 绑定为传入的 mask，即 lambda horse: horse(2)
    def mask(horse):
        return horse(2)
    return horse(mask)

	•	变量：
	•	horse = λ horse: horse(2)
	•	mask = func mask(horse) [parent=f1]

执行：

return horse(mask)

	•	horse 现在是 lambda horse: horse(2)
	•	计算 horse(mask)：

(lambda horse: horse(2))(mask)

	•	horse = mask，所以执行 mask(2)

进入 f2（Frame 2）。

⸻

3. f2: mask(2) 执行
	•	mask 现在是：

def mask(horse):
    return horse(2)

	•	mask 在 f1 作用域内定义，parent=f1
	•	这里 horse = 2
	•	计算 horse(2)

所以：

return 2

最终返回 2，不会报错。

⸻

最终结果

🔹 horse(mask) → mask(2) → 2
✅ 最终的返回值是 2，代码不会报错！

⸻

总结
	1.	错误理解修正：原本以为 horse(2) 会调用整数 2，但实际上 horse 在 f2 作用域内是一个函数（mask），所以执行正常。
	2.	作用域解析：
	•	horse = mask
	•	mask(2) 实际上调用的是 def mask(horse)，而 horse 在 mask(horse) 内部只是一个参数，并不会影响外层 horse 的绑定。
	3.	Python 的环境模型（Environment Model）：
	•	变量查找遵循 最近作用域原则（Lexical Scoping）。
	•	horse 变量在不同作用域内指向不同的对象，执行时要看 当前环境。
	


******装饰器*****

1. 什么是装饰器？

装饰器是Python 中的一种特殊函数，它的作用是：
✅ 给已有的函数或方法增加额外的功能，而不修改原来的代码。

可以把装饰器想象成：
🎭 给函数戴上一个“面具”，这个面具会增强或改变函数的行为，但函数本身保持不变。

⸻

2. 为什么要用装饰器？

在编写代码时，我们经常需要在多个函数中添加相同的功能，比如：
	•	日志记录（Logging）：记录函数的执行情况
	•	权限检查（Authentication）：检查用户是否有权限访问
	•	性能监测（Performance Monitoring）：测量函数运行时间

使用装饰器，我们可以避免重复代码，提高代码复用性。

⸻

3. 装饰器的基本用法

🔹 没有装饰器的情况

如果没有装饰器，我们可能这样给函数增加功能：

def print_log_and_run(func):
    def wrapper():
        print("开始执行函数...")
        func()
        print("函数执行结束。")
    return wrapper

def say_hello():
    print("Hello, world!")

# 手动给函数增加功能
say_hello = print_log_and_run(say_hello)
say_hello()

输出：

开始执行函数...
Hello, world!
函数执行结束。

👉 问题：我们每次都要手动 say_hello = print_log_and_run(say_hello)，很麻烦！

⸻

🔹 使用 @装饰器 语法

Python 提供了一种更优雅的方法：使用 @ 语法糖！

def print_log(func):
    def wrapper():
        print("开始执行函数...")
        func()
        print("函数执行结束。")
    return wrapper

@print_log  # 这行相当于 say_hello = print_log(say_hello)
def say_hello():
    print("Hello, world!")

say_hello()  # 直接调用

输出：

开始执行函数...
Hello, world!
函数执行结束。

✅ 好处：
	•	不用手动赋值，代码更简洁！
	•	多个函数可以复用这个装饰器，不会影响原始函数的代码。

⸻

4. 适用于有参数的函数

有些函数是带参数的，比如加法函数：

def print_log(func):
    def wrapper(*args, **kwargs):  # 接受任意参数
        print(f"开始执行 {func.__name__}，参数是 {args}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行结束，返回值是 {result}")
        return result
    return wrapper

@print_log
def add(a, b):
    return a + b

print(add(3, 5))

输出：

开始执行 add，参数是 (3, 5)
函数 add 执行结束，返回值是 8
8

✅ 好处：
	•	*args, **kwargs 让装饰器能适用于任何函数！
	•	适用于带参数和有返回值的函数。

⸻

5. 让装饰器不改变原函数的信息

有时候，我们希望函数的 __name__ 和 __doc__ 不被修改：

from functools import wraps

def print_log(func):
    @wraps(func)  # 这个装饰器可以保持原函数的信息
    def wrapper(*args, **kwargs):
        print(f"开始执行 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

📌 使用 @wraps(func) 可以保持原函数的 __name__ 和 __doc__。

⸻

6. 多个装饰器叠加

Python 支持多个装饰器，执行顺序是从上到下：

def decor1(func):
    def wrapper():
        print("装饰器 1")
        func()
    return wrapper

def decor2(func):
    def wrapper():
        print("装饰器 2")
        func()
    return wrapper

@decor1
@decor2
def say_hello():
    print("Hello!")

say_hello()

执行顺序：

装饰器 1
装饰器 2
Hello!

✅ 执行顺序：decor1(decor2(say_hello))

⸻

7. 装饰器的实际应用

（1）记录函数执行时间

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 运行时间: {end - start:.5f} 秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("函数执行完毕！")

slow_function()

输出：

函数执行完毕！
slow_function 运行时间: 2.00012 秒

✅ 用来测试函数的执行时间！

⸻

（2）权限控制

def check_permission(func):
    def wrapper(*args, **kwargs):
        user = "admin"
        if user != "admin":
            print("无权限执行！")
            return
        return func(*args, **kwargs)
    return wrapper

@check_permission
def delete_file():
    print("文件已删除！")

delete_file()

✅ 控制某些函数只能在满足条件时运行。

⸻

8. 课堂笔记总结

✅ 装饰器的核心概念
	1.	装饰器是一个函数，用于增强或修改另一个函数的行为。
	2.	语法：使用 @装饰器名 修饰函数，等同于 func = 装饰器(func)。
	3.	适用于多个函数，可以复用代码，避免重复编写。
	4.	适用于带参数的函数，使用 *args, **kwargs 来适配不同的函数。
	5.	使用 @wraps(func) 保持原函数的信息（如 __name__、__doc__）。
	6.	支持多个装饰器叠加，执行顺序从上到下。

⸻

✅ 装饰器的应用场景
	•	日志记录（Logging）📜
	•	权限控制（Authentication）🔒
	•	性能分析（Performance Monitoring）⏳
	•	缓存机制（Caching）🗄️
	•	输入参数验证（Validation）✅


