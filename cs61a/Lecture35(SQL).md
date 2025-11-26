# SQL - Declarative Programming
命令式编程、SQL 基本语法

## I. 核心概念：数据库的世界观
在学习 SQL 之前，首先建立对数据存储形式的认知 (Table-based)。

### 1. 数据的组织结构 (Structure)
* **Table (表)**：数据的容器，是记录的集合 (Collection of records)。
* **Column (列)**：数据的**属性**。
    * 每一列都有 **Name (名称)** 和 **Type (类型)**（例如：Latitude 列只能存数字）。
* **Row (行)**：数据的**实体**，也称为 **Record (记录)**。
    * 每一行在每一列上都必须有一个对应的值。

> **CS 视角类比**：
> * `Table` $\approx$ List of Objects
> * `Column` $\approx$ Class Attributes
> * `Row` $\approx$ Instance (Object)

## II. 编程范式对比 (Paradigms)
这是本节课的理论核心，理解**思维方式**的转变。

### 1. Imperative (命令式)
* **代表语言**：Python, C, Java
* **核心思维**：**How to do it** (怎么做)
* **控制权**：程序员控制流程 (Control Flow: loops, if-else)。
* **生活类比**：**菜谱** —— “先切肉，再热油，炒5分钟”。

### 2. Declarative (声明式)
* **代表语言**：**SQL**, Prolog
* **核心思维**：**What I want** (我要什么)
* **控制权**：解释器 (Interpreter) 决定如何执行和优化。
* **生活类比**：**菜单** —— “我要一盘五分熟的牛排”（不关心厨师怎么做）。

## III. SQL 代码实例解析
通过 CS61A 的 `Cities` 例子，理解 SQL 如何处理逻辑。

### 1. 基础语法：Create Table
```sql
create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,             71,               "Cambridge"        union
  select 45,             93,               "Minneapolis";
  ```

- select ... as ...：这里不是查询，而是声明静态数据。

- union：将独立的行拼接 (Combine) 成一个完整的表。

## 2. 逻辑判断：Select & Union
在 SQL 中没有 if-else，我们通过 ** 集合拼接**来实现条件分类。

目标：经度>=115 标记为 "west coast"，否则标记为 "other"。

```SQL
select "west coast" as region, name from cities where longitude >= 115
union
select "other"      as region, name from cities where longitude < 115;
```
### 实现原理：

#### Literal Projection (常量投影)：
select "west coast" as region。

我们在查询结果中凭空创造了 region 这一列，并强制填入 "west coast"。

#### 分治策略：
先筛选出符合条件的子集 (Sub-set)。

再筛选出不符合条件的子集。

最后用 union 把两个子集合二为一。




# SQL Overview
SQL 语言概览、核心语句与课程设定

## I. 语言特性：标准与方言 (Standard vs. Variants)
SQL (Structured Query Language) 的生态现状。

### 1. 官方标准 (ANSI/ISO)
* SQL 拥有一套国际通用的核心语法标准。
* 这意味着诸如 `SELECT`, `WHERE` 等基础关键字在任何数据库中都是通用的。

### 2. 实现差异 (Variants)
* 不同的 **DBMS** (数据库管理系统，如 MySQL, PostgreSQL, Oracle) 都会在标准之上实现自己的“方言”或特性。
* **CS61A 课程环境**：我们使用的是 **SQLite**。这是一个轻量级、无服务器的数据库引擎，它的某些语法特性与其他数据库可能略有不同。

## II. 核心语句 (Statements)
CS61A 侧重于数据的查询与转换，而非数据库运维。

### 1. SELECT 语句 (重点)
> *"A select statement creates a new table"*
* **地位**：这是 SQL 中最重要的操作，占据了课程 90% 的内容。
* **闭包性质 (Closure Property)**：
    * `SELECT` 的输入是表，**输出结果也是一张表**。
    * 这意味着查询结果可以被再次查询 (Sub-queries)。
* **数据来源**：
    1.  **From Scratch (凭空创造)**：直接定义数据生成表（如上一页的 `select 38 as...`）。
    2.  **Projecting (投影/映射)**：从现有的表中筛选列或计算新值。

### 2. CREATE TABLE 语句
* **作用**：给一个表分配一个**全局名称 (Global Name)**。
* **类比**：如果说 `SELECT ...` 是计算一个表达式的值，那么 `CREATE TABLE T AS SELECT ...` 就相当于编程语言中的变量赋值 (`T = ...`)，让数据持久化，供后续引用。

### 3. 其他语句
* 存在 `INSERT` (增), `UPDATE` (改), `DELETE` (删) 等操作，但不是本节课的重点。

## III. 课程设定：Today's Theme
PPT 下方的狗的照片不仅仅是装饰，它是接下来的核心数据集。

### 1. The "Dogs" Dataset
* 课程将引入一个关于“狗”的关联表 (Parents table)。
* **学习目标**：通过查询狗的家族关系（祖父母、兄弟姐妹），练习 **Joins (表连接)** 和 **Recursion (递归查询)**。

### 2. 解释器原理
* 只要一张纸的代码量就能实现一个 `SELECT` 语句的解释器。这暗示了 SQL 声明式语法背后的实现逻辑其实非常优雅且精简。

# Selecting Value Literals
如何使用 SQL 构建静态数据表及层级关系

## I. 基本语法规则
### 1. 列的定义
一个 `SELECT` 语句包含一系列用逗号分隔的列描述：
* **语法**：`select [表达式] as [列名]`
* **示例**：`select "abraham" as parent`
    * `"abraham"` 是 **Literal (字面量)**，即写死的固定值。
    * `parent` 是我们给这列起的列名。

### 2. 行的拼接 (Union)
* 单独的一个 `SELECT` 语句只能生成一行数据。
* 使用 **`UNION`** 关键字将多个 `SELECT` 语句的结果合并，从而构建多行表格。

## II. 实例分析：家族树 (Family Tree)
这页 PPT 展示了如何用二维表来表示树形结构。

### 1. 代码逻辑
```sql
select "abraham" as parent, "barack" as child union
select "abraham"          , "clinton"       union
select "delano"           , "herbert"       union
select "fillmore"         , "abraham"       ...
```
- 第一行：定义了列名为 parent 和 child。

- 后续行：不需要再写 as parent，SQL 会自动对齐第一行的列名。

### 2. 结构映射 (Data Structure)
SQL 表：存储的是一对对的 (parent, child) 连线。

可视化：这些连线组成了右图的树状结构。

Fillmore 指向 Abraham

Abraham 指向 Barack

结论：扁平的 SQL 表可以存储复杂的层级/递归数据结构。


# Naming Tables
SQL 的持久化存储与变量赋值

## I. 两种使用模式 (Modes of Usage)
理解 SQL 执行结果的生命周期。

### 1. 交互式 (Interactive)
* **行为**：当你仅执行 `SELECT` 语句时，SQL 充当计算器或查询工具。
* **结果**：数据被计算出来，展示在屏幕（标准输出）上，然后立即被**丢弃**。
* **局限**：你无法在后续的查询中引用这次的结果。

### 2. 持久化 (Stored)
* **行为**：为了保存查询结果供后续使用，必须给结果集起一个**全局名称 (Global Name)**。
* **语法**：
    ```sql
    create table [表名] as [select 语句];
    ```

## II. CS 视角的深度类比 (The Analogy)
作为 CS 学生，用 Python 的概念来理解 SQL 会非常透彻。

| 概念 | Python 代码 | SQL 代码 |
| :--- | :--- | :--- |
| **求值 (Evaluation)** | `3 + 5` <br> (算出 8，但不保存) | `select 3 + 5;` <br> (生成一行一列的表，不保存) |
| **赋值 (Assignment)** | `x = 3 + 5` <br> (将结果绑定到变量名 x) | `create table x as select 3 + 5;` <br> (将结果绑定到表名 x) |

> **核心洞察**：
> 在 SQL 中，`CREATE TABLE table_name AS ...` 本质上就是**变量赋值**操作。被赋值的对象（右值）必须是一个表（由 `SELECT` 生成），赋给的变量（左值）就是表名。

## III. 实践应用：Parents 表
PPT 中的代码构建了本课程最重要的基础数据集。

### 1. 代码结构
```sql
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham",           "clinton"         union
  ...
  select "eisenhower",        "fillmore";
```
### 2. 意义
通过 CREATE TABLE，我们把那一长串 UNION 拼接出的逻辑结构，固化成了一张名为 parents 的物理表。

后续复用：在接下来的课程中（Join, Recursion），我们可以直接写 select * from parents ...，而不需要每次都重新定义这一堆数据。
