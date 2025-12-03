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
