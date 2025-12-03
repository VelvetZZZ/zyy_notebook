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