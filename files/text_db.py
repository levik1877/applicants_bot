vay_to_user_file = "files/users.txt"
vay_to_selected_u_and_aoe_file = "files/selected_u_and_aoe.txt"


def get_user(user_id: int) -> tuple:
    with open(file=vay_to_user_file, mode="r", encoding='utf-8') as file:
        db = file.readlines()
        db = [i.split('|') for i in db]
        for i in range(len(db)):
            if int(db[i][0]) == user_id:
                return tuple(db[i])
        else:
            return (None, None, None, None, None)


def add_user(user_data: tuple):
    with open(file=vay_to_user_file, mode='a', encoding='utf-8') as file:
        file.write(f'{user_data[0]}|{user_data[1]}|{user_data[2]}|{user_data[3]}|{user_data[4]}\n')


def check_user(user_id: int) -> bool:
    with open(file=vay_to_user_file, mode='r', encoding='utf-8') as file:
        db = file.readlines()
        db = [i.split('|') for i in db]
        for i in range(len(db)):
            if int(db[i][0]) == user_id:
                return True
        else:
            return False


def select_u_and_aoe(user_id: int, university: str, area_of_education: str):
    with open(file=vay_to_selected_u_and_aoe_file, mode='a', encoding='utf-8') as file:
        file.write(f'{user_id}|{university}|{area_of_education}')


def get_selected_u_and_aoe(user_id: int) -> tuple:
    with open(file=vay_to_selected_u_and_aoe_file, mode='r', encoding='utf-8') as file:
        db = file.readlines()
        db = [i.split('|') for i in db]
        for i in range(len(db)):
            if int(db[i][0]) == user_id:
                return (db[i][1], db[i][2])
        else:
            return (None, None)
