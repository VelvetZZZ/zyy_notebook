# Create Table and Drop Table
## SQL `CREATE TABLE` 语法详解:
### 1. 核心概念：语法图 (Syntax Diagrams)
![alt text](image-4.png)

#### 如何阅读铁路图？
- 方向：从左向右阅读。
- 圆角框/椭圆 (如 CREATE, TABLE)：关键字。必须原样输入，不能修改。
- 方角框 (如 table-name)：变量。需要替换为自定义的名称。
- 分叉路径：表示 可选 (Optional)。如果不走直线走弯路，代表该部分可以省略（例如 IF NOT EXISTS）。
- 回路/循环：表示 可重复。通常配合逗号使用，表示可以定义多个项（例如定义多个列）。

### 2. CREATE TABLE 主语法结构
```SQL
CREATE [TEMP] TABLE [IF NOT EXISTS] table-name (
    column-def [, column-def]*
    [, table-constraint]*
) [WITHOUT ROWID];
```