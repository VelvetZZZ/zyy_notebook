
# 🧠 2.3 Unsupervised Learning 无监督学习
> 📌 Find something interesting in **unlabeled data**  
> 从没有标签的数据中发现潜在的结构或模式。

---

## 🔍 一、定义 & 目标

**无监督学习**是一类机器学习任务，其目标是在没有提供数据标签（output）的情况下，分析和建模数据的内部结构。

- 📊 数据没有“答案”或“正确结果”
- 🧩 模型尝试**寻找模式、关系或分组**
- 🤯 更像是“让机器自己去理解数据”

---

## 🧭 二、主要任务类型：

| 类型 | 描述 | 示例 |
|------|------|------|
| **Clustering 聚类** | 将数据划分为内部相似、外部差异较大的子集 | 客户细分、新闻分类、基因数据分组 |
| **Dimensionality Reduction 降维** | 把高维数据压缩到更少的维度，保留重要特征 | 图像压缩、数据可视化（如 t-SNE、PCA） |
| **Anomaly Detection 异常检测** | 识别不符合常规的数据点 | 欺诈检测、设备故障预警 |
| **Association Rule Learning** | 找出项之间的共现关系 | 超市购物篮分析（Apriori算法） |

---

## 🤖 三、常见聚类算法（Clustering Algorithms）

| 算法 | 特点 | 适用场景 |
|------|------|----------|
| **K-Means** | 快速、易于实现，需指定簇数K | 图像压缩、市场细分 |
| **DBSCAN** | 不需指定簇数，能发现任意形状的簇，适合带噪声数据 | 空间数据、地理信息聚类 |
| **Hierarchical** | 构建树状结构（dendrogram），可视化清晰 | 文档聚类、层级分析 |
| **Gaussian Mixture Model (GMM)** | 基于概率模型，簇可重叠 | 模型推理、行为建模 |

---

## 🧬 四、Clustering 示例场景

- 🗞 新闻分类（Google News）
- 🧬 基因表达数据聚类（DNA Microarray）
- 🧍‍♂️ 客户画像和用户分群（市场营销）
- 📷 图像分割
- 🧾 文档主题归类

---

## 🧠 五、常见术语解释

| 英文词汇 | 中文释义 | 小技巧记忆 |
|----------|----------|------------|
| **Cluster** | 聚类/簇 | 想成“群组”或“圈圈” |
| **Centroid** | 簇中心点 | 像星系中心一样聚拢点 |
| **Distance Metric** | 距离度量（如欧几里得距离） | 越近越像，越远越不同 |
| **Silhouette Score** | 聚类质量评价指标 | 越接近1越好 |

---

## 🧪 六、学习建议 & 小贴士

- ✅ 理解“没有标签”这个核心前提，算法只能**凭相似性**做判断。
- ✅ 多做可视化分析（如用 matplotlib 或 seaborn），帮助你直观理解聚类效果。
- ✅ 实战中常配合 PCA、t-SNE 做降维后再聚类。
- ✅ 训练不同的聚类算法对比效果，学会评估。

---

## 💡 一句话记住非监督学习

> **无监督学习就像黑暗中摸索结构的探险者，算法不告诉你答案，而是帮你揭示潜在的“组织方式”。**

---

## 📌 示例代码：K-Means 聚类

```python
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

print(kmeans.labels_)
print(kmeans.cluster_centers_)
```

---

> 📘 用 Obsidian 做笔记的你，可以添加 #UnsupervisedLearning #MachineLearning 标签方便管理。
