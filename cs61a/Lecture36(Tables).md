# Joining Tables (多表连接)
## I. 基础数据构建 (Data Setup)
- 在进行复杂查询之前，PPT 首先展示了如何利用 UNION 构建两张基础数据表。
1. Dogs 表 (属性表)这张表描述了狗狗的个体特征，包含名字 (name) 和毛发 (fur)。
```SQL
create table dogs as
  select "abraham" as name, "long" as fur union
  select "barack"         , "short"      union
  select "clinton"        , "long"       union
  ...
  select "herbert"        , "curly";
```
2. Parents 表 (关系表)这张表描述了实体间的连接，包含父母 (parent) 和孩子 (child)。
```SQL
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  ...;
```
## II. 核心机制: The Join (连接原理)
- 这是 SQL 声明式编程中最强大的功能之一：如何处理多张表。
### 逗号的含义 (Cartesian Product)
- PPT 核心定义："Two tables A & B are joined by a comma to yield all combos of a row from A & a row from B"
1. 语法：`FROM table_A, table_B`
2. 实质：笛卡尔积 (Cartesian Product)。
3. 效果：系统会将 A 表的每一行与 B 表的每一行进行强制配对，生成一个包含所有可能组合的“超级大表”。此时数据包含大量无意义的配对。
### 命名假设 (Naming Convention)
1. 前提：PPT 字幕提示，当前阶段假设所有列名在不同表中是唯一的 (Unambiguous)。
2. 现状：`dogs (name, fur)` vs `parents (parent, child)`。没有重名列，可以直接引用。

## III. 实践应用: 筛选与查询 (Filtering)

### 目标任务："Select the parents of curly-furred dogs" (选出所有卷毛狗的父母)。

#### 1. 逻辑三部曲
为了从混乱的“全组合”中提取有效信息，我们需要执行三个步骤：
1. Source (来源): 锁定涉及的两张表。
2. Bridge (搭桥): 定义两张表如何关联 (Join Condition)。
3. Filter (过滤): 定义具体的筛选条件 (Filter Condition)。

#### 2. 完整代码结构 
完整的逻辑实现如下：
```SQL
select parent             -- 目标：输出父母的名字
from parents, dogs        -- 1. 来源：全排列组合
where child = name        -- 2. 搭桥：parents表的"孩子" = dogs表的"名字"
and fur = "curly";      -- 3. 过滤：只保留卷毛狗
```
3. 关键逻辑辨析在写 WHERE 子句时，方向至关重要：

- 场景 A (本题)：找卷毛狗的父母 ---->意味着孩子是卷毛 ----> where child = name。
- 场景 B (反向)：找长毛狗的孩子 -----> 意味着父母是长毛 ------>where parent = name。





# Aliases and Dot Expressions 别名与点表达式
## Self-Joins (自连接)
*Declarative Programming (SQL) 核心挑战*：当我们需要找出同一张表内部实体之间的关系（如：兄弟姐妹、祖孙）时，普通的单表查询无法满足需求。

### I. 核心概念：别名与克隆 (Aliases)

#### 1. 为什么需要自连接？
有时我们需要比较同一张表中的两行数据。
    例如，为了找到“兄弟姐妹”，我们需要比较两个孩子及其父母，而这些信息都存储在同一张 parents 表中。

#### 2. 语法：创建“分身”
既然 SQL 不知道如何区分“第一次用这张表”和“第二次用这张表”，我们需要使用**AS**关键字给它们起别名。

```SQL
FROM parents AS a, parents AS b
```
1. 含义：想象我们把 parents 表复印了两份，一份贴上标签 A，另一份贴上标签 B。

2. 点表达式 (Dot Expressions)：现在我们用 a.child 指代表 A 里的孩子，用 b.child 指代表 B 里的孩子，从而消除歧义 (Disambiguate)。

### II. 案例分析 1：寻找兄弟姐妹 (Siblings)
- 目标：找出所有拥有同一个父母的孩子对 (Pairs of siblings)。

#### 1. 逻辑拆解
- 数据源：两份 parents 表 (a 和 b)。
- 条件 A (同一父母)：a.parent 必须等于 b.parent。
- 条件 B (去重与排序)：这是一个经典考点。
    - 如果只写 !=，会出现 (Barack, Clinton) 和 (Clinton, Barack) 这种重复数据。
    - 使用 < (字母序小于) 可以强行规定顺序，既避免了自己连自己，也避免了重复配对。

#### 2. 代码实现
```SQL
SELECT a.child AS first, b.child AS second
FROM parents AS a, parents AS b
WHERE a.parent = b.parent  -- 核心：拥有相同的父母
    AND a.child < b.child; -- 技巧：利用字母序去重，并排除自己
```
#### 运行结果示例：
 | First | Second | 说明 | | :--- | :--- | :--- | | barack | clinton | 都是 abraham 的孩子，且 'b' < 'c' | | abraham | delano | 都是 fillmore 的孩子 |

## III. 案例分析 2：寻找祖父母 (Grandparents)

- 目标：找出祖孙三代关系 (Grandparents -> Grandchildren)。

### 1. 逻辑拆解 (接力赛模型)
这是多步关系的典型应用。

- 第一棒 (表 a)：证明 X 是 Y 的父母。

- 第二棒 (表 b)：证明 Y 是 Z 的父母。

- 交接点：表 a 的“孩子”必须是表 b 的“父母”。