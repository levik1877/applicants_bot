import sqlite3

way_to_database = "users_data.db"


def create_table():
    with sqlite3.connect(way_to_database) as data_base:
        data_base.execute("CREATE TABLE users (telegram_user_id INTEGER, snils TEXT, fio TEXT)")
        data_base.execute("CREATE TABLE universities (name TEXT, url TEXT)")
        data_base.execute("CREATE TABLE faculties (university_id INTEGER, name TEXT, url TEXT)")
        sql = """
        CREATE TABLE selected_faculties (user_id INTEGER, 
        f1 INTEGER, f2 INTEGER, f3 INTEGER, f4 INTEGER, f5 INTEGER, 
        f6 INTEGER, f7 INTEGER, f8 INTEGER, f9 INTEGER, f10 INTEGER, 
        f11 INTEGER, f12 INTEGER, f13 INTEGER, f14 INTEGER, f15 INTEGER, 
        f16 INTEGER, f17 INTEGER, f18 INTEGER, f19 INTEGER, f20 INTEGER, 
        f21 INTEGER, f22 INTEGER, f23 INTEGER, f24 INTEGER, f25 INTEGER)
        """
        data_base.execute(sql)
        sql = """
        CREATE TABLE selected_universities (user_id int, 
        u1 INTEGER,  u2 INTEGER,  u3 INTEGER,  u4 INTEGER,  u5 INTEGER)
        """
        data_base.execute(sql)
        data_base.commit()


def open_database():
    database = sqlite3.connect(way_to_database)
    return database


def add_user(database, user_data: list):
    """users_data: [(id, snils, fio),
    [0, selected_university1, selected_university2, ... , selected_university5],
    [0, selected_faculty1, selected_faculty2, ... , selected_faculty25]]"""
    cursor = database.cursor()
    cursor.execute(f"INSERT INTO users VALUES {user_data[0]}")
    cursor.execute(f"SELECT rowid FROM users WHERE telegram_user_id = {user_data[0][0]}")
    db_user_id = cursor.fetchone()[0]
    selected_universities = user_data[1]
    selected_universities[0] = db_user_id
    cursor.execute(f"INSERT INTO selected_universities VALUES {tuple(selected_universities)}")
    selected_faculties = user_data[2]
    selected_faculties[0] = db_user_id
    cursor.execute(f"INSERT INTO selected_faculties VALUES {tuple(selected_faculties)}")


def get_user(detabase, user_id: int):
    cursor = detabase.cursor()
    user_snils_fio = cursor.execute(f"SELECT * FROM users WHERE telegram_user_id = {user_id}")
    sql = f"""
    SELECT * FROM selected_universities 
    JOIN users 
    WHERE (selected_universities.user_id = users.rowid) AND (telegram_user_id = {user_id})
    """
    user_selected_universities = cursor.execute(sql)
    sql = f"""
    SELECT * FROM selected_faculties 
    JOIN users 
    WHERE (selected_faculties.user_id = users.rowid) AND (telegram_user_id = {user_id})
    """
    user_selected_faculties = cursor.execute(sql)
    user_information = [user_snils_fio, user_selected_universities, user_selected_faculties]
    user_info = []
    for i in range(len(user_information)):
        for j in range(len(user_information[i])):
            user_info.append(user_information[i][j])
    return user_info


def edit_user(database, user_id: int, change_params: tuple, new_data):
    """
    :param database:
    :param user_id:
    :param change_params: (change_pattern, column(для 3,4))
    :param new_data:

    1 - изменить СНИЛС
    2 - изменить ФИО
    3 - выбрать университет
    4 - выбрать факультет

    """
    cursor = database.cursor()

    match change_params[0]:
        case 1:
            cursor.execute(f"UPDATE users SET snils = '{new_data}' WHERE telegram_user_id = {user_id}")
        case 2:
            cursor.execute(f"UPDATE users SET fio = '{new_data}' WHERE telegram_user_id = {user_id}")
        case 3:
            sql = f"""
            UPDATE selected_universities 
            SET {change_params[1]} = {new_data} 
            WHERE user_id = (SELECT rowid FROM users WHERE telegram_user_id = {user_id})
            """
            cursor.execute(sql)
        case 4:
            sql = f"""
            UPDATE selected_faculties 
            SET {change_params[1]} = {new_data} 
            WHERE user_id = (SELECT rowid FROM users WHERE telegram_user_id = {user_id})
            """
            cursor.execute(sql)


def check_user(database, user_id: int):
    cursor = database.cursor()
    cursor.execute(f"SELECT rowid FROM users WHERE telegram_user_id = {user_id}")
    if cursor.fetchone() == None:
        return False
    else:
        return True


def add_university(database, university_data: tuple):
    """
    :param database:
    :param university_data: (название университета, ссылка на списки поступающих)
    """
    cursor = database.cursor()
    cursor.execute(f"INSERT INTO universities VALUES {university_data}")


def add_faculty(database, faculty_data: tuple, university_name: str):
    """
    :param database:
    :param faculty_data: (название факультета, ссылка на таблицу поступающих)
    :param university_name:
    """
    cursor = database.cursor()
    cursor.execute(f"SELECT rowid FROM universities WHERE name = '{university_name}'")
    university_id = cursor.fetchone()[0]
    cursor.execute(f"INSERT INTO faculties VALUES ({university_id}, '{faculty_data[0]}', '{faculty_data[1]}')")


def edit_url(database, change_params: tuple, new_url):
    """
    :param database:
    :param change_params: (что меняем универ или факультет, Имя университета, Имя факультета)
    1 - универ
    2 - факультет
    :param new_url:
    """
    cursor = database.cursor()
    match change_params[0]:
        case 1:
            cursor.execute(f"UPDATE universities WHERE name = '{change_params[1]}' SET url = '{new_url}'")
        case 2:
            sql = f"""
                UPDATE faculties 
                SET url = '{new_url}'
                WHERE (name = '{change_params[2]}')  
                AND (university_id = (SELECT rowid FROM universities WHERE name = '{change_params[1]}'))
                """
            cursor.execute(sql)
