import pymysql

class MySQL:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTeacher()
        self.CreateStudent()

    def ConnectDB(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        self.c = self.db.cursor()

    def CreateDB(self):
        self.c.execute("CREATE DATABASE IF NOT EXISTS school")
        self.c.execute("USE school")

    def CreateTeacher(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS teacher(
                       id int AUTO_INCREMENT PRIMARY KEY,
                       name varchar(50),
                       surname varchar(50),
                       salary int,
                       experience int,
                       branch varchar(50))''')

    def InsertTecher(self):
        self.c.execute(f'''INSERT INTO teacher(name, surname, salary, experience, branch)
                        VALUES ("Ali",     "Karimov",   5000000, 10, "Fergana"),
                            ("Vali",    "Rahimov",   4500000,  7, "Toshkent"),
                            ("Nigora",  "Umarova",   6000000, 15, "Andijon"),
                            ("Jasur",   "Toshmatov", 3800000,  5, "Qarshi"),
                            ("Malika",  "Yusupova",  5500000, 12, "Samarkand"),
                            ("Sardor",  "Nazarov",   4200000,  8, "Buxoro"),
                            ("Dilnoza", "Hasanova",  7000000, 20, "Namangan")''')
        self.db.commit()

    def CreateStudent(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS student(
                       id int AUTO_INCREMENT PRIMARY KEY,
                       name varchar(50),
                       surname varchar(50),
                       monthly_payment int,
                       course_duration int,
                       branch varchar(50))''')
        
    def InsertStudent(self):
        self.c.execute(f'''INSERT INTO student(name, surname, monthly_payment, course_duration, branch)
                        VALUES ("Jasur",   "Toshmatov", 350000, 3, "Toshkent"),
                            ("Malika",  "Yusupova",  400000, 6, "Samarkand"),
                            ("Sardor",  "Nazarov",   300000, 4, "Buxoro"),
                            ("Dilnoza", "Hasanova",  450000, 2, "Fergana"),
                            ("Bobur",   "Karimov",   380000, 5, "Namangan"),
                            ("Nilufar", "Rahimova",  420000, 3, "Andijon"),
                            ("Sherzod", "Umarov",    500000, 8, "Qarshi")''')
        self.db.commit()

    def quest_1(self):
        self.c.execute(f'''select * from teacher order by salary''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)

    def quest_2(self):
        self.c.execute(f'''select * from teacher order by salary, experience desc''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)

    def quest_3(self):
        self.c.execute(f'''update teacher set salary = 5000000 order by salary desc limit''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)

    def quest_4(self):
        self.c.execute(f'''update teacher set branch = "Chilonzor" order by experience desc limit 1''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)

    def quest_5(self):
        self.c.execute(f'''select * from student order by surname''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)

    def quest_6(self):
        self.c.execute(f'''select * from student order by monthly_payment desc''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)

    def quest_7(self):
        self.c.execute(f'''select sum(monthly_payment*course_duration) as summa from student''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)

    def quest_8(self):
        self.c.execute(f'''update student set branch ="Dubay" order by  monthly_payment*course_duration desc limit 1''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)

    def quest_9(self):
        self.c.execute(f'''select t.branch, t.name teacher, s.name student from teacher t join student s on t.branch = s.branch''')
        natija = self.c.fetchall()
        for i in natija:
            print(i)
        

mysql = MySQL()
# mysql.InsertTecher()
# mysql.InsertStudent()

