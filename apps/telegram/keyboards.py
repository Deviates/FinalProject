from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from apps.courses.models import Courses

start_keyboards = [
    KeyboardButton("👨‍🎓 Наши курсы"),
    KeyboardButton("✍️ Записаться на урок"),
    KeyboardButton("🎬 Пройти викторину"),
    KeyboardButton("❓ Часто задоваемые вопросы"),
]

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2,
).add(*start_keyboards)

####################################################

courses = Courses.objects.all()

courses_keyboards = [
    KeyboardButton(course.title) for course in courses
]

courses_button = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
).add(*courses_keyboards)