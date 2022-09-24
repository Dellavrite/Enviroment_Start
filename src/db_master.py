import sqlite3
import os


class DataBase:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.starting_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        print("DB CLOSE")

    def create_quarry(self, quarry):
        self.cursor.execute(quarry)
        self.connection.commit()
        return self.cursor.fetchall()

    def starting_db(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        print("DB RUN")
        print(self.create_quarry("select sqlite_version();"))

    def check_db_exists(self, db_name: str) -> bool:
        if self.name == "users.db":
            quarry = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{db_name}';"
            return bool(len(self.create_quarry(quarry)))

    def check_user_exist(self, user_name: str) -> bool:
        quarry = f"SELECT person_id FROM users WHERE u_name = '{user_name}';"
        return bool(len(self.create_quarry(quarry)))

    def create_environments(self):
        self.create_quarry("""CREATE TABLE environments (
                           id INTEGER PRIMARY KEY,
                           u_id INTEGER NOT NULL,
                           env_option TEXT NOT NULL
                            );""")

    def create_users(self):
        self.create_quarry("""CREATE TABLE users (
                           person_id INTEGER PRIMARY KEY,
                           u_name TEXT NOT NULL
                            );""")

    def delete_user(self, user_name):
        self.create_quarry(f"DELETE FROM users WHERE u_name='{user_name}'")
        exit(0)


class User:
    def __init__(self, name, db):
        self.u_name = name
        self.id = None
        self.db_controller = db

    def loading(self):
        u_name = input("Input the username: ")

        if u_name == "del":
            self.db_controller.delete_user(input("Input del username: "))

        if not self.db_controller.check_db_exists("users"):
            self.db_controller.create_users()
        if not self.db_controller.check_db_exists("environments"):
            self.db_controller.create_environments()

        if self.db_controller.check_user_exist(u_name):
            print("READY")
            self.get_user()
        else:
            print("REG")
            self.create_user()

    def create_user(self):
        self.db_controller.create_quarry(f"INSERT INTO users (u_name) VALUES ('{self.u_name}')")
        quarry = f"SELECT person_id FROM users WHERE u_name = '{self.u_name}';"
        self.id = self.db_controller.create_quarry(quarry)[0][0]
        return self

    def get_user(self):
        quarry = f"SELECT person_id FROM users WHERE u_name = '{self.u_name}';"
        self.id = self.db_controller.create_quarry(quarry)[0][0]
        return self

    def start_environment(self):
        quarry = f"SELECT env_option FROM environments WHERE u_id == '{self.id}'"
        options = self.db_controller.create_quarry(quarry)[0]
        for i in options:
            os.system(f"start {i}")

    def view_options(self):
        quarry = f"SELECT env_option FROM environments WHERE u_id == '{self.id}'"
        res = self.db_controller.create_quarry(quarry)
        res = list(map(list, res))
        for i in res:
            quarry = f"SELECT id FROM environments WHERE env_option == '{i[0]}'"
            i.append(self.db_controller.create_quarry(quarry)[0][0])
        if len(res) == 0:
            print("None")
        else:
            print("\n".join(map(str, res)))

    def put_option(self):
        env_op = input("Option: ")
        quarry = f"INSERT INTO environments (u_id, env_option) VALUES ('{self.id}', '{env_op}')"
        self.db_controller.create_quarry(quarry)

    def delete_option_by_id(self):
        os.system("cls")
        self.view_options()
        id_of_option = int(input("Input id: "))
        quarry = f"DELETE FROM environments WHERE u_id='{self.id}' AND id={id_of_option}"
        self.db_controller.create_quarry(quarry)

    def get_env_id(self, id):
        pass

    def clear_options(self):
        quarry = f"DELETE FROM environments WHERE u_id='{self.id}'"
        self.db_controller.create_quarry(quarry)
