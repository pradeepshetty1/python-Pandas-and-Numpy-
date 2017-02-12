import sqlite3, os

class SqliteExamples(object):
    __DBPATH = os.path.join(os.getcwd(), 'sampledb')

    @classmethod
    def getConn(cls):
        return sqlite3.connect(cls.__DBPATH)

if __name__ == "__main__":
    conn = SqliteExamples.getConn()
    cursor = conn.cursor()
    updatecourseto = 'MongoDB'

    if cursor.execute('''update tasks set TaskName= ? where TaskId= ?''',(updatecourseto,1)):
        print 'Record updated successfully'




    conn.commit()
    cursor.close()
    conn.close()

