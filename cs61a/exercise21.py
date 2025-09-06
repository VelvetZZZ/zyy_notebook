#Linked Lists 链表
class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)#确保 rest 要么是 Link.empty，要么是另一个 Link 实例，防止误用。
        self.first = first
        self.rest = rest
s = Link(3, Link(4, Link(5)))


s = Link(3, Link(4, Link(5)))
#操纵链表
print(s.first)
print(s.rest)
print(s.rest.first)
print(s.rest.rest.first)
print(s.rest.rest.rest)
print(s.rest.rest.rest is Link.empty)
#更改链表
s.rest.first = 7
print(s)
#通常不改变链表
print(Link(8, s.rest))


#Linked List Processing
#Example：Range, Map, and Filter for Linked Lists
square = lambda x: x * x
odd = lambda x: x % 2 == 1
list(map(square, filter(odd, range(1, 6))))


def range_link(start, end):
    """Return a Link containing consecutive integers from start to end."""
#返回一个从 start 到 end - 1 的链表
range_link(3, 6)
#→ Link(3, Link(4, Link(5)))


def map_link(f, s):
    """Return a Link that contains f(x) for each x in Link s."""
#类似 Python 的 map()，将函数 f(x) 应用于链表 s 的每个元素，生成新链表。
map_link(square, range_link(3, 6))
#→ Link(9, Link(16, Link(25)))


def filter_link(f, s):
    """Return a Link that contains only the elements x of Link s for which f(x) is a true value."""
#类似 Python 的 filter()，保留链表中满足 f(x) 的元素。
filter_link(odd, range_link(3, 6))
#→ Link(3, Link(5))
map_link(square, filter_link(odd, range_link(1, 6)))



class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return f'Link({self.first}{rest_str})'

    def __str__(self):
        s = '<'
        while self.rest is not Link.empty:
            s += str(self.first) + ' '
            self = self.rest
        s += str(self.first) + '>'
        return s


# --------------------------
# 递归定义的函数部分
# --------------------------

def range_link(start, end):
    """Return a Link containing consecutive integers from start to end."""
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))


def map_link(f, s):
    """Return a Link that contains f(x) for each x in Link s."""
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
    """Return a Link that contains only the elements x of Link s for which f(x) is true."""
    if s is Link.empty:
        return s
    filtered_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filtered_rest)
    else:
        return filtered_rest


# --------------------------
# 测试代码
# --------------------------

# 定义函数：平方 和 判断奇数
square = lambda x: x * x
odd = lambda x: x % 2 == 1

# 创建链表：Link(1, Link(2, Link(3, Link(4, Link(5)))))
r = range_link(1, 6)

# 过滤奇数：Link(1, Link(3, Link(5)))
s = filter_link(odd, r)

# 映射平方：Link(1, Link(9, Link(25)))
t = map_link(square, s)

# 打印输出
print(t)       # 输出 Link(1, Link(9, Link(25)))
print(str(t))  # 输出 <1 9 25>


#Linked Lists Mutation(改变)

#Example：Adding to a Set Represented as an Ordered List
def add(s, v):
    assert s is not Link.empty

    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        s.rest = add(s.rest, v)
    return s



def remove(s, v):
    """Remove value v from ordered linked list s, return modified s."""
    assert s is not Link.empty

    if s.first == v :
        return s.rest
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(s)
    elif s.first < v:
        s.rest = remove(s.rest, v)  # ✅ 要更新链表结构
    else:
        return s


#Tree Class