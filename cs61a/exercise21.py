#Linked Lists 链表
class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)#确保 rest 要么是 Link.empty，要么是另一个 Link 实例，防止误用。
        self.first = first
        self.rest = rest
s = Link(3, Link(4, Link(5)))