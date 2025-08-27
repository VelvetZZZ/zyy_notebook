# The Class Statement
## 什么是 class 语句？
```python
class <name>:
    <suite>
```
•	class 是用来定义一个类的关键词。
•	<name> 是你给这个类起的名字（比如 Clown）。
•	<suite> 是类体（缩进块），定义了类的内容——比如变量（属性）或函数（方法）。
💡当你运行 class Clown: 时，Python 会立刻执行 suite 中的代码，并把这些赋值和函数绑定为这个类的属性。

📦 示例拆解
```python
class Clown:
    nose = 'big and red'
    
    def dance():
        return 'No thanks'
```
1.	定义了一个类 Clown。
2.	给这个类添加了两个属性：
nose: 一个类变量，值为 'big and red'
dance(): 一个类方法，返回 'No thanks'

🔍 如何使用这个类？
```python
Clown.nose
# 输出: 'big and red'

Clown.dance()
# 输出: 'No thanks'

Clown
# 输出: <class '__main__.Clown'>
```
说明：
•Clown.nose 是访问类的变量（没有创建实例）。
•Clown.dance() 是直接调用类里的函数。
•Clown 是一个类对象，本质上就是 <class 'Clown'>。
❗ 注意：这个类还没有实例！
  这个例子中我们并没有创建 Clown() 实例对象，只是在直接访问类属性本身。
  这叫做 类属性访问，区别于实例属性

✅ 总结知识点：
概念                               解释
类属性（Class Attribute）        定义在类里、__init__ 外的属性，所有对象共享
实例属性（Instance Attribute）   定义在 __init__ 里，用 self.xxx = ... 赋值，每个对象独立拥有
使用方式                         类属性可以通过类或对象访问：Account.interest 或 tom_account.interest
