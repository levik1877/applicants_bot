from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import files.text_for_answer as a_text


def start_question_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text=a_text.start_test_question1_answer_option_1)
    builder.button(text=a_text.start_test_question1_answer_option_2)
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def cities():
    builder = ReplyKeyboardBuilder()
    city = ['Москва', 'Санкт-Петербург', 'Ростов-на-Дону']
    for i in range(len(city)):
        builder.button(text=city[i])
    a = [1, 1, 1]
    builder.adjust(*a)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def rnd_u():
    builder = ReplyKeyboardBuilder()
    u = ['Южный федеральный университет',
         'Донской государственный технический университет',
         'Российская академия народного хозяйства и государственной службы',
         'Ростовский государственный экономический университет',
         'Ростовский медецинский университет'
    ]
    for i in range(len(u)):
        builder.button(text=u[i])
    a = [1]*len(u)
    builder.adjust(*a)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def donstu_faculties():
    builder = ReplyKeyboardBuilder()
    f = [
        '01.00.00 Математика и механика',
        '02.00.00 Компьютерные и информационные науки',
        '03.00.00 Физика и астрономия',
        '07.00.00 Архитектура',
        '08.00.00 Техника и технологии строительства',
        '09.00.00 Информатика и вычислительная техника',
        '10.00.00 Информационная безопасность',
        '11.00.00 Электроника, радиотехника и системы связи',
        '12.00.00 Фотоника, приборостроение, оптические и биотехнические системы и технологии',
        '13.00.00 Электро- и теплоэнергетика',
        '15.00.00 Машиностроение',
        '16.00.00 Физико-технические науки и технологии',
        '18.00.00 Химические технологии',
        '19.00.00 Промышленная экология и биотехнологии',
        '20.00.00 Техносферная безопасность и природообустройство',
        '21.00.00 Прикладная геология, горное дело, нефтегазовое дело и геодезия',
        '22.00.00 Технологии материалов',
        '23.00.00 Техника и технологии наземного транспорта',
        '24.00.00 Авиационная и ракетно-космическая техника',
        '25.00.00 Аэронавигация и эксплуатация авиационной и ракетно-космической техники',
        '27.00.00 Управление в технических системах',
        '28.00.00 Нанотехнологии и материалы',
        '29.00.00 Технологии легкой промышленности',
        '33.00.00 Фармация',
        '35.00.00 Сельское, лесное и рыбное хозяйство',
        '36.00.00 Ветеринария и зоотехния',
        '37.00.00 Психологические науки',
        '38.00.00 Экономика и управления',
        '39.00.00 Социология и социальная работа',
        '40.00.00 Юриспруденция',
        '42.00.00 Средства массовой информации и информационно-библиотечное дело ',
        '43.00.00 Сервис и туризм',
        '44.00.00 Образование и педагогические науки',
        '44.00.00 Образование и педагогические науки',
        '45.00.00 Языкознание и литературоведение',
        '46.00.00 История и археология',
        '48.00.00 Теология',
        '49.00.00 Физическая культура и спорт',
        '51.00.00 Культуроведение и социально культурные проекты',
        '54.00.00 Изобразительное и прикладные виды искусств'
    ]
    for i in range(len(f)):
        builder.button(text=f[i])
    a = [1]*len(f)
    builder.adjust(*a)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def iivt():
    builder = ReplyKeyboardBuilder()
    aoe = [
        '09.03.01 Информатика и вычислительная техника',
        '09.03.02 Информационные системы и технологии',
        '09.03.03 Прикладная информатика',
        '09.03.04 Программная инженерия'
    ]
    for i in range(len(aoe)):
        builder.button(text=aoe[i])
    a = [1]*len(aoe)
    builder.adjust(*a)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Выбрать ВУЗы")
    builder.button(text="Профиль")
    builder.button(text="Аналитика")
    builder.adjust(1, 2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def profile():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Изменить данные")
    builder.button(text="Назад")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def analytics():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Подробнее")
    builder.button(text="Назад")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def register_final_check_answer():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Всё верно")
    builder.button(text="Изменить данные")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def choice_u_and_aoe_menu(city: str):
    builder = ReplyKeyboardBuilder()
    builder.button(text="Добавить направление подготовки")
    builder.button(text=f"Добавить ВУЗ в городе {city}")
    builder.button(text="Выбрать другой город")
    builder.button(text="Вернуться в меню")
    builder.adjust(1, 1, 1, 1)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)