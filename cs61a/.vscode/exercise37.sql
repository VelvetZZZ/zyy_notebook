-- 1. 创建动物园 (准备数据)
DROP TABLE IF EXISTS animals;
CREATE TABLE animals AS
  SELECT "dog" AS kind, 4 AS legs, 20 AS weight UNION
  SELECT "cat"        , 4        , 10           UNION
  SELECT "ferret"     , 4        , 10           UNION
  SELECT "parrot"     , 2        , 6            UNION
  SELECT "penguin"    , 2        , 10           UNION
  SELECT "t-rex"      , 2        , 12000;

-- 2. PPT 上的例子：谁的腿最多？(Max)
-- 预期结果: 4
SELECT max(legs) FROM animals;

-- 3. 玩点新的：所有动物加起来有多重？(Sum)
-- 预期结果: 12056
SELECT sum(weight) FROM animals;

-- 4. 玩点新的：这里面有几只动物？(Count)
-- 预期结果: 
SELECT count(*) FROM animals;