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