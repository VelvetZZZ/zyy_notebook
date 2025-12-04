# Aggregate Functins 聚合函数
 > 在此之前，所有的 SQL 表达式一次只处理一行数据 (single row at a time)。聚合函数则是 SQL 中用于处理**数据集合**的工具，它能从一组行 (a group of rows) 中计算出一个单一的汇总值。

## 1. 基础数据构建
为了演示聚合计算，PPT 首先构建了一个包含动物种类、腿数和体重的`animals`表。

```SQL
create table animals as
  select "dog" as kind, 4 as legs, 20 as weight union
  select "cat"        , 4        , 10           union
  select "ferret"     , 4        , 10           union
  select "parrot"     , 2        , 6            union
  select "penguin"    , 2        , 10           union
  select "t-rex"      , 2        , 12000;
```

## 2. 核心操作演示
