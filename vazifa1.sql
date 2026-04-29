+------+--------------+-------------+-------+----------+------------+
| id   | product_name | category    | price | quantity | sale_date  |
+------+--------------+-------------+-------+----------+------------+
|    1 | Laptop       | Electronics |   800 |        2 | 2025-01-01 |
|    2 | Phone        | Electronics |   600 |        3 | 2025-01-01 |
|    3 | TV           | Electronics |   900 |        1 | 2025-01-02 |
|    4 | Headphones   | Electronics |   150 |        5 | 2025-01-03 |
|    5 | Table        | Furniture   |   300 |        1 | 2025-01-01 |
|    6 | Chair        | Furniture   |   100 |        4 | 2025-01-02 |
|    7 | Sofa         | Furniture   |  1200 |        1 | 2025-01-03 |
|    8 | Bed          | Furniture   |   900 |        1 | 2025-01-04 |
|    9 | T-shirt      | Clothing    |    40 |        6 | 2025-01-01 |
|   10 | Jeans        | Clothing    |    70 |        3 | 2025-01-02 |
|   11 | Jacket       | Clothing    |   120 |        2 | 2025-01-03 |
|   12 | Shoes        | Clothing    |    90 |        4 | 2025-01-04 |
|   13 | Apple        | Food        |     2 |       20 | 2025-01-01 |
|   14 | Bread        | Food        |     3 |       15 | 2025-01-02 |
|   15 | Milk         | Food        |     4 |       10 | 2025-01-03 |
|   16 | Cheese       | Food        |     8 |        5 | 2025-01-04 |
|   17 | Notebook     | Stationery  |     5 |       10 | 2025-01-01 |
|   18 | Pen          | Stationery  |     2 |       25 | 2025-01-02 |
|   19 | Marker       | Stationery  |     4 |       12 | 2025-01-03 |
|   20 | Folder       | Stationery  |     6 |        8 | 2025-01-04 |
+------+--------------+-------------+-------+----------+------------+


-- 1-masala
select category, sum(quantity) as sotilgan from sales group by category;
+-------------+----------+
| category    | sotilgan |
+-------------+----------+
| Electronics |       11 |
| Furniture   |        7 |
| Clothing    |       15 |
| Food        |       50 |
| Stationery  |       55 |
+-------------+----------+


-- 2-masala
select category, sum(price * quantity) as summa from sales group by category;
+-------------+-------+
| category    | summa |
+-------------+-------+
| Electronics |  5050 |
| Furniture   |  2800 |
| Clothing    |  1050 |
| Food        |   165 |
| Stationery  |   196 |
+-------------+-------+


-- 3-masala
select category, avg(price) as avg from sales group by category;
+-------------+-------+
| category    | avg   |
+-------------+-------+
| Electronics | 612.5 |
| Furniture   |   625 |
| Clothing    |    80 |
| Food        |  4.25 |
| Stationery  |  4.25 |
+-------------+-------+


-- 4-masala
select sale_date, sum(price * quantity) as Daromad from sales group by sale_date;
+------------+---------+
| sale_date  | Daromad |
+------------+---------+
| 2025-01-01 |    4030 |
| 2025-01-02 |    1605 |
| 2025-01-03 |    2278 |
| 2025-01-04 |    1348 |
+------------+---------+


-- 5-masala
select category, sum(price * quantity) as summa from sales group by category limit 1;
+-------------+-------+
| category    | summa |
+-------------+-------+
| Electronics |  5050 |
+-------------+-------+


-- 6-masala
select category, sum(price * quantity) as summa from sales group by category having summa > 2000;
+-------------+-------+
| category    | summa |
+-------------+-------+
| Electronics |  5050 |
| Furniture   |  2800 |
+-------------+-------+


-- 7-masala
select category, avg(price) as avg
    -> from sales
    -> group by category
    -> having avg > 100;
+-------------+-------+
| category    | avg   |
+-------------+-------+
| Electronics | 612.5 |
| Furniture   |   625 |
+-------------+-------+


-- 8-masala
select sale_date, sum(quantity) from sales group by sale_date having sale_date = "2025-01-01";
+------------+---------------+
| sale_date  | sum(quantity) |
+------------+---------------+
| 2025-01-01 |            42 |
+------------+---------------+


-- 9-masala
select category, sum(quantity) as sold from sales group by category order by sold DESC limit 1;
+------------+------+
| category   | sold |
+------------+------+
| Stationery |   55 |
+------------+------+


-- 10-masala
select category, SUM(price * quantity) as total FROM sales WHERE quantity > 3 GROUP BY category;
+-------------+-------+
| category    | total |
+-------------+-------+
| Electronics |   750 |
| Furniture   |   400 |
| Clothing    |   600 |
| Food        |   165 |
| Stationery  |   196 |
+-------------+-------+