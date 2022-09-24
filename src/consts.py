import os

from db_master import DataBase
from db_master import User


def view_options():
    global STAGE_NOW
    USER.view_options()
    STAGE_NOW = STAGES["CONTROL"]
    choice_command()


def put_option():
    USER.put_option()
    choice_command()


def delete_option_by_id():
    USER.delete_option_by_id()
    choice_command()


def choice_command():
    os.system("cls")
    for i in STAGE_NOW[0].items():
        print(f"{i[0]}: {i[1]}")
    user_choice = int(input("Choice option: "))
    STAGE_NOW[1][STAGE_NOW[0][user_choice]]()


def return_back():
    global STAGE_NOW
    if STAGE_NOW == STAGES["OPTIONS"]:
        STAGE_NOW = STAGES["START"]
        choice_command()
    if STAGE_NOW == STAGES["CONTROL"]:
        STAGE_NOW = STAGES["OPTIONS"]
        choice_command()


def view_options_settings():
    global STAGE_NOW
    STAGE_NOW = STAGES["OPTIONS"]
    choice_command()


USER = User(None, None)

COMMANDS_VIEW_START = {
    1: "Start environment",
    2: "Options settings",
    0: "CLOSE"
}
COMMANDS_START_START = {
    "Start environment": USER.start_environment,
    "Options settings": view_options_settings,
    "CLOSE": exit
}

COMMANDS_VIEW_OPTIONS = {
    1: "View options",
    2: "Clear options",
    0: "RETURN"
}
COMMANDS_START_OPTIONS = {
    "View options": view_options,
    "Clear options": USER.clear_options,
    "RETURN": return_back
}
COMMANDS_VIEW_CONTROL = {
    1: "Put option",
    2: "Delete option by id",
    0: "RETURN"
}
COMMANDS_START_CONTROL = {
    "Put option": put_option,
    "Delete option by id": delete_option_by_id,
    "RETURN": return_back
}
DB = DataBase("users.db")

STAGES = {
    "START": (COMMANDS_VIEW_START, COMMANDS_START_START),
    "OPTIONS": (COMMANDS_VIEW_OPTIONS, COMMANDS_START_OPTIONS),
    "CONTROL": (COMMANDS_VIEW_CONTROL, COMMANDS_START_CONTROL)
}

STAGE_NOW = STAGES["START"]
