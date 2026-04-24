CREATE DATABASE Kompyuter;
use Kompyuter

CREATE TABLE kompyuterlar(brand text, model text, cpu text, frequency real, ram int, os text, price int)

INSERT into kompyuterlar values("Apple", "MacBook Pro 14", "Intel Core i7", 3.2, 16, "macOS Monterey", 1999),
                                ("Apple", "MacBook Air M2", "Apple M2", 3.5, 8, "macOS Ventura", 1299),
                                ("Apple", "MacBook Pro 16", "Intel Core i9", 3.9, 32, "macOS Monterey", 2499),
                                ("ASUS", "ZenBook 14", "Intel Core i5", 2.4, 8, "Windows 11", 749),
                                ("ASUS", "ZenBook Pro", "Intel Core i7", 2.8, 16, "Windows 11", 1199),
                                ("ASUS", "VivoBook 15", "AMD Ryzen 5", 2.1, 8, "Windows 10", 599),
                                ("ASUS", "ROG Strix G15", "AMD Ryzen 7", 3.2, 16, "Windows 11", 1349),
                                ("Dell", "XPS 13", "Intel Core i7", 2.8, 16, "Windows 11", 1299),
                                ("Dell", "Inspiron 15", "Intel Core i5", 2.4, 8, "Windows 10", 649),
                                ("Dell", "Latitude 5520", "Intel Core i7", 3.0, 16, "Ubuntu 20.04", 1099),
                                ("HP", "Spectre x360", "Intel Core i7", 2.9, 16, "Windows 11", 1399),
                                ("HP", "Pavilion 15", "AMD Ryzen 5", 2.3, 8, "Windows 10", 579),
                                ("HP", "EliteBook 840", "Intel Core i7", 3.0, 16, "Windows 11", 1249),
                                ("Lenovo", "ThinkPad X1", "Intel Core i7", 3.1, 16, "Windows 11", 1549),
                                ("Lenovo", "IdeaPad 5", "AMD Ryzen 5", 2.5, 8, "Windows 10", 699),
                                ("Lenovo", "Legion 5 Pro", "AMD Ryzen 7", 3.2, 16, "Windows 11", 1199),
                                ("Samsung", "Galaxy Book Pro", "Intel Core i5", 2.4, 8, "Windows 11", 849),
                                ("Samsung", "Galaxy Book 360", "Intel Core i7", 2.8, 16, "Windows 11", 1149),
                                ("Acer", "Aspire 5", "AMD Ryzen 5", 2.1, 8, "Windows 10", 499),
                                ("Acer", "Swift 3", "Intel Core i7", 2.9, 16, "Ubuntu 20.04", 879);

+---------+-----------------+---------------+-----------+------+----------------+-------+
| brand   | model           | cpu           | frequency | ram  | os             | price |
+---------+-----------------+---------------+-----------+------+----------------+-------+
| Apple   | MacBook Pro 14  | Intel Core i7 |       3.2 |   16 | macOS Monterey |  1999 |
| Apple   | MacBook Air M2  | Apple M2      |       3.5 |    8 | macOS Ventura  |  1299 |
| Apple   | MacBook Pro 16  | Intel Core i9 |       3.9 |   32 | macOS Monterey |  2499 |
| ASUS    | ZenBook 14      | Intel Core i5 |       2.4 |    8 | Windows 11     |   749 |
| ASUS    | ZenBook Pro     | Intel Core i7 |       2.8 |   16 | Windows 11     |  1199 |
| ASUS    | VivoBook 15     | AMD Ryzen 5   |       2.1 |    8 | Windows 10     |   599 |
| ASUS    | ROG Strix G15   | AMD Ryzen 7   |       3.2 |   16 | Windows 11     |  1349 |
| Dell    | XPS 13          | Intel Core i7 |       2.8 |   16 | Windows 11     |  1299 |
| Dell    | Inspiron 15     | Intel Core i5 |       2.4 |    8 | Windows 10     |   649 |
| Dell    | Latitude 5520   | Intel Core i7 |         3 |   16 | Ubuntu 20.04   |  1099 |
| HP      | Spectre x360    | Intel Core i7 |       2.9 |   16 | Windows 11     |  1399 |
| HP      | Pavilion 15     | AMD Ryzen 5   |       2.3 |    8 | Windows 10     |   579 |
| HP      | EliteBook 840   | Intel Core i7 |         3 |   16 | Windows 11     |  1249 |
| Lenovo  | ThinkPad X1     | Intel Core i7 |       3.1 |   16 | Windows 11     |  1549 |
| Lenovo  | IdeaPad 5       | AMD Ryzen 5   |       2.5 |    8 | Windows 10     |   699 |
| Lenovo  | Legion 5 Pro    | AMD Ryzen 7   |       3.2 |   16 | Windows 11     |  1199 |
| Samsung | Galaxy Book Pro | Intel Core i5 |       2.4 |    8 | Windows 11     |   849 |
| Samsung | Galaxy Book 360 | Intel Core i7 |       2.8 |   16 | Windows 11     |  1149 |
| Acer    | Aspire 5        | AMD Ryzen 5   |       2.1 |    8 | Windows 10     |   499 |
| Acer    | Swift 3         | Intel Core i7 |       2.9 |   16 | Ubuntu 20.04   |   879 |
+---------+-----------------+---------------+-----------+------+----------------+-------+


SELECT * FROM kompyuterlar ORDER BY price DESC LIMIT 1;
+-------+----------------+---------------+-----------+------+----------------+-------+
| brand | model          | cpu           | frequency | ram  | os             | price |
+-------+----------------+---------------+-----------+------+----------------+-------+
| Apple | MacBook Pro 16 | Intel Core i9 |       3.9 |   32 | macOS Monterey |  2499 |
+-------+----------------+---------------+-----------+------+----------------+-------+

SELECT * FROM kompyuterlar ORDER BY price LIMIT 1;
+-------+----------+-------------+-----------+------+------------+-------+
| brand | model    | cpu         | frequency | ram  | os         | price |
+-------+----------+-------------+-----------+------+------------+-------+
| Acer  | Aspire 5 | AMD Ryzen 5 |       2.1 |    8 | Windows 10 |   499 |
+-------+----------+-------------+-----------+------+------------+-------+


SELECT frequency FROM kompyuterlar WHERE price BETWEEN 400 and 1000 and cpu LIKE "%intel%";
+-----------+
| frequency |
+-----------+
|       2.4 |
|       2.4 |
|       2.4 |
|       2.9 |
+-----------+


SELECT count(brand) as brand_Apple from kompyuterlar WHERE brand LIKE "Apple";
+-------------+
| brand_Apple |
+-------------+
|           3 |
+-------------+


SELECT price FROM kompyuterlar WHERE os LIKE "%Windows%" AND ram = 8 AND brand = "ASUS" ORDER BY price
+-------+
| price |
+-------+
|   599 |
|   749 |
+-------+