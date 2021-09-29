from aiogram import types
from aiogram.utils import executor
from create_bot import dp, bot
from handlers import weather_config


async def on_startup(_):
    print("Bot run!")


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):

    await bot.send_message(message.from_user.id, "Привет {0.first_name}!".format(message.from_user) + "\nВ каком городе узнать погоду?")

weather_config.register_heandlers_other(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
