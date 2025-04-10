#Trees
#实现树结构抽象 (Implementing the Tree Abstraction)
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)  # 确保每个分支本身也是一个合法的树
    return [label] + list(branches)  # 构造树的列表结构

def label(tree):
    return tree[0]#返回树的根值（label）

def branches(tree):
    return tree[1:]#返回树的所有分支（子树）

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True#判断一个结构是否是合法的树；必须是 list 类型且长度 >= 1；每一个分支也必须是树（递归判断）

def is_leaf(tree):
    return not branches(tree)#如果没有分支（branches 为空），那么就是叶子节点

tree(1)
print(is_leaf(tree(1)))

t = tree(1, [tree(5, [tree(7)]),tree(6)])
print(t)
print(label(t))
print(branches(t))
print(branches(t)[0])
print(is_tree(branches(t)[0]))
print(label(branches(t)[0]))

#fibonacci tree
def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])
print(fib_tree(0))
print(fib_tree(2))
print(fib_tree(1))
print(label(fib_tree(1)))

#Tree processing
"""Functions that take trees as input or return trees as output are often tree recursive themselves."""
def count_nodes(tree):
    total = 1  # 自己是一个节点
    for branch in branches(tree):
        total += count_nodes(branch)  # 对每个分支递归调用
    return total

#找出树中最大值
def tree_max(t):
    current_max = label(t)
    for b in branches(t):
        current_max = max(current_max, tree_max(b))
    return current_max

t = tree(3, [
    tree(1, [tree(0), tree(1)]),
    tree(2, [tree(1)]),
    tree(1, [tree(0), tree(1)])
])
print(tree_max(t))

#Tree Processing Uses Recursion
def count_leaves(t):
    """Count the leaves of a tree"""
    if is_leaf(t):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(t)]
        return sum(branch_counts)
print(fib_tree(4))
print(count_leaves(fib_tree(4)))
print(count_leaves(fib_tree(10)))


#SUM函数的不同用法
print(sum([[1], [2,3],[4]],[]))
print(sum([[1]],[]))
print(sum([[[1]],[2]],[]))

def leaves(tree):
    """Return a list containing the leaf labels of tree"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)],[])

print(leaves(fib_tree(5)))