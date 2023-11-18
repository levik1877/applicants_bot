import sqlite3

way_to_database = r"C:\Users\levvo\Desktop\applicants_bot\telegram_DB\users_data.db"


def create_table():
    """Содаёт чистенькую БД"""
    with sqlite3.connect(way_to_database) as data_base:
        data_base.execute("CREATE TABLE users (telegram_user_id INTEGER, snils TEXT, name TEXT, surname TEXT, patronymic TEXT)")
        data_base.execute("CREATE TABLE universities (name TEXT, faculties TEXT, city_id INTEGER)")
        data_base.execute("CREATE TABLE cities (name TEXT)")
        data_base.execute("CREATE TABLE faculties (name TEXT)")
        data_base.execute("CREATE TABLE areas_of_education (university_id INTEGER, faculty_id INTEGER, name TEXT, description TEXT)")
        sql = """
            CREATE TABLE selected_areas_of_education (user_id INTEGER, 
            aoe1 INTEGER, aoe2 INTEGER, aoe3 INTEGER, aoe4 INTEGER, aoe5 INTEGER, 
            aoe6 INTEGER, aoe7 INTEGER, aoe8 INTEGER, aoe9 INTEGER, aoe10 INTEGER, 
            aoe11 INTEGER, aoe12 INTEGER, aoe13 INTEGER, aoe14 INTEGER, aoe15 INTEGER, 
            aoe16 INTEGER, aoe17 INTEGER, aoe18 INTEGER, aoe19 INTEGER, aoe20 INTEGER, 
            aoe21 INTEGER, aoe22 INTEGER, aoe23 INTEGER, aoe24 INTEGER, aoe25 INTEGER)
            """
        data_base.execute(sql)
        sql = """
            CREATE TABLE selected_universities (user_id int, 
            u1 INTEGER,  u2 INTEGER,  u3 INTEGER,  u4 INTEGER,  u5 INTEGER)
            """
        data_base.execute(sql)
        data_base.commit()


def open_database():
    """
    :return: Файл БД
    """
    database = sqlite3.connect(way_to_database)
    return database


def add_user(database, user_telegram_id: int, user_snils: str, user_name: str, user_surname: str, user_patronymic: str, selected_universities: list, selected_areas_of_education: list):
    """
    :param database:
    :param user_telegram_id:
    :param user_snils:
    :param user_name:
    :param user_surname:
    :param user_patronymic:
    :param selected_universities: [0, selected_university1, selected_university2, ... , selected_university5]
    :param selected_areas_of_education: [0, selected_area_of_education1, selected_area_of_education2, ... , selected_area_of_education25]
    """
    cursor = database.cursor()
    cursor.execute(f"INSERT INTO users VALUES {(user_telegram_id, user_snils, user_name, user_surname, user_patronymic)}")
    cursor.execute(f"SELECT rowid FROM users WHERE telegram_user_id = {user_telegram_id}")
    db_user_id = cursor.fetchone()[0]
    selected_universities[0] = db_user_id
    cursor.execute(f"INSERT INTO selected_universities VALUES {tuple(selected_universities)}")
    selected_areas_of_education[0] = db_user_id
    cursor.execute(f"INSERT INTO selected_areas_of_education VALUES {tuple(selected_areas_of_education)}")
    cursor.close()


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
        SELECT * FROM selected_areas_of_education 
        JOIN users 
        WHERE (selected_areas_of_education.user_id = users.rowid) AND (telegram_user_id = {user_id})
        """
    user_selected_areas_of_education = cursor.execute(sql)
    user_info = []
    [user_info.append(i) for i in user_snils_fio]
    user_info.append(user_selected_universities)
    user_info.append(user_selected_areas_of_education)
    cursor.close()
    return user_info


def edit_user_snils(database, user_telegram_id: int, new_snils: str):
    cursor = database.cursor()
    cursor.execute(f"UPDATE users SET snils = '{new_snils}' WHERE telegram_user_id = {user_telegram_id}")
    cursor.close()


def edit_user_fio(database, user_telegram_id: int, new_fio: tuple):
    cursor = database.cursor()
    cursor.execute(f"UPDATE users SET name = '{new_fio[0]}' WHERE telegram_user_id = {user_telegram_id}")
    cursor.execute(f"UPDATE users SET surname = '{new_fio[1]}' WHERE telegram_user_id = {user_telegram_id}")
    cursor.execute(f"UPDATE users SET patronymic = '{new_fio[2]}' WHERE telegram_user_id = {user_telegram_id}")
    cursor.close()


def edit_user_selected_university(database, user_telegram_id: int, selected_university_number: int, new_selected_university_name: str):
    cursor = database.cursor()
    sql = f"""
        UPDATE selected_universities 
        SET u{selected_university_number} = (SELECT rowid FROM universities WHERE name = '{new_selected_university_name}') 
        WHERE user_id = (SELECT rowid FROM users WHERE telegram_user_id = {user_telegram_id})
        """
    cursor.execute(sql)
    cursor.close()


def edit_user_selected_areas_of_education(database, user_telegram_id: int, selected_area_of_education_number: int, new_selected_area_of_education_name: str):
    cursor = database.cursor()
    sql = f"""
        UPDATE selected_areas_of_education 
        SET aoe{selected_area_of_education_number} = (SELECT rowid FROM areas_of_education_number WHERE name = '{new_selected_area_of_education_name}')  
        WHERE user_id = (SELECT rowid FROM users WHERE telegram_user_id = {user_telegram_id})
        """
    cursor.execute(sql)
    cursor.close()


def check_user(database, user_id: int):
    cursor = database.cursor()
    cursor.execute(f"SELECT rowid FROM users WHERE telegram_user_id = {user_id}")
    if cursor.fetchone() is None:
        cursor.close()
        return False
    else:
        cursor.close()
        return True


def add_university(database, university_data: list):
    """
    :param database:
    :param university_data: [название университета, [id факультетов], город]
    """
    cursor = database.cursor()
    # ДОДЕЛАТЬ! нужно продумать как хранить информацию о факультетах в университете
    cursor.execute(f"INSERT INTO universities VALUES {university_data}")
    cursor.close()


def add_area_of_education(database, area_of_education_data: tuple, university_name: str):
    """
    :param database:
    :param area_of_education_data: (код направления подготовки, название факультета, описание направления подготовки)
    :param university_name:
    """
    cursor = database.cursor()
    cursor.execute(f"SELECT rowid FROM universities WHERE name = '{university_name}'")
    university_id = cursor.fetchone()[0]
    cursor.execute(f"INSERT INTO areas_of_education VALUES ({university_id}, '{area_of_education_data[0]}', '{area_of_education_data[1]}', '{area_of_education_data[2]}')")
    cursor.close()


def get_universities(database, city: str):
    cursor = database.cursor()
    universities = cursor.execute(f"SELECT * FROM universities WHERE city_id = (SELECT rowid FROM cities WHERE name = '{city}')").fetchall()
    cursor.close()
    return universities


def get_faculties(database): #НЕ ПРАВИЛЬНО переделать чтобы возвращала список факультетв конкретного университета
    cursor = database.cursor()
    faculties = cursor.execute("SELECT * FROM faculties").fetchall()
    cursor.close()
    return faculties


def get_areas_of_education(database, university_name: str, faculty_name: str):
    cursor = database.cursor()
    sql = f"""
    SELECT * 
    FROM areas_of_education 
    WHERE (university_id = (SELECT rowid FROM universities WHERE name = '{university_name}')) 
    AND (faculty_id = (SELECT rowid FROM faculties WHERE name = '{faculty_name}'))
    """
    area_of_education = cursor.execute(sql).fetchall()
    cursor.close()
    return area_of_education


def add_cities(database, city_name: str):
    cursor = database.cursor()
    cursor.execute(f"INSERT INTO cities VALUES ('{city_name}')") # чёт не робит
    cursor.close()


def get_cities(database):
    cursor = database.cursor()
    cities = cursor.execute("SELECT * FROM cities").fetchall()
    cursor.close()
    return cities

