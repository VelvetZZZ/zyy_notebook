#Lists in Environment Diagrams
s = [1, 2]
t = s
t.append(3)
print(s)  # 输出？

s = [1, 2]
t = list(s)
t.append(3)
print(s)  # 输出？


t = [1, 2, 3]
t[1:3] = [t]
t.extend(t)

t = [[1, 2], [3, 4]]
t[0].append(t[1:2])

#Land Owners —— 类属性 vs 实例属性

class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

# Examples:Iterables & Iterators

def min_abs_indices(s):
    """
    Indices of all elements in list s that have the smallest absolute value.

    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    min_abs = min(abs(x) for x in s)
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]
s = [-4, -3, -2, 3, 2, 4]
print(min_abs_indices(s))
"""等价于
def min_abs_indices(s):
    min_abs = min(map(abs, s))
    def f(i):
        return abs(s[i]) == min_abs
    return list(filter(f, range(len(s))))"""



def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s."""
    return max([s[i] + s[i+1] for i in range(len(s) - 1)])
"""等价于max([a + b for a, b in zip(s[:-1], s[1:])])"""


def digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d."""
    return {
        d: [x for x in s if x % 10 == d]
        for d in range(10)
        if any(x % 10 == d for x in s)
    }
s = [5, 8, 13, 21, 34, 55, 89]
print(digit_dict(s))

# 方法 2：先提取所有出现过的个位数（更高效）
def digit_dict(s):
    last_digits = [x % 10 for x in s]
    return {
        d: [x for x in s if x % 10 == d]
        for d in range(10)
        if d in last_digits
    }

# 示例测试
s = [5, 8, 13, 21, 34, 55, 89]
print(digit_dict(s))


def all_have_an_equal(s):
    """Does every element equal some other element in s?"""
    return min([s.count(x) for x in s]) > 1

#方法2:使用列表切片
def all_have_an_equal(s):
    return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])