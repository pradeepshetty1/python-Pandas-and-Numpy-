import sqlite3, os

class SqliteExamples(object):
    __DBPATH = os.path.join(os.getcwd(), 'sampledb')

    @classmethod
    def getConn(cls):
        return sqlite3.connect(cls.__DBPATH)

if __name__ == "__main__":
    conn = SqliteExamples.getConn()
    cursor = conn.cursor()

    insert_sql = 'Insert Into Tasks(TaskID, TaskName) Values(?,?)'
    insert_rec1 = (2, 'Learn Python')
    insert_rec2 = (3, 'Learn Hadoop')
    resultset = cursor.executemany('''Insert Into Tasks(TaskID, TaskName) Values(?,?)''',[insert_rec1, insert_rec2])
    for record in resultset.fetchall():
        print record
    conn.commit()
    cursor.close()
    conn.close()

