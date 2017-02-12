import sqlite3, os

class SqliteExamples(object):
    __DBPATH = os.path.join(os.getcwd(), 'sampledb')

    @classmethod
    def getConn(cls):
        return sqlite3.connect(cls.__DBPATH)

if __name__ == "__main__":
    conn = SqliteExamples.getConn()
    cursor = conn.cursor()


    resultset = cursor.execute('''select TaskID,TaskName from tasks''')
    for record in resultset.fetchall():
        print record

    print '================================'
    resultset = cursor.execute('''select TaskID,TaskName from tasks''')
    print resultset.fetchone()


    conn.commit()
    cursor.close()
    conn.close()

