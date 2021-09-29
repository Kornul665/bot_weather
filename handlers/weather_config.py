import requests
from datetime import datetime
import config
from aiogram import types, Dispatcher


async def get_weather(message: types.Message):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U0001F325",
        "Rain": "Дождь \U0001F326",
        "Drizzle": "Дождь \U0001F327",
        "Thunderstorm": "Гроза \U0001F329",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&lang=ru&appid={config.TOKEN}&units=metric"
        )

        # picking up the dictionary
        data = r.json()

        city = data["name"]
        current_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            await message.reply("Выгляни в окно, чего то не пойму что там происходит. ")

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.fromtimestamp(
            data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(
            data["sys"]["sunset"])

        length_day = sunset - sunrise

        await message.reply(f"\U0001F341{datetime.now().strftime('%Y-%m-%d %H:%M')}\U0001F30D"
                            f"\nПогода в городе: {city}\nТемпература: {current_weather}С° {wd}\nВлажность: {humidity}\n"
                            f"Давление: {pressure}мм.рт.ст\nСкорость ветра: {wind}м/с\n"
                            f"Восход: {sunrise}\nЗакат: {sunset}\n"
                            f"Продолжительность светового дня: {length_day}"
                            "\nВсего доброго.")
    except:
        await message.reply("Проверьте название города")


def register_heandlers_other(dp: Dispatcher):
    dp.register_message_handler(get_weather)
