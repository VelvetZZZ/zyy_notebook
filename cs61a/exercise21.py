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
