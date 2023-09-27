import sqlite3

db="mytodo.db"
conn= sqlite3.connect(db)
c = conn.cursor()

def createtable():
    sql = 'CREATE TABLE IF NOT EXISTS task(ID INTEGER PRIMARY KEY AUTOINCREMENT,TaskName text)'
    c.execute(sql)

def insertdata(task):
    c.execute('INSERT INTO task(TaskName)VALUES(?)',[task])
    conn.commit()

def displaydata():
    sql='SELECT * FROM task'
    c.execute(sql)
    for row in c.fetchall():
        print(row[0],"----",row[1])

def deletedata(index):
    c.execute('DELETE FROM task WHERE ID=?',(index, ))

def close():
    c.close()
    conn.close()