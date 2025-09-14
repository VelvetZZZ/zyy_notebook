#Modular Design 模块化设计
#Separation of concerns（关注点分离）
#Example:Restaurant Search
def search(query, ranking=lambda r: -r.stars):
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)


class Restaurant:
    all = []  # ⚠️ 确保是列表，不要覆盖！

    def __init__(self, name, stars):
        self.name = name
        self.stars = stars
        Restaurant.all.append(self)

    def similar(self, k):
        """Return the k most similar restaurants to SELF."""
        others = [r for r in Restaurant.all if r is not self]
        return sorted(others, key=lambda r: abs(r.stars - self.stars))[:k]

    def __repr__(self):
        return '<' + self.name + '>'


# 测试数据
Restaurant('Thai Delight', 2)
Restaurant('Thai Basil', 3)
Restaurant('Top Dog', 5)

# 搜索 + 输出相似餐厅
results = search('Thai')
for r in results:
    print(r, 'is similar to', r.similar(3))

#Example:Similar Restaurants