import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")
NAME = input("Enter the deleting no...")
conn.execute("DELETE FROM COMPANY WHERE ID =  "+NAME)
# data = conn.execute("SELECT * from COMPANY LIMIT 1,1")
print("ID  NAME   AGE  ADDRESS   SALARY")
# for n in data:
#     print(n[0],"",n[1]," ", n[2]," ", n[3]," ",n[4])
# conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')

# ins = """
# insert into COMPANY
#             (ID,NAME, AGE, ADDRESS, SALARY) VALUES
#             (53,"Sagya", 24, "Solapur", 33000.0)
#     """
# print("Table created successfully");
# conn.execute(ins)
conn.commit()
conn.close()
print("Insert successfully");
