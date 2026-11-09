print("WELCOME TO SCHOOL MANAGEMENT SYSTEM")

from datetime import date
d=date.today()
print("DATE:",d)

import mysql.connector as conn
db=conn.connect(user='root',host='localhost',passwd='yourpassword',database='class12')
cur=db.cursor()


def login():
    user="select user_name from profile"
    passwd = "select password from profile;"
    cur.execute(user)
    profiles = cur.fetchall()
    cur.execute(passwd)
    password = cur.fetchall()

    profiles = [i[0] for i in profiles]
    password = [i[0] for i in password]

    un=input("Enter the User name:")
    pwd=input("Enter the password:")
    if un in profiles:
        i=profiles.index(un)
        if pwd==password[i]:
            print("You are logged in\n WELCOME ",un.capitalize())
            if un == "principal":
                repeat="y"
                while repeat=="y":

                    def add_new_teacher():
                        name=input("Enter the teacher name:")
                        un_new=input("Create new user name:")
                        pwd_new=input("Create new password:")
                        designation=input("Enter the designation:")
                        class_assgn=input("Enter the class assigned:")
                        q1 = "INSERT INTO profile VALUES (%s, %s)"
                        cur.execute(q1, (un_new, pwd_new))
                        q = "INSERT INTO teachers VALUES (%s, %s, %s, %s)"
                        cur.execute(q, (un_new, name, designation, class_assgn))
                        print("Teacher added successfully")
                        db.commit()

                    def add_new_student():
                        name = input("Enter the student name:")
                        s_id = int(input("Enter the student ID:"))
                        roll_no = int(input("Enter the student roll no:"))
                        clas = input("Enter the class:")

                        q = "select assigned_class from teachers"
                        cur.execute(q)
                        r = cur.fetchall()

                        if (f"{clas.capitalize()}",) in r:
                            q1 = f"INSERT INTO {clas} VALUES (%s, %s, %s)"
                            cur.execute(q1, (roll_no, s_id, name))
                            db.commit()


                        else:
                            ask = input("Create new class?(y/n)")
                            if ask == "y":
                                k = f"create table {clas}(Roll_no int not null,s_id int primary key,Name varchar(30));"
                                cur.execute(k)
                                q1 = f"insert into {clas} values(roll_no,s_id,name);"
                                cur.execute(q1)
                                db.commit()
                            else:
                                print("renter the student details")
                                add_new_student()

                    def l_teacher():
                        q=f"select * from teachers"
                        cur.execute(q)
                        r = cur.fetchall()
                        for i in r:
                            print(r.index(i)+1,':',i[1],'-',i[2],'    Assigned class:',i[3])


                    def l_student():
                        q = "select assigned_class from teachers"
                        cur.execute(q)
                        r = cur.fetchall()
                        for i in r:
                            k = f"select * from {i[0]}"
                            cur.execute(k)
                            p = cur.fetchall()
                            print("CLASS:", i[0])
                            for j in p:
                                print(j[0], j[1], j[2])

                    def l_present():
                        cur.execute("SELECT assigned_class FROM teachers")
                        classes = cur.fetchall()

                        for c in classes:
                            table = c[0].replace(" ", "_")

                            try:
                                query = f"""SELECT d.date, d.roll_no, s.name
                                    FROM data_{table} d
                                    JOIN {table} s ON d.roll_no = s.roll_no
                                    WHERE d.present = 0 AND d.date = %s"""
                                cur.execute(query, (d,))
                                rows = cur.fetchall()

                                for row in rows:
                                    print(row[0], row[1], row[2], table)

                            except Exception as e:
                                print(f"No attendance data for class {table}")

                    def l_absent():
                        cur.execute("SELECT assigned_class FROM teachers")
                        classes = cur.fetchall()

                        for c in classes:
                            table = c[0].replace(" ", "_")


                            try:
                                query = f"""
                                    SELECT d.date, d.roll_no, s.name
                                    FROM data_{table} d
                                    JOIN {table} s ON d.roll_no = s.roll_no
                                    WHERE d.present = 0 AND d.date = %s"""
                                cur.execute(query, (d,))
                                rows = cur.fetchall()

                                for row in rows:
                                    print(row[0], row[1], row[2], table)

                            except Exception as e:
                                print(f"No attendance data for class {table}")

                    def deletestudent():
                        cl=input("Enter the class:")
                        x=input("Enter the student roll no:")
                        s=input("Enter the student id:")
                        qa1 = f"delete from {cl} where roll_no=%s and s_id=%s;"
                        cur.execute(qa1, (x,s))  # tuple
                        print("student deleted")


                    print("\n\n Functions you can do as a Principal:")
                    print("0:Add new teacher")
                    print("1:Add new student")
                    print("2:list of teachers")
                    print("3:list of  student class wise")
                    print("4:list of  student present today")
                    print("5:list of  student absent today")
                    print("6:Remove student")

                    fun=input("Enter your choice:")
                    if fun=="0":
                        add_new_teacher()

                    elif fun=="1":
                        add_new_student()

                    elif fun=="2":
                        l_teacher()

                    elif fun=="3":
                        l_student()

                    elif fun=="4":
                        l_present()

                    elif fun=="5":
                        l_absent()

                    elif fun=="6":
                        deletestudent()


                    repeat = input("Want to do anything else?(y/n):")

            else:
                q = "SELECT * FROM teachers WHERE user_name = %s"
                cur.execute(q, (un,))

                val = cur.fetchone()
                print("\n\n Name:",val[1])
                print("Designation:",val[2])
                print("Assigned Class:",val[3])

                repeat="y"
                while repeat=="y":
                    def atnd():
                        qa=f"create table if not exists data_{val[3].replace(' ', '_')} (date date, roll_no int, present int,primary key (date, roll_no))"
                        cur.execute(qa)
                        qc = f"select roll_no, name from {val[3]}"
                        cur.execute(qc)
                        l = cur.fetchall()
                        qb = f"insert into data_{val[3].replace(' ', '_')} values(%s,%s,%s)"
                        for a in l:
                            r = a[0]
                            print(a[0], a[1])
                            while True:
                                p = input("enter 1 if above student is present and 0 if not:")  # acceppts only one str, f
                                if p in ('1', '0'):
                                    p = int(p)
                                    break
                                else:
                                    print("invalid input, input again")
                            cur.execute(qb, (d, r, p))
                            db.commit()

                    qx = f"select count(*) from data_{val[3].replace(' ', '_')} where roll_no=%s and present=1"

                    def satten():
                        x=input("Enter the student roll no:")
                        if studentexists(x):
                            cur.execute(qx, (x,))
                            v = cur.fetchone()[0]
                            print("attendance of student is", str(v))
                            return v
                        else:
                            print("student not found")
                            return None

                    def studentexists(x):

                        q = f"select 1 from {val[3]} where roll_no=%s"
                        cur.execute(q, (x,))
                        return cur.fetchone() is not None

                    def sattenperc():

                        x = input("Enter the student roll no:")
                        if studentexists(x):
                            cur.execute(qx, (x,))
                            v = cur.fetchone()[0]
                            qy = f"select count(distinct date) from data_{val[3].replace(' ', '_')}"
                            cur.execute(qy)
                            y = cur.fetchone()[0]
                            if y != 0:
                                p = v * 100 / y
                                print("attendance percentage is", str(p))
                                return p
                            else:
                                print("invalid operation")
                                return None
                        else:
                            print("invalid operation, student not found")
                            return None

                    def p_atten():
                        x=d
                        qz = f"select count(*) from data_{val[3].replace(' ', '_')} where date=%s and present=1"
                        cur.execute(qz, (x,))
                        v = cur.fetchone()[0]
                        print("Number of presentees=",v)

                    def a_atten():
                        x=d
                        qz = f"select count(*) from data_{val[3].replace(' ', '_')} where date=%s and present=0"
                        cur.execute(qz, (x,))
                        v = cur.fetchone()[0]
                        print("Number of absentees=",v)



                    print("\n\nFunctions you can do as a teacher:")
                    print("0:Record student attendance")
                    print("1:Show attendance of a student")
                    print("2:Show attendance percentage of a student")
                    print("3:Number of presentees of the day")
                    print("4:Number of absentees of the day")

                    t=input("Enter your choice:")
                    if t=="0":
                        atnd()

                    elif t=="1":
                        satten()

                    elif t=="2":
                        sattenperc()

                    elif t=="3":
                        p_atten()

                    elif t=="4":
                        a_atten()

                    repeat=input("Want to do anything else?(y/n):")




        else:
            print("INVALID CREDENTIALS! ")
            login()
    else:
        print("INVALID CREDENTIALS! ")
        login()
    db.commit()
    db.close()

login()