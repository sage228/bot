import datetime
import config
import asyncio
from aiogram import Bot, Dispatcher, executor, types

#bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#echo
@dp.message_handler()
async def echo(message: types.Message):
    today = datetime.datetime.now()
    bday = datetime.datetime(2022, 12, 30)
    st = ''
    raznitsa = bday - today
    days, seconds = raznitsa.days, raznitsa.seconds
    hours = str(seconds // 3600-3)
    minutes = str((seconds % 3600) // 60)
    seconds = str(seconds % 60)
    days = str(days)
    await message.answer('До дня рождения мамочки осталось ' + days + ' дней ' + hours + ' часов ' + minutes + ' мигут ' + seconds + ' секунд')

# run long-polling
if __name__=='__main__':
    executor.start_polling(dp, skip_updates=False)
