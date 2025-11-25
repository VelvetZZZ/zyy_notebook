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