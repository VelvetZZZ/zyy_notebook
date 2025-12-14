class Tree:
    def __init__(self, label, branches=None):
        self.label = label
        self.branches = branches if branches is not None else []

    def __repr__(self):
        if not self.branches:
            return f"Tree({self.label})"
        return f"Tree({self.label}, {self.branches})"


def bigs(t):
    def f(a, x):
        # a: 当前节点
        # x: 祖先中的最大标签
        if a.label > x:
            return 1 + sum(f(b, a.label) for b in a.branches)
        else:
            return sum(f(b, x) for b in a.branches)

    return f(t, t.label - 1)


# ===== 测试 =====
if __name__ == "__main__":
    a = Tree(1, [
        Tree(4, [Tree(4), Tree(5)]),
        Tree(3, [Tree(0, [Tree(2)])])
    ])

    print(bigs(a))  # 应该输出 4



## 另一种实现方式，使用可变对象保存计数
def bigs(t):
    n = [0]  # 用列表保存计数（可变对象）

    def f(a, x):
        if a.label > x:
            n[0] += 1

        for b in a.branches:
            f(b, max(a.label, x))

    f(t, t.label - 1)
    return n[0]




# 完整的 smalls(t) 实现

def smalls(t):
    """
    返回所有非叶子节点中标签小于所有后代节点标签的节点的列表。
    """
    # 结果列表必须在外部定义，以便 process 函数可以修改它 (副作用)
    result = []
    
    # 定义内部辅助函数
    def process(t):
        if t.is_leaf():
            return t.label
        else:
            # 1. 递归获取所有后代中的最小标签
            smallest_in_descendants = min([process(b) for b in t.branches]) 
            
            # 2. 核心判断与副作用
            if t.label < smallest_in_descendants:
                result.append(t)
                
            # 3. 向上返回：返回当前子树 (包括 t) 的最小标签
            return min(smallest_in_descendants, t.label)

    # 启动递归，但忽略 process(t) 的返回值，因为结果存储在 result 中
    process(t) 
    return result

# 注意：在实际 Python 代码中，内部函数 process 需要被定义在 smalls 内部，
# 才能访问到 result 变量。