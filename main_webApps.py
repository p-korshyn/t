from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot=Bot('6671202999:AAHDIInqZHnlwAHBWnsv9r3h0tPmTOO_z2c')
dp=Dispatcher(bot)

@dp.message_handler(commands=['start']) 
async def start(message: types.Message):
    markup=types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Website', web_app=WebAppInfo(url='http://pypi.org')))
    await message.answer('Привет!', reply_markup=markup)







executor.start_polling(dp)