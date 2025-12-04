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
-- 预期结果: 6
SELECT count(*) FROM animals;

-- 5. 综合练习：腿最多的动物和最轻的动物的差值是多少？(Max - Min)
-- 预期结果: -6
SELECT max(legs) - min(weight) FROM animals;


-- 6. 综合练习：除了霸王龙以外，腿最少的动物有几条腿？(Min with WHERE)
-- 预期结果: 2
SELECT min(legs), max(weight) FROM animals
WHERE kind <> "t-rex";

-- 7. 额外练习题目：平均每只动物有多少条腿？(Avg)
-- 预期结果: 3.0
SELECT avg(legs) FROM animals;

-- 8. 额外练习题目：动物种类有多少种？(Count Distinct)
-- 预期结果: 6
SELECT count(kind) FROM animals

-- 9. 计算行数
-- 预期结果: 6
SELECT count(*) FROM animals;

-- 10. 计算不同腿数的种类数
-- 预期结果: 2
SELECT count(distinct legs) FROM animals;
-- 11. 计算不同重量的总和
-- 预期结果: 12146
SELECT sum(distinct weight) FROM animals;



-- 1. 准备数据
DROP TABLE IF EXISTS animals;
CREATE TABLE animals AS
  SELECT "dog" AS kind, 4 AS legs, 20 AS weight UNION
  SELECT "cat"        , 4        , 10           UNION
  SELECT "ferret"     , 4        , 10           UNION
  SELECT "parrot"     , 2        , 6            UNION
  SELECT "penguin"    , 2        , 10           UNION
  SELECT "t-rex"      , 2        , 12000;

-- Test 1: 有意义 (谁最重？) -> 预期: t-rex
SELECT max(weight), kind FROM animals;

-- Test 2: 模棱两可 (谁腿最多？) -> 预期: dog (因为它是第一个由4条腿的)
SELECT max(legs), kind FROM animals;

-- Test 3: 无意义 (平均体重的代表是谁？) -> 预期: 这里的 kind 是随机且无意义的
SELECT avg(weight), kind FROM animals;