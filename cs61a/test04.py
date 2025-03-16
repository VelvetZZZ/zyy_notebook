def apply_twice(f, x):
    return f(f(x))


def square(x):
    return x * x


result = apply_twice(square, 2)
print(result)


def make_adder(n):#第一个帧
    def adder(k):
        return k + n

    return adder#将信息从本地帧带回到首次调用该函数的当前帧


add_three = make_adder(3)
print(add_three(4))#新框架：k绑定到4
print(add_three(5))
#nested framework(def statement):把函数的父级设置为该函数创建时的当前帧


