import sqlite3, os

__DBPATH = os.path.join(os.getcwd(), 'sampledb_simple')

conn = sqlite3.connect(__DBPATH)
cursor = conn.cursor()
simple_sql = "Select SQLITE_VERSION()"
myresultset = cursor.execute(simple_sql)
for record in myresultset.fetchall():
    print record

cursor.close
conn.commit()

conn.close()

