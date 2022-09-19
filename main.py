from DB import DB
from master_file import User, view_commands
import os

user_name = input("Enter the username: ")

with DB("users.db") as data_base:
    if user_name == "del":
        data_base.create_quarry(f"DELETE FROM users WHERE u_name='{input()}'")
        exit(0)
    user = User(user_name, data_base)
    user.lor_user()
    ret = ""
    while ret != "CLOSE":
        view_commands()
        ret = int(input("Input the num of command: "))
        ret = user.command_run(ret)
        os.system("cls")



