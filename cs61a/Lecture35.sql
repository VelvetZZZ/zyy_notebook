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