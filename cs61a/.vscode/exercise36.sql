-- ==========================================
-- 第一部分：构建数据表 (Data Setup)
-- 对应 PPT 中的 create table 语句
-- ==========================================

-- 1. 创建 dogs 表
-- 包含两列：name (名字), fur (毛发类型)
DROP TABLE IF EXISTS dogs; -- 如果表已存在则删除，防止重复创建报错
CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur UNION
  SELECT "barack",          "short"       UNION
  SELECT "clinton",         "long"        UNION
  SELECT "delano",          "long"        UNION
  SELECT "eisenhower",      "short"       UNION
  SELECT "fillmore",        "curly"       UNION
  SELECT "grover",          "short"       UNION
  SELECT "herbert",         "curly";

-- 2. 创建 parents 表
-- 包含两列：parent (父母), child (孩子)
DROP TABLE IF EXISTS parents;
CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham",           "clinton"         UNION
  SELECT "delano",            "herbert"         UNION
  SELECT "fillmore",          "abraham"         UNION
  SELECT "fillmore",          "delano"          UNION
  SELECT "fillmore",          "grover"          UNION
  SELECT "eisenhower",        "fillmore";

-- ==========================================
-- 第二部分：PPT 代码测试 (Testing)
-- 对应终端截图中的三个查询
-- ==========================================

-- 测试 1: 查看所有“亲子对”以及孩子的毛发特征
-- 逻辑：连接两张表，匹配 child = name
SELECT * FROM parents, dogs 
WHERE child = name;

-- 测试 2: 筛选出“卷毛狗”及其父母的详细信息
-- 逻辑：在上面的基础上，增加 fur = "curly" 的筛选
SELECT * FROM parents, dogs 
WHERE child = name AND fur = "curly";

-- 测试 3: (最终目标) 只输出“卷毛狗父母”的名字
-- 逻辑：只选择 parent 这一列
SELECT parent 
FROM parents, dogs 
WHERE child = name AND fur = "curly";






-- ==========================================
-- 1. 准备基础数据 (Data Setup)
-- ==========================================

DROP TABLE IF EXISTS dogs;
CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur UNION
  SELECT "barack",          "short"       UNION
  SELECT "clinton",         "long"        UNION
  SELECT "delano",          "long"        UNION
  SELECT "eisenhower",      "short"       UNION
  SELECT "fillmore",        "curly"       UNION
  SELECT "grover",          "short"       UNION
  SELECT "herbert",         "curly";

DROP TABLE IF EXISTS parents;
CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham",           "clinton"         UNION
  SELECT "delano",            "herbert"         UNION
  SELECT "fillmore",          "abraham"         UNION
  SELECT "fillmore",          "delano"          UNION
  SELECT "fillmore",          "grover"          UNION
  SELECT "eisenhower",        "fillmore";

-- ==========================================
-- 2. 创建祖父母表 (Grandparents Creation)
-- ==========================================

DROP TABLE IF EXISTS grandparents;
CREATE TABLE grandparents AS
  SELECT a.parent AS grandog, b.child AS grandpup
  FROM parents AS a, parents AS b
  WHERE a.child = b.parent;

-- ==========================================
-- 3. 测试验证 (Verification)
-- 对应截图 image_0e96d9.jpg 中的查询
-- ==========================================

-- 看看 Eisenhower 的孙子辈是谁？
SELECT grandpup FROM grandparents 
WHERE grandog = "eisenhower";



-- ==========================================

-- ==========================================
-- 1. 创建城市表 (Cities Table)
-- 数据来源：Slide example
-- ==========================================
DROP TABLE IF EXISTS cities;
CREATE TABLE cities AS
  SELECT 38 AS latitude, 122 AS longitude, "Berkeley"    AS name UNION
  SELECT 42,             71,               "Cambridge"           UNION
  SELECT 45,             93,               "Minneapolis"         UNION
  SELECT 33,             117,              "San Diego"           UNION
  SELECT 26,             80,               "Miami"               UNION
  SELECT 90,             0,                "North Pole";

-- ==========================================
-- 2. 简单的数值筛选示例 (Cold Cities)
-- 对应 PPT 右侧中间的小例子
-- ==========================================
DROP TABLE IF EXISTS cold;
CREATE TABLE cold AS
  SELECT name FROM cities WHERE latitude >= 43;

-- 查看寒冷城市
SELECT * FROM cold;

-- ==========================================
-- 3. 计算距离表 (Distances Table)
-- 核心：自连接 + 数学运算
-- 60 * (lat_b - lat_a) 粗略模拟纬度距离
-- ==========================================
DROP TABLE IF EXISTS distances;
CREATE TABLE distances AS
  SELECT a.name AS first, b.name AS second,
         60 * (b.latitude - a.latitude) AS distance
  FROM cities AS a, cities AS b;

-- ==========================================
-- 4. 验证测试
-- 对应 PPT 左侧终端的查询：
-- "以 Minneapolis 为起点，去往其他城市的距离，按距离排序"
-- ==========================================
SELECT second, distance 
FROM distances 
WHERE first = "Minneapolis" 
ORDER BY distance;


-- ==========================================
-- 1. 基础字符串拼接 (Basic Concatenation)
-- 对应 PPT 第一个红绿灯示例
-- ==========================================

-- 知识点：SQL 使用双竖线 || 进行拼接，而不是 +
SELECT "hello," || " world" AS greeting;


-- ==========================================
-- 2. 复杂的字符串操作 (Complex Manipulation)
-- 对应 PPT 中间部分：从 "hello, world" 中提取 "low"
-- ==========================================

-- 2.1 准备数据：创建 phrase 表
DROP TABLE IF EXISTS phrase;
CREATE TABLE phrase AS
  SELECT "hello, world" AS s;

-- 2.2 执行复杂查询
-- 逻辑拆解：
-- part1: substr(s, 4, 2) -> 从第4位('l')开始取2个 -> "lo"
-- part2: instr(s, " ")   -> 找空格的位置 -> 7
-- part3: substr(s, 7+1, 1) -> 从第8位('w')开始取1个 -> "w"
-- result: "lo" || "w" -> "low"
SELECT substr(s, 4, 2) || substr(s, instr(s, " ")+1, 1) AS result
FROM phrase;


-- ==========================================
-- 3. 模拟列表解析 (List Parsing)
-- 对应 PPT 底部示例：解析逗号分隔的字符串
-- ==========================================

-- 3.1 准备数据：模拟 Lisp 风格的列表结构
-- car = "one" (第一个元素)
-- cdr = "two,three,four" (剩余的元素)
DROP TABLE IF EXISTS lists;
CREATE TABLE lists AS
  SELECT "one" AS car, "two,three,four" AS cdr;

-- 3.2 提取 cdr 中的第一个元素 (即原本列表的第二个元素)
-- 逻辑拆解：
-- 1. instr(cdr, ",") -> 找到逗号在第 4 位
-- 2. 4 - 1 = 3       -> 计算出单词 "two" 的长度
-- 3. substr(..., 1, 3) -> 从头取 3 个字符 -> "two"
SELECT substr(cdr, 1, instr(cdr, ",") - 1) AS cadr
FROM lists;
