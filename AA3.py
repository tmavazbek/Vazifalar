import pymysql

class MySQL:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()

    def ConnectDB(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        self.c = self.db.cursor()

    def CreateDB(self):
        self.c.execute("CREATE DATABASE IF NOT EXISTS gilos")
        self.c.execute("USE gilos")

    def CreateTB(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS restoran(
                       id int AUTO_INCREMENT PRIMARY KEY,
                       name text,
                       address text,
                       maxFoodPrice int,
                       minFoodPrice int,
                       employeesCount int,
                       experience int)''')
        
    def InsertTB(self):
        self.c.execute(f'''INSERT INTO restoran(name, address, maxFoodPrice, minFoodPrice, employeesCount, experience) 
                       VALUES("Mirzo",   "Toshkent",   85000, 15000, 30, 12),
                            ("Bahor",    "Samarkand",  60000, 10000, 20,  5),
                            ("Muhabbat", "Buxoro",     95000, 20000, 45, 18),
                            ("Navbahor", "Fergana",    70000, 12000, 25,  8),
                            ("Zafar",    "Namangan",   55000,  8000, 15,  3),
                            ("Malika",   "Toshkent",  110000, 25000, 60, 22),
                            ("Oybek",    "Andijon",    45000,  7000, 12,  2),
                            ("Mehriban", "Qarshi",     80000, 18000, 35, 10),
                            ("Gulbahor", "Nukus",      65000, 11000, 22,  6),
                            ("Mavlono",  "Termiz",     90000, 22000, 40, 15)''')
        self.db.commit()

    def name_m_o(self):
        self.c.execute(f'''select name, maxFoodPrice from restoran where name like "M%" and name like "%o" order by maxFoodPrice''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)

    def arzon_3ta(self):
        self.c.execute(f'''select name, minFoodPrice from restoran order by minFoodPrice limit 3''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)

    def quest4(self):
        self.c.execute(f'''select name, maxFoodPrice, experience from restoran order by experience desc, maxFoodPrice desc limit 4''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)



mysql = MySQL()
# for i in range(10):
#     mysql.InsertTB(input("Comp_name: "), input("Location: "), int(input("max_p: ")), int(input("min_p: ")), int(input("emp_count: ")), int(input("Experinence: ")))
# mysql.InsertTB()
# mysql.name_m_o()
# mysql.arzon_3ta()
# mysql.quest4()