# 树结构抽象（Tree Abstraction）讲解笔记

⸻

🌳 什么是树？两种描述方式

✅ 1. 递归描述（Recursive Description）

我们从编程角度（特别是 Python）来看树的定义：

“A tree has a root label and a list of branches.”

也就是说：
	•	一棵树由两部分组成：
	•	根节点的值（root label）
	•	一组分支（branches）
	•	每一个分支本身也是一棵树（递归结构）
	•	如果某棵树的分支数量为 0，那么它是一个 叶子节点（leaf）

🔁 递归性：树结构是天然适合递归处理的，因为它是“自相似”的 —— 分支本身也是树。

⸻

👪 2. 相对描述（Relative Description）

这种描述方式更像是我们平常理解的家谱（family tree）或组织结构图：

“Each location in a tree is called a node.”

	•	每一个位置叫做一个节点（node）
	•	每个节点都有一个值，称作标签（label）
	•	一个节点可以是另一个节点的 父节点（parent） 或 子节点（child）

📌 注意：
	•	相对于“节点”来说，“标签”是节点上保存的数据
	•	这个定义更强调节点之间的关系，比如谁是谁的父节点、子节点

⸻

🔍 结合图理解（从图看起）
	•	根节点：图中最上面的 “3”，是整个树的入口点
	•	标签（label）：节点中显示的数字（如3, 1, 2, 0, 1…）
	•	节点（node）：每一个圆圈都表示一个节点
	•	分支（branch）：从一个节点延伸出去的路径，指向它的子树
	•	叶子节点（leaf）：没有子树的节点（图中最下方的0, 1 等）

⸻

🧩 代码与图之间的连接

让我们回忆上一个页面中的代码（tree(label, branches=[])）和这张图是如何对应的：

tree(3, [
    tree(1, [tree(0), tree(1)]),
    tree(2, [tree(1)]),
    tree(1, [tree(0), tree(1)])
])

对应图形结构如下：

        3
      / | \
     1  2  1
   / \   \ / \
  0   1   1 0 1



⸻

✏️ 实用术语整理

术语	定义	示例（图中）
Tree	包含一个根和若干分支的结构	整棵图
Label	每个节点上存储的值	3, 1, 0, 2
Branch	子树，仍然是树	tree(1, [...])
Node	树中的一个点	每一个圆圈
Root	树的起点（顶层）	3
Leaf	没有子树的节点	0, 1（底部）
Parent/Child	节点之间的关系	3 是 1, 2, 1 的父节点



⸻

💬 课程格言式提醒

“People often refer to labels by their locations: each parent is the sum of its children”

这是一种在某些算法中常见的思维方式，意思是：
	•	父节点的值往往由子节点推导而来（比如在递归中汇总求和）

⸻

✅ 总结：你需要掌握的知识点
	•	✅ 树的两种定义方法（递归 vs 相对）
	•	✅ 如何用列表在 Python 中构造树
	•	✅ 节点、标签、分支、叶子的含义
	•	✅ 每个分支就是一个子树，树结构适合递归处理
	•	✅ 树可以非常灵活地表示层级关系，比如文件系统、表达式树、家谱树等

⸻


# “Functions that take trees as input or return trees as output are often tree recursive themselves.” 

⸻

🧾 句子原文分析：

📌 原句：

Functions that take trees as input or return trees as output are often tree recursive themselves.

✅ 中文翻译：

那些接受树作为输入或返回树作为输出的函数，本身通常也是树递归的。

⸻

🌳 什么是“树递归”（Tree Recursion）？

树递归 = 函数 对每一个分支递归调用自己，就像一棵树展开的过程一样。

🌱 举个简单的例子：

比如我们有一个函数要遍历整棵树的所有节点，它必须：
	•	先处理当前节点（root）
	•	然后 递归地对每一个子树调用自己

def count_nodes(tree):
    total = 1  # 自己是一个节点
    for branch in branches(tree):
        total += count_nodes(branch)  # 对每个分支递归调用
    return total

这就是树递归的经典结构。

⸻

🧠 为什么操作树就自然需要树递归？

原因是树本身就是 递归定义的结构，你无法一次性看完整棵树，只能逐层深入。

每一个“分支”本身又是一棵“树”。

因此：
	•	如果你的函数的目标是“遍历”或“分析”整个树，你就必须对每个子树都做相同的处理
	•	这就意味着：你的函数 会在每一层都调用自己（递归调用）

⸻

🔁 例子再来一个：找出树中最大值

def tree_max(t):
    current_max = label(t)
    for b in branches(t):
        current_max = max(current_max, tree_max(b))
    return current_max

每个函数都对自己的所有“孩子”再次调用自己 —— 这就是典型的“树递归”结构。

⸻

✅ 总结一句话解释：

因为树是递归定义的结构，所以处理树的函数 往往也需要递归地处理每一个子树 —— 也就是“树递归”。

⸻

💡延伸思考：

如果你学过普通的线性递归（比如求阶乘 factorial(n)），你会发现树递归更复杂：
	•	普通递归：每次只递归一次（一个分支）
	•	树递归：每次递归多个分支（比如3个子树就递归3次）

树递归的“递归分支数”等于分支的数量。









⸻

🎓 主题：实现树结构抽象 (Implementing the Tree Abstraction)

🌳 什么是树（Tree）？

树是计算机科学中一种非常基础而重要的数据结构，它由两部分组成：
	•	一个 根（root），也叫做标签 label
	•	一组 分支（branches），每一个分支本身也是一个树（递归定义）

⸻

📘 Python 实现解析

我们通过 Python 的列表（list）来表示一个树结构：

1. tree(label, branches=[])

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)  # 确保每个分支本身也是一个合法的树
    return [label] + list(branches)  # 构造树的列表结构

笔记：
	•	label 是树的根节点的值
	•	branches 是一个子树列表
	•	使用 assert 来进行递归验证，每个分支也是树（防止结构非法）
	•	返回的结构是一个列表，其第一个元素是根，后面的元素是子树（分支）

⸻

2. label(tree)

def label(tree):
    return tree[0]

笔记：
	•	返回树的根值（label）

⸻

3. branches(tree)

def branches(tree):
    return tree[1:]

笔记：
	•	返回树的所有分支（子树）

⸻

4. is_tree(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

笔记：
	•	判断一个结构是否是合法的树
	•	必须是 list 类型且长度 >= 1
	•	每一个分支也必须是树（递归判断）

⸻

5. is_leaf(tree)

def is_leaf(tree):
    return not branches(tree)

笔记：
	•	如果没有分支（branches 为空），那么就是叶子节点

⸻

🌲 树结构图例解释

右边是一个图示和构造实例：

      3
     / \
    1   2
         \
          1

可以用代码构造如下：

tree(3, [
    tree(1),
    tree(2, [tree(1)])
])

它表示的结构是：

[3, [1], [2, [1]]]



⸻

📒 小结笔记

函数名	功能描述
tree(l, b)	构造一棵树，根为 l，分支为列表 b
label(t)	返回树 t 的根（标签）
branches(t)	返回树 t 的所有子树
is_tree(t)	判断结构 t 是否是合法树结构
is_leaf(t)	判断树 t 是否是叶子节点（无子树）



⸻

🎯 补充说明（适合初学者）
	•	本质上，我们用 Python 的 list 来模拟一棵树。
	•	第一个元素永远是根（label），其余元素是分支（branches），每个分支都是另一个树（递归结构）。
	•	这是一种简洁的抽象，让我们可以轻松实现树的递归操作。

