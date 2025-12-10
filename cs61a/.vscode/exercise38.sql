-- Create table and Drop table
-- Modifying Tables

-- 1. 创建表 `primes`
-- 列 n 是唯一约束 (UNIQUE)，列 prime 默认值为 1 (DEFAULT 1)。
CREATE TABLE primes(n UNIQUE, prime DEFAULT 1);

-- 2. 插入第一批数据 (2, 1) 和 (3, 1)
INSERT INTO primes VALUES (2, 1), (3, 1);

-- 3. 检查数据
SELECT * FROM primes;
-- 预期输出:
-- 2|1
-- 3|1

-- 4. 插入第二批数据 (4, 5), (5, 6), (6, 7)
INSERT INTO primes VALUES (4, 5), (5, 6), (6, 7);

-- 5. 再次检查数据
SELECT * FROM primes;
-- 预期输出:
-- 2|1
-- 3|1
-- 4|5
-- 5|6
-- 6|7

-- 6. 使用 SELECT 语句的结果进行 INSERT
-- 向 primes 表的 n 列插入数据。
-- 数据源是：从 primes 表中选择 n 列的值，然后每个值都 + 6。
-- 新插入的 n 值将是： 2+6=8, 3+6=9, 4+6=10, 5+6=11, 6+6=12。
-- 由于只指定了 n 列，prime 列会使用默认值 1。
INSERT INTO primes(n) SELECT n+6 FROM primes;

-- 7. 检查最终数据 (现在应有 5 + 5 = 10 行记录)
SELECT * FROM primes;
-- 预期输出:
-- 2|1
-- 3|1
-- 4|5
-- 5|6
-- 6|7
-- 8|1
-- 9|1
-- 10|1
-- 11|1
-- 12|1
