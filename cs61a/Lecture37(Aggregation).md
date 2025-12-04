# Aggregate Functins 聚合函数
 > 在此之前，所有的 SQL 表达式一次只处理一行数据 (single row at a time)。聚合函数则是 SQL 中用于处理**数据集合**的工具，它能从一组行 (a group of rows) 中计算出一个单一的汇总值。

## 1. 基础数据构建
为了演示聚合计算，PPT 首先构建了一个包含动物种类、腿数和体重的`animals`表。

```SQL
create table animals as
  select "dog" as kind, 4 as legs, 20 as weight union
  select "cat"        , 4        , 10           union
  select "ferret"     , 4        , 10           union
  select "parrot"     , 2        , 6            union
  select "penguin"    , 2        , 10           union
  select "t-rex"      , 2        , 12000;
```

## 2. 核心操作演示
- 聚合函数不仅仅是查看数据，而是对一列数据进行数学统计。 例如，找出所有动物中“腿最多”的数量：

```SQL
-- 计算 legs 列的最大值
select max(legs) from animals;

-- 输出结果: 4
```

## 3. 常用函数扩展
除了求最大值 (max)，字幕中还提到了其他几种最常用的聚合操作，它们都可以对整列数据进行“降维打击”：

- max(column): 求最大值 (Maximum)。

- min(column): 求最小值 (Minimum)。

- sum(column): 求总和 (Summation)。

- count(*): 统计行数 (Count rows)。





# Mixing Aggregates (混合查询)
 > 核心问题：当我们把“聚合函数”（如 max）和“普通列”（如 kind）放在同一个 SELECT 语句中时，数据库是如何决定显示哪一行数据的？

## I. 机制原理

- 在 SQLite 中，如果聚合函数（如 max 或 min）能够锁定特定的某一行，那么随后的普通列就会显示那一行的数据。
    > "An aggregate function also selects a row in the table, which may be meaningful."

## II. 三种结果分类

### 1. 有意义的结果 (Meaningful) ✅
当极值（最大/最小）在表中是唯一的时候，查询结果非常准确。
- 代码：select max(weight), kind ...

- 逻辑：只有 T-Rex 是 12000。

- 结果：12000 | "t-rex"

- 解读：最重的动物就是霸王龙。

### 2. 模棱两可的结果 (Ambiguous) ⚠️
当极值由多行共享时，结果具有随机性。
- 代码：select max(legs), kind ...

- 逻辑：Dog, Cat, Ferret 都是 4 条腿。

- 结果：4 | "dog" (SQLite 通常返回遇到的第一行)。

- 解读：虽然找到了最多的腿数，但显示的动物只是“拥有 4 条腿的动物之一”，不代表全部。

### 3. 无意义的结果 (Meaningful Value? No.) ❌
当聚合函数计算的是一个不存在于原表中的数值（如平均值）时。
- 代码：select avg(weight), kind ...

- 逻辑：平均值是一个虚拟数字，没有任何一只动物对应这个体重。

- 结果：2009.33 | "dog" (完全随机的行)。

- 解读：这里的 kind 是没有任何参考价值的噪音数据。

### 避坑指南
如果你用 MAX 或 MIN，通常是想找“那个最大/最小的是谁”，这通常没问题（只要考虑平局情况）。

如果你用**SUM 或 AVG（平均）**，千万不要在后面加**普通列名（如 name 或 kind）**，因为那个结果是毫无逻辑的。



# Grouping Rows (分组聚合)
 > 核心逻辑：将数据表按特定特征“分桶”，然后在每个桶内部独立进行聚合计算。

## I. 语法结构
```SQL
SELECT [column], [aggregate_function]
FROM [table]
GROUP BY [expression];
```
## II. 执行流程 (Visual Walkthrough)

- 以 `SELECT legs, max(weight) FROM animals GROUP BY legs;` 为例
1. 识别组 (Identify Groups):
- SQL 扫描`GROUP BY`指定的`legs`列。发现两个唯一值 (Unique Values)：4 和 2。

2. 分桶 (Group Rows):
- 所有`legs=4`的行被归为一组`(Dog, Cat, Ferret)`。
- 所有`legs=2`的行被归为一组 `(Parrot, Penguin, T-Rex)`。

3. 组内聚合 (Aggregate per Group):
在` 4-legs` 组 中计算 `max(weight)` ----> 20。在`2-legs`组 中计算`max(weight)`-----> 12000。
- 输出结果:
| legs | max(weight) | | :--- | :--- | | 4 | 20 | | 2 | 12000 |

## III. 关键规则
- 行数决定因素：结果表的**行数**等于 `GROUP BY` 表达式中唯一值 (Unique Values) 的数量。

- 列的选择：在 `SELECT` 中，除了聚合函数外，通常只能放被用来分组的那一列（例如这里的 legs）。如果放了其他列（如 kind），可能会导致上一页提到的“模棱两可”问题。



# Selecting Groups (HAVING 子句)

- 核心概念：`HAVING`子句用于**过滤分组后的数据集**，它通常与聚合函数（如 count, sum, max）配合使用。

## I. 语法结构

```SQL
SELECT [columns] 
FROM [table] 
GROUP BY [expression] 
HAVING [expression]; -- 注意：HAVING 在 GROUP BY 之后
```

## II. 执行逻辑四步走

- 以 `SELECT weight/legs, count(*) ... GROUP BY weight/legs HAVING count(*)>1`为例：


1. `Calculate`: 计算分组键值 (如 weight/legs)。

- 注意：SQLite 整数除法 10/4 = 2。

2. `Group`: 将具有相同键值的行归并到同一个“桶”中。
    - Group 5: {Dog, Penguin}
    - Group 2: {Cat, Ferret}
    - Group 3: {Parrot}
    - Group 6000: {T-Rex}

3. `Aggregate`: 计算每个组的统计信息。
    - Group 5 count: 2
    - Group 3 count: 1 ...

4. `Filter (HAVING)`: 剔除不满足条件的组。
    - 条件 count(*) > 1 剔除了 Parrot 和 T-Rex 组。

## III. 关键区别：WHERE vs HAVING
`WHERE`: 过滤原始数据行 (Filters the set of rows before aggregation).

`HAVING`: 过滤聚合后的组 (Filters the set of groups that are aggregated).