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
