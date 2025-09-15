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

class Restaurant:
    all = []

    def __init__(self, name, stars):
        self.name = name
        self.stars = stars
        Restaurant.all.append(self)

    def __repr__(self):
        return f'<{self.name}>'

    def similar(self, k, similarity):  # ✅ 放进类里！
        """Return the K most similar restaurants to SELF, using SIMILARITY for comparison."""
        others = list(Restaurant.all)
        others.remove(self)  # 从列表中移除自身，防止自己和自己比较
        return sorted(others, key=lambda r: -similarity(self, r))[:k]#[:k]的作用：只返回前k个，通过切片实现，不返回所有其他餐馆的列表
    
# ✅ 需要先创建实例！
r1 = Restaurant("Thai Delight", 2)
r2 = Restaurant("Thai Basil", 3)
r3 = Restaurant("Top Dog", 5)

# ✅ similarity 函数
def similarity(r1, r2):
    return -abs(r1.stars - r2.stars)  # 星级差距越小，越相似

print(r1.similar(2, similarity))




#设计一个 Restaurant 类，并通过比较评价者（reviewers）来判断两家餐厅的相似性，找出与某家餐厅最相似的 K 家餐厅。

#🧮 相似度函数定义
def reviewed_both(r1, r2):
    return len(set(r1.reviewers) & set(r2.reviewers))

#🧱 类定义部分
class Restaurant:
    all = []

    def __init__(self, name, stars, reviewers):
        self.name = name
        self.stars = stars
        self.reviewers = reviewers
        Restaurant.all.append(self)

    def similar(self, k, similarity=reviewed_both):
        """Return the K most similar restaurants to SELF."""
        others = Restaurant.all
        others.remove(self)
        different = lambda r: -similarity(r, self)
        return sorted(others, key=different)[:k]

    def __repr__(self):
        return '<' + self.name + '>'
    
#🔁 数据读取部分
import json

reviewers_for_restaurant = {}

# 读取 reviews.json
for line in open('reviews.json'):
    r = json.loads(line)
    biz = r['business_id']
    if biz not in reviewers_for_restaurant:
        reviewers_for_restaurant[biz] = [r['user_id']]
    else:
        reviewers_for_restaurant[biz].append(r['user_id'])

# 读取 restaurants.json 并创建 Restaurant 对象
for line in open('restaurants.json'):
    r = json.loads(line)
    reviewers = reviewers_for_restaurant[r['business_id']]
    Restaurant(r['name'], r['stars'], reviewers)


#🔍 餐厅搜索与打印
results = search('Thai')

for r in results:
    print(r.name, 'shares reviewers with', r1.similar(3))