import sqlite3, os

class SqliteExamples(object):
    __DBPATH = os.path.join(os.getcwd(), 'sampledb')

    @classmethod
    def getConn(cls):
        return sqlite3.connect(cls.__DBPATH)

if __name__ == "__main__":
    conn = SqliteExamples.getConn()
    cursor = conn.cursor()


    #insert_sql0 = 'Insert Into Tasks(TaskID, TaskName) Values(0,"Learn DataScience")'
    insert_sql0 = 'Insert Into Tasks(TaskID, TaskName) Values(1,"Python")'
    cursor.execute(insert_sql0)
    conn.commit()
    cursor.close()
    conn.close()

