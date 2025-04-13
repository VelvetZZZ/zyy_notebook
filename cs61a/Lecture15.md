# 主题：Objects（对象）

## 什么是对象（Objects）？
	•	Objects represent information
→ 对象是用来“表示信息”的。比如，一个“学生”对象可以表示学生的姓名、年龄、成绩等信息。
	•	They consist of data and behavior, bundled together to create abstractions
→ 对象包含 数据（data） 和 行为（behavior），它们被“打包”在一起。这种方式叫做 抽象（abstraction） —— 用简单的方式表示复杂的事物。
✅ 举例：你可以用一个“猫”对象来表示一只猫，它的数据是“名字、年龄、颜色”，它的行为可能是“喵喵叫、抓老鼠”。

⸻

## 对象可以表示什么？
	•	Objects can represent things, but also properties, interactions, & processes
→ 它不仅能代表“东西”（比如猫、车、人），还能表示“属性、相互作用、过程”。这比传统的函数更强大。

⸻

#  什么是类（Class）？
	•	A type of object is called a class; classes are first-class values in Python
→ 类是一种“对象的模板”，用来创建多个类似的对象。比如有一个 Student 类，你可以用它创建很多学生对象。
在 Python 中，类本身也是一个对象（也就是说，类也是值，也可以传递、赋值）。

⸻

#  面向对象编程（Object-Oriented Programming, OOP）
	•	A metaphor for organizing large programs
→ 面向对象编程是一种组织大型程序的方法。它就像你在写小说时，用“角色”来推动故事一样，你用“对象”来组织程序。
	•	Special syntax that can improve the composition of programs
→ OOP 有专门的语法，让你写出结构更清晰、更容易维护的代码。

⸻

#  Python 的对象模型
	•	In Python, every value is an object
→ 在 Python 里，一切皆对象！（包括整数、字符串、函数、模块……）
	•	All objects have attributes
→ 每个对象都有“属性”，比如字符串对象有 .upper() 方法，列表对象有 .append() 方法。
	•	A lot of data manipulation happens through object methods
→ 数据操作主要通过对象的方法（method）来实现。方法就像对象的“功能”。
	•	Functions do one thing; objects do many related things
→ 函数只做一件事，但对象可以包含多个相关的功能。例如，一个“车”对象可以有“启动、加速、刹车”等方法。

⸻

📝 总结笔记（适合记在本子上）
	1.	对象（Object） = 数据 + 行为，构建程序的基本单位。
	2.	类（Class） = 创建对象的模板。
	3.	面向对象编程（OOP）：更适合构建大型项目的方式，结构清晰。
	4.	在 Python 中，所有的值都是对象（包括函数、数字、字符串等）。
	5.	对象方法 = 操作数据的工具（如 str.upper()，list.append()）。
	6.	区别函数和对象：
	•	函数：单一功能；
	•	对象：多个相关功能组合在一起。
