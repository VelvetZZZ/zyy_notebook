Turtle 速成教学方案（1小时）

目标：在1小时内掌握 turtle 库的基本用法，能够熟练绘制 PTA 实验 2.2 中的 叠加三角形、五角星、六角形 等图形，并记住最简单、最容易背诵的代码。

⸻

第一阶段：20 分钟 - 基础概念

了解 turtle 画图的基本函数，并快速实践。

1.1 turtle 库简介

turtle 是 Python 自带的一个绘图库，可以像画笔一样绘制图形。
使用 turtle 画图的基本步骤：

import turtle  # 引入库
t = turtle.Turtle()  # 创建画笔对象
t.forward(100)  # 前进 100 像素
t.right(90)  # 右转 90 度
t.forward(100)  # 再次前进
turtle.done()  # 结束画图，保持窗口

💡 记住：forward(距离) 画线，right(角度) 转向。

1.2 关键函数速记

函数	作用
t.forward(n)	向前移动 n 像素
t.backward(n)	向后移动 n 像素
t.right(deg)	右转 deg 度
t.left(deg)	左转 deg 度
t.penup()	抬起画笔（不画线）
t.pendown()	放下画笔（开始画线）
t.goto(x, y)	移动到 (x, y) 位置
t.setheading(deg)	设置方向（0 右, 90 上, 180 左, 270 下）
t.color("red")	设置颜色
t.begin_fill() t.end_fill()	填充颜色



⸻

第二阶段：20 分钟 - PTA 题目讲解

直接练习考试要考的三道题，并记住最简单的代码。

2.1 叠加等边三角形

要求绘制一个重叠的等边三角形，如题目 8-1。

import turtle
t = turtle.Turtle()

# 画第一个三角形
for _ in range(3):
    t.forward(100)
    t.left(120)

# 画第二个三角形（倒置）
t.penup()
t.goto(50, 50 * (3**0.5))  # 移动到顶部
t.pendown()

for _ in range(3):
    t.forward(100)
    t.right(120)

turtle.done()

📌 记住：
	•	画三角形的转角是 120°
	•	第二个三角形的起点是 (50, 50 * (3**0.5))

⸻

2.2 红色五角星

要求绘制一个 红色填充 的五角星，如题目 8-2。

import turtle
t = turtle.Turtle()
t.color("red")  # 设置颜色
t.begin_fill()  # 开始填充

for _ in range(5):
    t.forward(100)  # 画线
    t.right(144)  # 五角星的角度

t.end_fill()  # 结束填充
turtle.done()

📌 记住：
	•	五角星转角是 144°
	•	begin_fill() 和 end_fill() 用于填充颜色

⸻

2.3 六角星

要求绘制一个六角形的 交叉星形，如题目 8-3。

import turtle
t = turtle.Turtle()

for _ in range(6):
    t.forward(100)
    t.backward(100)  # 退回中心
    t.right(60)  # 旋转 60°

turtle.done()

📌 记住：
	•	六角星的角度是 60°
	•	采用 画线后退回原点 的方法

⸻

第三阶段：20 分钟 - 速记 + 练习

通过重复背诵代码 + 自己手写一遍，确保 100% 掌握。

	1.	背代码：按照上面三道题，逐行朗读，并闭眼回忆函数名称。
	2.	练习手写：不看笔记，自己尝试写出代码并运行。
	3.	错题复习：如果有不对的地方，马上改正并重新写一遍。
	4.	简化记忆法：
	•	等边三角形 → left(120)
	•	五角星 → right(144)
	•	六角星 → right(60), forward(), backward()
	•	颜色填充 → begin_fill() → 画图 → end_fill()

⸻

🎯 复习总结

✅ 掌握 turtle 的基本操作
✅ 熟练编写三道考试题的代码
✅ 记住关键函数和角度

考试策略：
	•	如果遇到不会的题目，先 默写最简单的三角形和五角星，保证基本分。
	•	再回忆 right(144) 画五角星，right(60) 画六角星，尽量还原正确答案。

⸻

最终目标

💯 1 小时内掌握 turtle，考试轻松满分！ 🚀



以下是针对考试的高效学习方案，助你在1小时内掌握turtle绘图核心技巧：

### 一、必背函数速记表（5分钟）
```python
import turtle               # 导入库（考试题开头必须写）
turtle.setup(width, height) # 设置画布尺寸（记住参数顺序：宽→高）
turtle.pensize(n)           # 画笔粗细（n=数字）
turtle.pencolor("颜色名")    # 颜色控制（red/blue/gold/purple）
turtle.penup()              # 抬笔（移动不画线）
turtle.pendown()            # 落笔（开始画线）
turtle.fd(距离)             # 前进（forward简写）
turtle.seth(角度)           # 绝对角度（0→右，90↑，-40↓）
turtle.circle(r, 角度)      # 画圆（半径r，弧度角度）
turtle.done()               # 保持窗口（程序结尾必须写）
```

### 二、太阳花模板（10分钟）
```python
from turtle import *
pencolor("gold")        # 花瓣颜色
pensize(3)              # 花瓣粗细

for _ in range(16):     # 花瓣数量（改数字即可调整）
    fd(100)             # 花瓣长度（改数值调整大小）
    right(160)          # 转角角度（保持160即可形成花瓣）

done()
```

### 三、蟒蛇魔改模板（15分钟）
```python
import turtle
turtle.setup(800,400)           # 改宽高调整画布
turtle.pensize(20)              # 蛇身粗细
turtle.pencolor("darkgreen")    # 改颜色关键词
turtle.seth(-60)                # 初始角度（-40改-60）

for i in range(4):              # 循环次数（改数值调整弯曲次数）
    turtle.circle(30, 80)       # 正圆半径（改数值）
    turtle.circle(-50, 80)      # 负圆半径（改数值）
    turtle.fd(30)               # 蛇身长度（改数值）

turtle.done()
```

### 四、应试技巧（5分钟）
1. **快速修改参数**：颜色名/数字参数是主要得分点，每个参数后加#注释说明修改意图
2. **姿态调整口诀**：
   - 正圆半径大→蛇身向上拱
   - 负圆半径大→蛇身向下弯
   - seth负数→初始头朝下
3. **万能应对法**：遇到新题时直接套模板，只改颜色/循环次数/前进距离三个参数

### 五、典型考题解法（25分钟）
**题目**：将蟒蛇改为蓝色、缩短蛇身、增加弯曲幅度
```python
# 修改点标注：
turtle.pencolor("blue")         # 改颜色 ✔
turtle.pensize(15)             # 改粗细 ✔
turtle.seth(-60)               # 改初始角度 ✔

for i in range(6):             # 增加循环次数→更多弯曲 ✔
    turtle.circle(40, 100)     # 增大弧度→弯曲更明显 ✔
    turtle.circle(-60, 100)    # 增大负圆半径→弯曲幅度大 ✔
    turtle.fd(20)              # 缩短蛇身 ✔
```

**考试注意**：
1. 所有题目必须包含`import turtle`和`turtle.done()`
2. 参数修改后立即写注释说明（如`# 改颜色得分点`）
3. 运行前检查所有括号是否闭合

按此方案练习3遍即可熟练应试，重点记忆彩色标注部分。遇到新题时只需调整颜色参数和循环次数即可快速适配，祝考试顺利！