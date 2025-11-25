create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,             71,               "Cambridge"        union
  select 45,             93,               "Minneapolis";

select * from cities;

create table parent as
    select "abraham" as parent, "barack" as child union 
    select "abraham",           "clinton"         union
    select "delano",            "herbert"         union
    select "fillmore",          "abraham"         union
    select "fillmore",          "delano"          union
    select "fillmore",          "grover"          union
    select "eisenhower",        "fillmore";                   
    select * from parent;