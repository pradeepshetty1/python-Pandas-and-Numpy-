import sqlite3, os

class SqliteExamples(object):
    __DBPATH = os.path.join(os.getcwd(), 'sampledb')

    @classmethod
    def getConn(cls):
        return sqlite3.connect(cls.__DBPATH)

    def readFromFile(self, cursor):
        record_list = []
        my_insert_sql = '''Insert Into Tasks(TaskID, TaskName) Values(?,?)'''
        with open('filename.txt','r') as f:
            for line in f:
                rec =  line.split(',') # a,b,c,d
                record_list.append(tuple(rec))

        cursor.executemany(my_insert_sql, record_list)

    def insertRecs(self, cursor):
        insert_sql = 'Insert Into Tasks(TaskID, TaskName) Values(?,?)'
        insert_rec1 = (1, 'Learn Python')
        insert_rec2 = (2, 'Learn Hadoop')

        resultset = cursor.executemany('''Insert Into Tasks(TaskID, TaskName) Values(?,?)''',[insert_rec1, insert_rec2])
        return resultset

if __name__ == "__main__":
    conn = SqliteExamples.getConn()
    cursor = conn.cursor()
    #sql_stmt = "Select SQLITE_VERSION()"
    #create_sql = "Create Table Tasks(TaskID Integer Primary Key, TaskName Text, TaskOwner Text)"
    #cursor.execute(create_sql)
    #check_tables = "Select name from sqlite_master where type='table'"
    #drop_table = "Drop Table Tasks"
    insert_sql = 'Insert Into Tasks(TaskID, TaskName) Values(?,?)'
    insert_rec1 = (1, 'Learn Python')
    insert_rec2 = (2, 'Learn Hadoop')
    #resultset = cursor.executemany('''Insert Into Tasks(TaskID, TaskName) Values(?,?)''',[insert_rec1, insert_rec2])
    conn.commit()
    resultset = cursor.execute('Select * From Tasks')
    select_tasks = '''Select * From Tasks Where TaskID = ?'''
    update_tasks = '''Update Tasks Set TaskOwner = ? Where TaskID = ?'''

    #resultset = cursor.execute(update_tasks,('Me',1,))
    print cursor.lastrowid
    conn.commit()
    #resultset = cursor.execute(select_tasks, (1,))
    for record in resultset.fetchmany(3):
        print record

    cursor.close()
    conn.close()

