from django.shortcuts import render
from django.conf import settings
from aiogram import Bot, Dispatcher, types, executor
from asgiref.sync import sync_to_async
from logging import basicConfig, INFO

from apps.telegram.models import TelegramUser
from apps.telegram.keyboards import start_markup, courses_button

# Create your views here.
bot = Bot(settings.TELEGRAM_TOKEN)
dp = Dispatcher(bot)
basicConfig(level=INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    user = await sync_to_async(TelegramUser.objects.get_or_create)(
        id_user=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        chat_id=message.chat.id
    )
    await message.answer(f"Привет {message.from_user.full_name}", reply_markup=start_markup)

@dp.message_handler(text='👨‍🎓 Наши курсы')
async def get_courses(message:types.Message):
    await message.answer('🥳 Выбери язык программирования! 🥳', reply_markup=courses_button)