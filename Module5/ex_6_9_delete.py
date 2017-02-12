import sqlite3, os

class SqliteExamples(object):
    __DBPATH = os.path.join(os.getcwd(), 'sampledb')

    @classmethod
    def getConn(cls):
        return sqlite3.connect(cls.__DBPATH)

if __name__ == "__main__":
    conn = SqliteExamples.getConn()
    cursor = conn.cursor()


    if cursor.execute('''delete from tasks where TaskId= 1'''):
        print 'Record deleted successfully'




    conn.commit()
    cursor.close()
    conn.close()

