import sqlite3, os

class SqliteExamples(object):
    __DBPATH = os.path.join(os.getcwd(), 'sampledb')

    @classmethod
    def getConn(thiscls):
        return sqlite3.connect(thiscls.__DBPATH)



if __name__ == "__main__":
    conn = SqliteExamples.getConn()
    cursor = conn.cursor()
    create_sql = "Create Table Tasks(TaskID Integer Primary Key, TaskName Text, TaskOwner Text)"
    cursor.execute(create_sql)

    cursor.close
    conn.commit()

    conn.close()

