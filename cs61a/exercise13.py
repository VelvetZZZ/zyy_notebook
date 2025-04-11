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



#创建一棵结构一样的新树，只对叶子节点的标签进行 +1
def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented(递增)."""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t),bs)
#创建一棵结构一样的新树，对所有节点（包括根节点和所有子节点）都进行 +1。    
def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])
    
#Example:Printing Trees
def print_tree(t):
    print(label(t))
    for b in branches(t):
        print_tree(b)
print_tree(fib_tree(4))

print('     '* 5 + str(5))

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)
print_tree(fib_tree(4))
#The indentation level of a label corresponds to its depth in the tree

#Example:Summing Paths
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n -1)
print(fact(5))

def fact_times(n, k):
    "Return k * n * (n-1) * ... * 1"
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)



from tree import *
numbers = tree(3,[tree(4), tree(5, [tree(6)])])
haste = tree('h', [tree('a', [tree('s'),
                                   tree('t')]),
                    tree('e')])

def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)
print(print_sums(numbers, 0))
print(print_sums(haste, ''))

#Count Paths that have a Total Label Sum