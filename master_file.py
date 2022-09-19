import pandas as pd
import os

COMMANDS = {1: "Put option",
            2: "View Options",
            3: "Start environment",
            4: "Del options",
            0: "CLOSE"}


def view_commands():
    print(pd.Series(COMMANDS))


class User:
    def __init__(self, name, db):
        self.u_name = name
        self.id = id
        self.db_controller = db

    def lor_user(self):
        if len(self.db_controller.create_quarry(f"SELECT person_id FROM users WHERE u_name = '{self.u_name}';")) == 0:
            self.db_controller.create_quarry(f"INSERT INTO users (u_name) VALUES ('{self.u_name}')")
            print("USER REG")
        else:
            quarry = f"SELECT person_id FROM users WHERE u_name = '{self.u_name}';"
            self.id = self.db_controller.create_quarry(quarry)[0][0]
            print(f"HELLO {self.id}")

    def command_run(self, command_num):
        command_num = int(command_num)
        match command_num:
            case 0:
                return "CLOSE"
            case 1:
                env_op = input("Option: ")
                quarry = f"INSERT INTO environments (u_id, env_option) VALUES ('{self.id}', '{env_op}')"
                self.db_controller.create_quarry(quarry)
            case 2:
                quarry = f"SELECT env_option FROM environments WHERE u_id == '{self.id}'"
                res = self.db_controller.create_quarry(quarry)
                if len(res) == 0:
                    print("None")
                else:
                    print(pd.Series(res))
            case 3:
                quarry = f"SELECT env_option FROM environments WHERE u_id == '{self.id}'"
                options = self.db_controller.create_quarry(quarry)[0]
                for i in options:
                    os.system(f"start {i}")
            case 4:
                quarry = f"DELETE FROM environments WHERE u_id='{self.id}'"
                self.db_controller.create_quarry(quarry)




