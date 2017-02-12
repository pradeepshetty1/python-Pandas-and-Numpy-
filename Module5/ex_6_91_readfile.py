import sqlite3, os

class SqliteExamples(object):
    __DBPATH = os.path.join(os.getcwd(), 'sampledb')

    @classmethod
    def getConn(cls):
        return sqlite3.connect(cls.__DBPATH)

if __name__ == "__main__":
    conn = SqliteExamples.getConn()
    cursor = conn.cursor()

    record_list = []
    my_insert_sql = '''Insert Into Tasks(TaskID, TaskName) Values(?,?)'''
    with open('filename.txt','r') as f:
         for line in f:
            rec =  line.split(',') # a,b,c,d
            record_list.append(tuple(rec))

    cursor.executemany(my_insert_sql, record_list)
    conn.commit()
    cursor.close()
    conn.close()

