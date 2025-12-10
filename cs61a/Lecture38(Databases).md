# Create Table and Drop Table
# SQL `CREATE TABLE` 语法详解:

## 1. 核心概念：语法图 (Syntax Diagrams)
![alt text](image-4.png)

PPT 中的流程图在计算机科学中被称为 **铁路图 (Railroad Diagrams)**。它是阅读编程语言官方文档的基础技能。

### 如何阅读
- **从左向右**：沿着线条的方向阅读。
- **圆角框/椭圆** (如 `CREATE`, `TABLE`)：**关键字 (Keywords)**。必须原样输入，不能修改。
- **方角框** (如 `table-name`)：**变量 (Variables)**。需要替换为自定义的名称。
- **分叉路径**：表示 **可选 (Optional)**。如果不走直线走弯路，代表该部分可以省略（例如 `IF NOT EXISTS`）。
- **回路/循环**：表示 **可重复 (Repeatable)**。通常配合逗号使用，表示可以定义多个项。

---

## 2. CREATE TABLE 基础语法

根据 PPT 左侧的主路径，基本结构如下：

```sql
CREATE [TEMP] TABLE [IF NOT EXISTS] table-name (
    column-def [, column-def]*
    [, table-constraint]*
) [WITHOUT ROWID];
```
### 2.1 关键组件解析
- `CREATE TABLE`：建表指令起点。

- `IF NOT EXISTS (可选)`：保护性语句。如果表已存在，SQL 引擎会忽略指令而不是报错。

- `table-name`：自定义的表名。

- `(...)`：括号内定义表的具体列结构。

## 3. 列定义与约束 (Column Definition)

### 3.1 语法结构
`列名` -> `类型(可选)` -> `约束(可选)`

### 3.2 常见约束 (Constraints)
约束是给数据立“规矩”，常见类型如下：

- `PRIMARY KEY` (主键)：整行数据的唯一标识，不能重复，不能为空。

- `UNIQUE` (唯一)：该列的值不能重复（例如：身份证号、用户名）。

- `CHECK` (检查)：插入数据时必须满足特定条件（例如：age > 0）。

- `DEFAULT` (默认值)：如果插入数据时未指定该列的值，系统自动填充此默认值。

## 4. 实例代码演示
### 示例 1: 最基础的建表
没有任何约束，最简单的形式。
```sql
CREATE TABLE numbers (n, note);
```
*含义*：创建一个名为 numbers 的表，包含 n 和 note 两列。

### 示例 2: 添加 UNIQUE (唯一) 约束

```sql
CREATE TABLE numbers (n UNIQUE, note);
```
*含义*：n 这一列的值必须是唯一的。如果尝试插入重复的 n 值，数据库会报错。

### 示例 3: 添加 DEFAULT (默认值)
```sql
CREATE TABLE numbers (n, note DEFAULT "No comment");
```
*含义*：

如果你插入时指定了 note：VALUES(1, "Hello") -> note 为 "Hello"

如果你插入时忽略了 note：VALUES(1) -> note 自动填为 "No comment"

**补充：使用 CREATE TABLE 只是造出了一个空的容器（Empty Table）。**

# Drop Table 

## 1. 核心功能
`DROP TABLE` 用于从数据库中**彻底删除**一张表。
* **注意**：这是一个破坏性操作，表结构和表内的所有数据都会被永久移除。

## 2. 语法结构与安全机制

语法图路径：`DROP` -> `TABLE` -> `[IF EXISTS]` -> `表名`

### 2.1 两种写法的区别

#### 写法 A：强制删除 (不推荐在脚本中使用)
```sql
DROP TABLE numbers;
```
*逻辑*：命令数据库直接删除 numbers 表。

*风险*：如果 numbers 表根本不存在，SQL 会报错 (Error)，导致程序中断。

#### 写法 B：安全删除 (推荐)
```sql
DROP TABLE IF EXISTS numbers;
```
*逻辑*：
- 先检查 numbers 表是否存在。
- 如果存在 -> 删除它。
- 如果不存在 -> 忽略该命令，不报错。

*优势*：这种写法被称为“幂等性”操作，无论运行多少次，结果都是安全的，不会导致程序崩溃。

# SQL `INSERT` 语句学习笔记

## I. INSERT 语句概述
`INSERT` 语句用于向数据库的 表 中添加新的 行（记录）。

## II. 语法结构与选项 (基于 Railroad Diagram)

`INSERT` 语句的基本结构是 :
**`INSERT [OR resolution] INTO table_name ...。`**

### A. 冲突处理子句 (OR resolution)
- 在 INSERT 之后可以指定 OR 关键字，以及一个冲突解决动作，用于处理插入操作违反数据库约束（如 PRIMARY KEY 或 UNIQUE）时的情况。

| 动作 (Action) | 描述 (Description) |
|--------------|---------------------|
| OR REPLACE   | 如果发生冲突，删除导致冲突的现有行，然后插入新行。 |
| OR ROLLBACK  | 遇到冲突时，回滚整个事务（中止并撤销所有更改）。 |
| OR ABORT     | 遇到冲突时，中止当前 SQL 语句（默认行为），并回滚该语句所做的更改。 |
| OR FAIL      | 遇到冲突时，中止当前 SQL 语句，但不回滚事务中该语句之前的更改。 |
| OR IGNORE    | 遇到冲突时，忽略该行数据，继续处理后续的插入操作。 |

### B. 目标和数据源
*目标*： `INTO` 后面跟 `table-name`（表名），以及可选的 `(column-name, ...)` 列名列表。

*数据源*：

`VALUES`: 插入明确指定的值列表。

`select-stmt`: 使用 SELECT 语句的结果集作为要插入的数据。

`DEFAULT VALUES`: 插入一行，所有列都使用其定义的默认值（或 NULL）。

### III. 常见用法示例

假设有一个表 `t` 包含两列数据，以下是两种基本的插入方法：

#### A. 插入到指定列

只为表 `t` 中的 `特定列` 插入数据。未指定的列将使用`默认值`或`NULL`。

```sql
INSERT INTO t(column) VALUES (value);
```
#### B. 插入到所有列
为表 `t` 中的 `所有列` 依次提供数据。值的数量必须与表的列数一致。

```sql
INSERT INTO t VALUES (value0, value1);
```
*  *关键点*： 如果你没有指定列名列表，VALUES 中的值将按照表定义的列顺序依次插入。
