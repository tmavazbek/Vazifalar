select * 
from book as b 
inner join author as a on a.id = b.a_id 
inner join genre as g on g.id = b.g_id;
-- +----+-------------------+--------+--------+------+------+----+------------------------+----+----------+
-- | id | name              | price  | amount | a_id | g_id | id | name                   | id | name     |
-- +----+-------------------+--------+--------+------+------+----+------------------------+----+----------+
-- |  4 | Do'st ortirish    |  60000 |     10 |    1 |    1 |  1 | Xudoyberdi To'xtaboyev |  1 | ertak    |
-- |  6 | Binafsha shulasi  | 150000 |     29 |    1 |    2 |  1 | Xudoyberdi To'xtaboyev |  2 | tarixiy  |
-- |  1 | Shaytanat         | 100000 |      4 |    2 |    3 |  2 | Adolfe Hitler          |  3 | badiiy   |
-- |  2 | Ikki eshik orasi  | 150000 |      2 |    2 |    2 |  2 | Adolfe Hitler          |  2 | tarixiy  |
-- |  9 | Mehrobdan chayon  | 150000 |      2 |    2 |    4 |  2 | Adolfe Hitler          |  4 | detektiv |
-- |  5 | Jannatiy odamlar  | 150000 |      2 |    3 |    4 |  3 | Alisher Navoiy         |  4 | detektiv |
-- |  7 | Al - kimyogar     | 150000 |     14 |    3 |    1 |  3 | Alisher Navoiy         |  1 | ertak    |
-- |  8 | Buzrukning kuzi   | 150000 |      5 |    3 |    3 |  3 | Alisher Navoiy         |  3 | badiiy   |
-- |  3 | Devona            |  70000 |      4 |    4 |    3 |  4 | Ahad Qayum             |  3 | badiiy   |
-- | 10 | Dunyoning ishlari | 150000 |     90 |    4 |    2 |  4 | Ahad Qayum             |  2 | tarixiy  |
-- +----+-------------------+--------+--------+------+------+----+------------------------+----+----------+


-- 1-masala 
select a.name, JSON_ARRAYAGG(g.name) as janrlar 
from book as b 
inner join author as a on a.id = b.a_id 
inner join genre as g on g.id = b.g_id 
GROUP by a.id 
having a.name = "Alisher Navoiy";
-- +----------------+---------------------------------+
-- | name           | janrlar                         |
-- +----------------+---------------------------------+
-- | Alisher Navoiy | ["detektiv", "ertak", "badiiy"] |
-- +----------------+---------------------------------+

-- 2- masala
select a.name, JSON_ARRAYAGG(g.name) as janrlar 
from book as b 
inner join author as a on a.id = b.a_id 
inner join genre as g on g.id = b.g_id 
GROUP by a.id;
-- +------------------------+-----------------------------------+
-- | name                   | janrlar                           |
-- +------------------------+-----------------------------------+
-- | Xudoyberdi To'xtaboyev | ["ertak", "tarixiy"]              |
-- | Adolfe Hitler          | ["badiiy", "tarixiy", "detektiv"] |
-- | Alisher Navoiy         | ["detektiv", "ertak", "badiiy"]   |
-- | Ahad Qayum             | ["badiiy", "tarixiy"]             |
-- +------------------------+-----------------------------------+

-- 3-masala 
SELECT a.name , g.name as janrlar, COUNT(*) AS soni
FROM book as b
JOIN author as a ON b.a_id = a.id
JOIN genre as g ON b.g_id = g.id
GROUP BY a.id, g.id;
-- +------------------------+----------+------+
-- | name                   | janrlar  | soni |
-- +------------------------+----------+------+
-- | Xudoyberdi To'xtaboyev | ertak    |    1 |
-- | Xudoyberdi To'xtaboyev | tarixiy  |    1 |
-- | Adolfe Hitler          | badiiy   |    1 |
-- | Adolfe Hitler          | tarixiy  |    1 |
-- | Adolfe Hitler          | detektiv |    1 |
-- | Alisher Navoiy         | detektiv |    1 |
-- | Alisher Navoiy         | ertak    |    1 |
-- | Alisher Navoiy         | badiiy   |    1 |
-- | Ahad Qayum             | badiiy   |    1 |
-- | Ahad Qayum             | tarixiy  |    1 |
-- +------------------------+----------+------+

-- 4=masala
select g.name as janrlar, JSON_ARRAYAGG(b.name)as kitoblar, COUNT(*) as soni 
from book as b 
join author as a on a.id = b.a_id 
join genre as g on g.id = b.g_id 
GROUP by g.name 
order by soni desc limit 1;
-- +---------+--------------------------------------------+------+
-- | janrlar | kitoblar                                   | soni |
-- +---------+--------------------------------------------+------+
-- | badiiy  | ["Shaytanat", "Buzrukning kuzi", "Devona"] |    3 |
-- +---------+--------------------------------------------+------+ 

-- 5-masala
select a.name, g.name as janrlar, COUNT(*) as soni
from book as b 
inner join author as a on a.id = b.a_id 
inner join genre as g on g.id = b.g_id 
GROUP by a.id, g.id;

-- 6-masala
select a.name, sum(b.amount) as sotildi
from book as b 
inner join author as a on a.id = b.a_id 
inner join genre as g on g.id = b.g_id 
GROUP by a.name 
order by sotildi desc;

-- +------------------------+---------+
-- | name                   | sotildi |
-- +------------------------+---------+
-- | Ahad Qayum             |      94 |
-- | Xudoyberdi To'xtaboyev |      39 |
-- | Alisher Navoiy         |      21 |
-- | Adolfe Hitler          |       8 |
-- +------------------------+---------+