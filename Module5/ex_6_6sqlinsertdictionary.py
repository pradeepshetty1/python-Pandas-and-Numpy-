import sqlite3, os

class SqliteExamples(object):
    __DBPATH = os.path.join(os.getcwd(), 'sampledb')

    @classmethod
    def getConn(cls):
        return sqlite3.connect(cls.__DBPATH)

if __name__ == "__main__":
    conn = SqliteExamples.getConn()
    cursor = conn.cursor()

    data_dictionary={'courseid':6,'coursename':'Data Science'}
    resultset = cursor.execute('''Insert Into Tasks(TaskID, TaskName) Values(:courseid,:coursename)''',data_dictionary)
    for record in resultset.fetchall():
        print record
    conn.commit()
    cursor.close()
    conn.close()

