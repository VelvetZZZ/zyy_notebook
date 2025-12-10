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