好问题！我们先来回答你最关心的一点：

⸻

💡 “关键字” 和 “保留字” 是一样的吗？

在 Python 中它们基本是一个意思，可以互换使用 ✅
	•	官方文档使用的是 “keywords”，翻译为“关键字”
	•	也有人称它们为“保留字”，因为这些词被保留给语言语法使用，不能当变量名使用

**总结一句话：**在 Python 中，“关键字” = “保留字” ✅

⸻

📘 Python 3 保留字（关键字）速记表（共 35 个）

我们把这些关键词分成几类，方便你记忆：

⸻

🧱 1. 条件判断类

关键字	 说明
if	    如果
elif	否则如果
else	否则



⸻

🔁 2. 循环控制类

关键字	   说明
for	      循环
while	  当…时循环
break	  跳出循环
continue  跳过当前循环
pass	  占位（什么也不做）



⸻

🧠 3. 逻辑运算类

关键字	说明
and	    与
or	    或
not	    非
in	   在…中
is	  身份比较



⸻

📦 4. 数据结构类

关键字	说明
True	布尔真
False	布尔假
None	空值



⸻

🧰 5. 定义与声明类

关键字	    说明
def	      定义函数
return	  返回值
lambda	  匿名函数
class	  定义类
yield	  返回生成器值
global	  声明全局变量
nonlocal  声明外层变量（闭包）
del	删除



⸻

🧱 6. 异常与上下文类

关键字	   说明
try	     尝试
except	捕获异常
finally	无论如何都执行
raise	抛出异常
assert	断言（调试）
with	上下文管理（常用于文件）
as	    起别名



⸻

🔐 7. 模块与导入类

关键字	 说明
import	导入模块
from	从模块中导入
as	    起别名



⸻

🌐 8. 其他语法类

关键字	 说明
await	等待（异步）
async	异步函数
None	空值（像 null）



⸻

✅ 快速查关键字（推荐记不住时跑一遍）

import keyword
print(keyword.kwlist)

这会输出当前 Python 版本中的全部关键字列表。
