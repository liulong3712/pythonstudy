import sqlite3

cx = sqlite3.connect("E:\\PythonStudy\\pythonstudy\\python\\study\\sqlite3\\test1.db")
cu = cx.cursor()
cu.execute('create TABLE IF NOT EXISTS catalog(id integer PRIMARY KEY AUTOINCREMENT ,pid integer, name varchar(110) )')
cu.execute('INSERT INTO catalog(pid, name) VALUES (0,"hello")')
cu.execute('SELECT * FROM catalog')
print cu.fetchmany(2)
print cu.fetchall()
print cu.next()
cx.commit()