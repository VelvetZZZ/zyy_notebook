create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,             71,               "Cambridge"        union
  select 45,             93,               "Minneapolis";

select * from cities;

create table parents as
    select "abraham" as parent, "barack" as child union 
    select "abraham",           "clinton"         union
    select "delano",            "herbert"         union
    select "fillmore",          "abraham"         union
    select "fillmore",          "delano"          union
    select "fillmore",          "grover"          union
    select "eisenhower",        "fillmore";                   
    select * from parents;

--Projecting Tables 投影表

create table parents as
    select "abraham" as parent, "barack" as child union 
    select "abraham",           "clinton"         union
    select "delano",            "herbert"         union
    select "fillmore",          "abraham"         union
    select "fillmore",          "delano"          union
    select "fillmore",          "grover"          union
    select "eisenhower",        "fillmore";                   
  
  -- 1. 看看 Abraham 的孩子
  select child from parents where parent = "abraham";

  -- 2. 看看谁的名字比孩子大 (注意体会 fillmore 出现了几次)
  select parent from parents where parent > child;

  -- 3. 玩一下排序 (ORDER BY) - PPT 没写例子但提到了
  -- 试着把所有孩子按字母倒序排列
  select child from parents order by child desc;


  -- Step 1: 准备数据 (构建 ints 表)
-- 这一步模拟了二进制位：one=1, two=2, four=4, eight=8
DROP TABLE IF EXISTS ints;

CREATE TABLE ints AS
  SELECT "zero" AS word, 0 AS one, 0 AS two, 0 AS four, 0 AS eight UNION
  SELECT "one",          1,        0,        0,        0         UNION
  SELECT "two",          0,        2,        0,        0         UNION
  SELECT "three",        1,        2,        0,        0         UNION
  SELECT "four",         0,        0,        4,        0         UNION
  SELECT "five",         1,        0,        4,        0         UNION
  SELECT "six",          0,        2,        4,        0         UNION
  SELECT "seven",        1,        2,        4,        0         UNION
  SELECT "eight",        0,        0,        0,        8         UNION
  SELECT "nine",         1,        0,        0,        8;

-- Step 2: 验证数据 (查看全表)
SELECT * FROM ints;

-- Step 3: 你的神仙解法 (Powers of 2)
-- 逻辑：如果是 2 的幂，那么它只会在某一列上有值，且该值除以该列的权重等于 1。
-- 所有的 "1" 加起来必须等于 1。
SELECT word FROM ints 
WHERE one + two/2 + four/4 + eight/8 = 1;

-- 对比一下：普通人的解法 (枚举法)
-- SELECT word FROM ints WHERE one + two + four + eight IN (1, 2, 4, 8);