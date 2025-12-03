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

### 2. 代码实现
```SQL
SELECT a.parent AS grandog,    -- 爷爷 (第一代的父母)
       b.child AS grandpup     -- 孙子 (第二代的孩子)
FROM parents AS a, parents AS b
WHERE a.child = b.parent;      -- 核心桥梁：爸爸是爷爷的孩子，同时也是孙子的爸爸
```

## 学习心得 / 复习要点
1. 自连接本质：就是 JOIN 操作的一种特殊情况，只是左表和右表是同一个。

2. a.child < b.child 的妙用：在处理“成对组合”问题时，永远记住用<来避免重复和自匹配。

3. 连接方向：

    - 找兄弟 (平级)：WHERE a.parent = b.parent (共用上级)

    - 找祖孙 (层级)：WHERE a.child = b.parent (链式传递)


# I. 数值表达式 (Numerical Expressions)
## 1. 基本能力
SQL 表达式不仅可以引用列名，还可以包含函数调用和算术运算符。
- 语法结构：
```SQL
SELECT [expression] AS [name], [expression] AS [name] ...
```
## 2. 常用操作符
- 算术 (Arithmetic): `+, -, *, /, % (取模), and, or`

- 数学函数 (Functions): `abs (绝对值), round (四舍五入)`

- 比较 (Comparison):

`<, <=, >, >=`

`<> 或 != (不等于)`

`= (等于) `: ⚠️ 注意：SQL 中没有变量赋值的概念，所以单等号 = 专门用于判断相等，不使用 ==。

## II. 实战案例：计算距离 (Distances)
- 目标：基于经纬度数据，计算两个城市之间的纬度距离。

### 1. 数据源：`cities 表`
包含城市名称及其地理坐标。
```SQL
CREATE TABLE cities AS
  SELECT 38 AS latitude, 122 AS longitude, "Berkeley" AS name UNION
  SELECT 42,             71,               "Cambridge"      UNION
  SELECT 45,             93,               "Minneapolis"    UNION
  ...;
```

### 2. 计算逻辑：distances 表
利用**自连接 (Self-Join)** 和 **数值运算**。
- 公式：$Distance = 60 \times (Lat_2 - Lat_1)$
- 代码逻辑：
```SQL
CREATE TABLE distances AS
  SELECT a.name AS first, b.name AS second,
         60 * (b.latitude - a.latitude) AS distance
  FROM cities AS a, cities AS b;
```
- 解释：这将生成一个包含所有城市对之间距离的表（笛卡尔积）。如果 cities 有 $N$ 行，distances 将有 $N^2$ 行。

#### AS的不同作用：
| 位置       | 代码片段                     | 作用            | 含义                                           |
|------------|------------------------------|-----------------|------------------------------------------------|
| 在表名后   | `CREATE TABLE distances AS ...` | 定义来源        | “这个表的数据**来源于**后面的查询”              |
| 在列名后   | `SELECT a.name AS first`       | 起外号 (Alias) | “把这一列在结果中**改名**叫 `first`”             |
| 在 FROM 后 | `FROM cities AS a`             | 起外号 (Alias) | “把这张表在代码里**简称为** `a`”                 |



# String Expressions (字符串处理)
- 核心痛点：SQL 的字符串处理逻辑与 Python 完全不同，容易在索引和切片上踩坑。

## I. 基础语法对照 (Python vs SQL)
| 功能 (Function) | Python 写法 | SQL 写法 | 备注 |
|----------------|-------------|----------|------|
| 拼接 (Combine) | `"a" + "b"` | `"a" || "b"` | — |
| 索引 (Indexing) | 从 0 开始 | 从 1 开始 | SQL 的第 1 个字符就是 index 1 |
| 切片 (Slicing) | `[start:end]` | `substr(str, start, length)` | SQL 的第 3 个参数是**长度**，不是结束位置 |

### II. 核心函数详解

1. `substr(string, start, length)`
- 含义：取子字符串 (Substring)。

- 参数：
    - string: 要操作的字符串。
    - start: 起始位置（记得从 1 数起）。
    - length: 要拿几个字符。

2. `instr(string, substring)`
- 含义：查找位置 (In-string)。

- 功能：返回子字符串第一次出现的索引位置。

- 示例：
```SQL
instr("hello, world", " ")
-- 返回 7 (因为空格在第 7 位)
```

### III. 难点代码深度拆解 (The "low" Example)
PPT 中展示了一个复杂的嵌套例子，用来得到单词 "low"。

#### 原始代码：
```SQL
-- 假设表 phrase 中有一列 s 内容为 "hello, world"
select substr(s, 4, 2) || substr(s, instr(s, " ")+1, 1) from phrase;
```
#### 逻辑推演步骤：
1. 前半部分：`substr("hello, world", 4, 2)`
- 数一数：h(1)-e(2)-l(3)-l(4)-o(5)...
- 动作：从第 4 位开始，拿 2 个字符。
- 结果："lo"

2. 后半部分：
- 先找位置：`instr("hello, world", " ")` -----> 找到空格在第 7 位。
- 计算起点：7 + 1 = 8。第 8 位是字符 'w'。取字符：substr(..., 8, 1) ----> 从第 8 位开始，拿 1 个字符。
- 结果："w"

3. 最终拼接："lo" || "w" -----> "low"

### IV. 进阶案例：解析列表 (List Parsing)
PPT 的最后一个例子展示了如何手动解析类似 "one,two,three" 这样的字符串。

```SQL
-- 假设 cdr 为 "two,three,four"
select substr(cdr, 1, instr(cdr, ",") - 1) ...
```

1. 逻辑拆解：
- 目标：想取出第一个逗号前的单词（即 "two"）。
- 找逗号：instr(cdr, ",") 发现逗号在第 4 位。算长度：逗号在第 4 位，说明前面的单词长度是 $4 - 1 = 3$。
- 取值：substr(cdr, 1, 3)----->从头拿 3 个字------->"two"。

⚠️ 教授的警告"Strings can be used to represent structured values, but doing so is rarely a good idea"含义：虽然 SQL 既然能硬解字符串，但千万别这么做！如果数据是列表，应该把它们拆分存到不同的行（Row）里，而不是塞在一个字符串里。