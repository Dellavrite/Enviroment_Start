import sqlite3


class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.start_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        print("DB CLOSE")

    def create_quarry(self, quarry):
        self.cursor.execute(quarry)
        self.connection.commit()
        return self.cursor.fetchall()

    def start_db(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        print("DB RUN")
        print(self.create_quarry("select sqlite_version();"))
        if self.name == "users.db":
            if len(self.create_quarry(f"SELECT name FROM sqlite_master WHERE type='table' AND name='users';")) == 0:
                self.create_quarry("""CREATE TABLE users (
                                       person_id INTEGER PRIMARY KEY,
                                       u_name TEXT NOT NULL
                                        );""")
            if len(self.create_quarry(f"SELECT name FROM sqlite_master WHERE type='table' AND name='environments';")) == 0:
                self.create_quarry("""CREATE TABLE environments (
                                       id INTEGER PRIMARY KEY,
                                       u_id INTEGER NOT NULL,
                                       env_option TEXT NOT NULL
                                        );""")
