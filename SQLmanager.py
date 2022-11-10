import sqlite3


def create_database():
    conn = sqlite3.connect('test.db')
    print("数据库打开成功")
    c = conn.cursor()
    c.execute('''
    CREATE TABLE FILES
    (ID INT PRIMARY KEY     NOT NULL,
    NAME    TEXT            NOT NULL,
    PATH    TEXT            NOT NULL,
    SIZE    INTEGER         NOT NULL,
    )''')
    conn.commit()
    conn.close()

def insert_files(info):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''
    INSERT INFO FILES(ID
    ''')


class SqlWorker:

    cmd_count = 0

    def __init__(self, path, *args, **kwargs):
        self.dbpath = path
        self.cnn = sqlite3.connect(path)
        self.cursor = self.cnn.cursor()
        super(SqlWorker, self).__init__(*args, **kwargs)

    # def sqlcmd(self, cmdline):
    #     if self.cmd_count > 50:
    #         self.cnn.commit()
    #         self.cmd_count = 0
    #     self.cursor.execute(cmdline)
    #     self.cmd_count+=1
    #     print(self.cmd_count)

    def sqlcmd(self, cmdline):
        self.cursor.execute(cmdline)

    def commit(self):
        self.cnn.commit()

    def rollback(self):
        self.cnn.rollback()

    def close(self):
        self.cursor.close()
        self.cnn.close()

    def connect_test(path):
        return sqlite3.connect(path)

    def fetch(self):
        return self.cursor.fetchone()

    def fetch_all(self):
        return self.cursor.fetchall()

    def init_files_db(self):
        # 判断是否有这个数据库？
        sqline = f'CREATE TABLE IF NOT EXISTS FILES \
        (id integer primary key, \
        name text not null, \
        path text not null, \
        size text not null, \
        alias TEXT NOT NULL)'
        return self.sqlcmd(sqline)
    #
    #     self.cursor.execute('''
    # CREATE TABLE FILES
    # (ID INTEGER PRIMARY KEY     NOT NULL,
    # NAME    TEXT    NOT NULL,
    # PATH    TEXT    NOT NULL,
    # SIZE    INTEGER NOT NULL,
    # )''')
    #     self.cnn.commit()
    #     self.cnn.close()

    def insert_lines(self, v):
        cmd_line = f"insert into table values(\"{v['name']}\", \"{v['path']}\", \"{v['size']}\")"
        self.sqlcmd(cmd_line)
        self.commit()


class CSVSqlWorker(SqlWorker):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = args[0]




