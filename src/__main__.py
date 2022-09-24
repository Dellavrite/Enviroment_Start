from consts import *


def main():
    with DB as db:
        USER.db_controller = db
        USER.loading()
        choice_command()


if __name__ == "__main__":
    main()
