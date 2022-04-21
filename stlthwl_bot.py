import telebot
from telebot import types
import config
import converter
import currency
import wether
import news
import datetime


token = config.token
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Курсы валют', 'Погода')
    markup.row('Конвертер величин', 'Новости')
    bot.send_message(message.chat.id, 'Выбери нужный раздел, пользуясь подсказками ниже👇🏻', reply_markup=markup)
    bot.register_next_step_handler(message, section_selection)


def section_selection(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.InlineKeyboardMarkup()
    if message.text == 'Курсы валют':
        markup.row('Обменник')
        markup.row('Назад')
        try:
            usd = currency.Currency('usd')
            usd = usd.get_currency(currency.url_usd)
            eur = currency.Currency('eur')
            eur = eur.get_currency(currency.url_eur)
            btc = currency.Currency('btc')
            btc = btc.get_crypto(currency.url_btc)
            eth = currency.Currency('eth')
            eth = eth.get_crypto(currency.url_eth)
            bot.send_message(message.chat.id, f'USD: {usd} RUB', reply_markup=markup)
            bot.send_message(message.chat.id, f'EUR: {eur} RUB', reply_markup=markup)
            bot.send_message(message.chat.id, f'BTC: {btc} USD', reply_markup=markup)
            bot.send_message(message.chat.id, f'ETH: {eth} USD', reply_markup=markup)
            bot.register_next_step_handler(message, money_exchange_menu)
        except Exception:
            bot.send_message(message.chat.id, 'сервис недоступен\nпопробуй позже', reply_markup=markup)
            bot.register_next_step_handler(message, money_exchange)
    elif message.text == 'Погода' or message.text == 'Назад':
        markup.row('Москва', 'Санкт-Петербург')
        markup.row('Казань', 'Уфа')
        markup.row('Екатеринбург', 'Пермь')
        markup.row('Новосибирск', 'Владивосток')
        markup.row('Назад')
        bot.send_message(message.from_user.id, 'Выбери город из списка\nили введи нужный', reply_markup=markup)
        bot.register_next_step_handler(message, get_weather)
    elif message.text == 'Конвертер величин' or message.text == 'вернуться назад':
        markup.row('Длина', 'Масса')
        markup.row('Объем', 'Температура')
        markup.row('Назад')
        msg = bot.send_message(message.chat.id, 'Выбери раздел?', reply_markup=markup)
        bot.register_next_step_handler(msg, converter_value)
    elif message.text == 'Новости':
        markup.row('Назад')
        try:
            n_l = news.News('news')
            n_l = n_l.get_news_line(news.url_news)
            bot.send_message(message.from_user.id, f'{n_l}', reply_markup=markup)
            link_btn = types.InlineKeyboardButton(text='подробнее',
                                                  url='https://lenta.ru/')
            keyboard.add(link_btn)
            bot.send_message(message.chat.id, 'источник по ссылке ниже 👇🏻', reply_markup=keyboard)
            bot.register_next_step_handler(message, start)
        except Exception:
            bot.send_message(message.chat.id, 'сервис недоступен\nпопробуй позже')
            bot.register_next_step_handler(message, start)
    else:
        markup.row('Курсы валют', 'Погода')
        markup.row('Конвертер величин', 'Новости')
        bot.send_message(message.chat.id, 'Выбери нужный раздел, пользуясь подсказками ниже👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def money_exchange_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if message.text == 'Обменник':
        markup.row('USD  ➡  RUB', 'RUB  ➡  USD')
        markup.row('USD  ➡  EUR', 'EUR  ➡  USD')
        markup.row('EUR  ➡  RUB', 'RUB  ➡  EUR')
        markup.row('Назад')
        bot.send_message(message.chat.id, 'выбери пару для обмена', reply_markup=markup)
        bot.register_next_step_handler(message, money_exchange)
    else:
        markup.row('Курсы валют', 'Погода')
        markup.row('Конвертер величин', 'Новости')
        bot.send_message(message.chat.id, 'Выбери нужный раздел, пользуясь подсказками ниже👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def money_exchange(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'USD  ➡  RUB':
        bot.send_message(message.chat.id, 'введи сумму USD', reply_markup=markup)
        bot.register_next_step_handler(message, usd_in_rub)
    elif message.text == 'RUB  ➡  USD':
        bot.send_message(message.chat.id, 'введи сумму RUB', reply_markup=markup)
        bot.register_next_step_handler(message, rub_in_usd)
    elif message.text == 'USD  ➡  EUR':
        bot.send_message(message.chat.id, 'введи сумму USD', reply_markup=markup)
        bot.register_next_step_handler(message, usd_in_eur)
    elif message.text == 'EUR  ➡  USD':
        bot.send_message(message.chat.id, 'введи сумму EUR', reply_markup=markup)
        bot.register_next_step_handler(message, eur_in_usd)
    elif message.text == 'EUR  ➡  RUB':
        bot.send_message(message.chat.id, 'введи сумму EUR', reply_markup=markup)
        bot.register_next_step_handler(message, eur_in_rub)
    elif message.text == 'RUB  ➡  EUR':
        bot.send_message(message.chat.id, 'введи сумму RUB', reply_markup=markup)
        bot.register_next_step_handler(message, rub_in_eur)
    else:
        markup.row('Курсы валют', 'Погода')
        markup.row('Конвертер величин', 'Новости')
        bot.send_message(message.chat.id, 'Выбери нужный раздел, пользуясь подсказками ниже👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def usd_in_rub(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    usd = currency.Currency('usd')
    usd = usd.get_currency(currency.url_usd)
    markup.row('USD  ➡  RUB', 'RUB  ➡  USD')
    markup.row('USD  ➡  EUR', 'EUR  ➡  USD')
    markup.row('EUR  ➡  RUB', 'RUB  ➡  EUR')
    markup.row('Назад')
    try:
        date = datetime.datetime.now()
        now = str(date.strftime("%d.%m.%Y %H:%M"))
        rub = round(float(message.text) * usd, 2)
        bot.send_message(message.chat.id, f'{now}\n{message.text} $ = {rub} ₽ по курсу ЦБ',
                         reply_markup=markup)
        bot.register_next_step_handler(message, money_exchange)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать\nвыбери пару')
        bot.register_next_step_handler(message, money_exchange)


def rub_in_usd(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    usd = currency.Currency('usd')
    usd = usd.get_currency(currency.url_usd)
    markup.row('USD  ➡  RUB', 'RUB  ➡  USD')
    markup.row('USD  ➡  EUR', 'EUR  ➡  USD')
    markup.row('EUR  ➡  RUB', 'RUB  ➡  EUR')
    markup.row('Назад')
    try:
        date = datetime.datetime.now()
        now = str(date.strftime("%d.%m.%Y %H:%M"))
        res = round(float(message.text) / usd, 2)
        bot.send_message(message.chat.id, f'{now}\n{message.text} ₽ = {res} $ по курсу ЦБ',
                         reply_markup=markup)
        bot.register_next_step_handler(message, money_exchange)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать\nвыбери пару')
        bot.register_next_step_handler(message, money_exchange)


def usd_in_eur(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    eur = currency.Currency('eur')
    eur = eur.get_currency(currency.url_eur)
    usd = currency.Currency('usd')
    usd = usd.get_currency(currency.url_usd)
    markup.row('USD  ➡  RUB', 'RUB  ➡  USD')
    markup.row('USD  ➡  EUR', 'EUR  ➡  USD')
    markup.row('EUR  ➡  RUB', 'RUB  ➡  EUR')
    markup.row('Назад')
    try:
        date = datetime.datetime.now()
        now = str(date.strftime("%d.%m.%Y %H:%M"))
        res = round(float(message.text) * (usd / eur), 2)
        bot.send_message(message.chat.id, f'{now}\n{message.text} $ = {res} € по курсу ЦБ',
                         reply_markup=markup)
        bot.register_next_step_handler(message, money_exchange)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать\nвыбери пару')
        bot.register_next_step_handler(message, money_exchange)


def eur_in_usd(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    eur = currency.Currency('eur')
    eur = eur.get_currency(currency.url_eur)
    usd = currency.Currency('usd')
    usd = usd.get_currency(currency.url_usd)
    markup.row('USD  ➡  RUB', 'RUB  ➡  USD')
    markup.row('USD  ➡  EUR', 'EUR  ➡  USD')
    markup.row('EUR  ➡  RUB', 'RUB  ➡  EUR')
    markup.row('Назад')
    try:
        date = datetime.datetime.now()
        now = str(date.strftime("%d.%m.%Y %H:%M"))
        res = round(float(message.text) * (eur / usd), 2)
        bot.send_message(message.chat.id, f'{now}\n{message.text} € = {res} $ по курсу ЦБ',
                         reply_markup=markup)
        bot.register_next_step_handler(message, money_exchange)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать\nвыбери пару')
        bot.register_next_step_handler(message, money_exchange)


def eur_in_rub(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    eur = currency.Currency('eur')
    eur = eur.get_currency(currency.url_eur)
    markup.row('USD  ➡  RUB', 'RUB  ➡  USD')
    markup.row('USD  ➡  EUR', 'EUR  ➡  USD')
    markup.row('EUR  ➡  RUB', 'RUB  ➡  EUR')
    markup.row('Назад')
    try:
        date = datetime.datetime.now()
        now = str(date.strftime("%d.%m.%Y %H:%M"))
        res = round(float(message.text) * eur, 2)
        bot.send_message(message.chat.id, f'{now}\n{message.text} € = {res} ₽ по курсу ЦБ',
                         reply_markup=markup)
        bot.register_next_step_handler(message, money_exchange)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать\nвыбери пару')
        bot.register_next_step_handler(message, money_exchange)


def rub_in_eur(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    eur = currency.Currency('eur')
    eur = eur.get_currency(currency.url_eur)
    markup.row('USD  ➡  RUB', 'RUB  ➡  USD')
    markup.row('USD  ➡  EUR', 'EUR  ➡  USD')
    markup.row('EUR  ➡  RUB', 'RUB  ➡  EUR')
    markup.row('Назад')
    try:
        date = datetime.datetime.now()
        now = str(date.strftime("%d.%m.%Y %H:%M"))
        res = round(float(message.text) / eur, 2)
        bot.send_message(message.chat.id, f'{now}\n{message.text} ₽ = {res} € по курсу ЦБ',
                         reply_markup=markup)
        bot.register_next_step_handler(message, money_exchange)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать\nвыбери пару')
        bot.register_next_step_handler(message, money_exchange)


def get_weather(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.row('Назад')
        get_city = message.text
        openweater_token = config.api_openweather_key
        city = wether.Get_Weather(get_city)
        city = city.get_any_city(get_city, openweater_token)
        bot.send_message(message.chat.id, f'{city}', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)
    except Exception:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Курсы валют', 'Погода')
        markup.row('Конвертер величин', 'Новости')
        bot.send_message(message.chat.id, 'Город не найден')
        bot.send_message(message.chat.id, 'Выбери нужный раздел, пользуясь подсказками ниже👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def converter_value(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    if message.text == 'Длина':
        markup.row('километры в мили')
        markup.row('метры в футы')
        markup.row('сантиметры в дюймы')
        bot.send_message(message.chat.id, 'что будем конвертировать?', reply_markup=markup)
        bot.register_next_step_handler(message, length)
    elif message.text == 'Масса':
        markup.row('килограммы в фунты')
        markup.row('граммы в унции')
        bot.send_message(message.chat.id, 'что будем конвертировать?', reply_markup=markup)
        bot.register_next_step_handler(message, weight)
    elif message.text == 'Объем':
        markup.row('литры в галоны')
        bot.send_message(message.chat.id, 'что будем конвертировать?', reply_markup=markup)
        bot.register_next_step_handler(message, volume)
    elif message.text == 'Температура':
        markup.row('°C -> F')
        markup.row('°C -> K')
        bot.send_message(message.chat.id, 'что будем конвертировать?', reply_markup=markup)
        bot.register_next_step_handler(message, temperature)
    else:
        markup.row('Курсы валют', 'Погода')
        markup.row('Конвертер величин', 'Новости')
        bot.send_message(message.chat.id, 'Выбери нужный раздел, пользуясь подсказками ниже👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def length(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'километры в мили':
        bot.send_message(message.chat.id, 'вводи километры')
        bot.register_next_step_handler(message, calc_mile)
    elif message.text == 'метры в футы':
        bot.send_message(message.chat.id, 'вводи метры')
        bot.register_next_step_handler(message, calc_feet)
    elif message.text == 'сантиметры в дюймы':
        bot.send_message(message.chat.id, 'вводи сантиметры')
        bot.register_next_step_handler(message, calc_inch)
    else:
        markup.row('Курсы валют', 'Погода')
        markup.row('Конвертер величин', 'Новости')
        bot.send_message(message.chat.id, 'Выбери нужный раздел, пользуясь подсказками ниже👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def weight(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'килограммы в фунты':
        bot.send_message(message.chat.id, 'вводи килограммы')
        bot.register_next_step_handler(message, calc_lb)
    elif message.text == 'граммы в унции':
        bot.send_message(message.chat.id, 'вводи граммы')
        bot.register_next_step_handler(message, calc_oz)
    else:
        markup.row('Курсы валют', 'Погода')
        markup.row('Конвертер величин', 'Новости')
        bot.send_message(message.chat.id, 'Выбери нужный раздел, пользуясь подсказками ниже👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def volume(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'литры в галоны':
        bot.send_message(message.chat.id, 'вводи литры')
        bot.register_next_step_handler(message, calc_gal)
    else:
        markup.row('Курсы валют', 'Погода')
        markup.row('Конвертер величин', 'Новости')
        bot.send_message(message.chat.id, 'Выбери нужный раздел, пользуясь подсказками ниже👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def temperature(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == '°C -> F':
        bot.send_message(message.chat.id, 'вводи градусы')
        bot.register_next_step_handler(message, calc_f)
    elif message.text == '°C -> K':
        bot.send_message(message.chat.id, 'вводи градусы')
        bot.register_next_step_handler(message, calc_k)
    else:
        markup.row('Курсы валют', 'Погода')
        markup.row('Конвертер величин', 'Новости')
        bot.send_message(message.chat.id, 'Выбери нужный раздел, пользуясь подсказками ниже👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def calc_mile(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Длина', 'Масса')
    markup.row('Объем', 'Температура')
    markup.row('Назад')
    try:
        mile = converter.Length('mile')
        mile = mile.km_in_mile(message.text)
        bot.send_message(message.chat.id, f'{message.text} километров - это {mile} миль', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать', reply_markup=markup)
        bot.send_message(message.chat.id, 'вводи цифры', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)


def calc_feet(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Длина', 'Масса')
    markup.row('Объем', 'Температура')
    markup.row('Назад')
    try:
        feet = converter.Length('feet')
        feet = feet.m_in_feet(message.text)
        bot.send_message(message.chat.id, f'{message.text} метров - это {feet} футов', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать', reply_markup=markup)
        bot.send_message(message.chat.id, 'вводи цифры', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)


def calc_inch(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Длина', 'Масса')
    markup.row('Объем', 'Температура')
    markup.row('Назад')
    try:
        inch = converter.Length('inch')
        inch = inch.cm_in_inch(message.text)
        bot.send_message(message.chat.id, f'{message.text} сантиметров - это {inch} дюймов', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать', reply_markup=markup)
        bot.send_message(message.chat.id, 'вводи цифры', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)


def calc_lb(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Длина', 'Масса')
    markup.row('Объем', 'Температура')
    markup.row('Назад')
    try:
        lb = converter.Weight('lb')
        lb = lb.kg_in_lb(message.text)
        bot.send_message(message.chat.id, f'{message.text} килограмм - это {lb} фунтов', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать', reply_markup=markup)
        bot.send_message(message.chat.id, 'вводи цифры', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)


def calc_oz(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Длина', 'Масса')
    markup.row('Объем', 'Температура')
    markup.row('Назад')
    try:
        oz = converter.Weight('oz')
        oz = oz.gm_in_oz(message.text)
        bot.send_message(message.chat.id, f'{message.text} грамм - это {oz} унций', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать', reply_markup=markup)
        bot.send_message(message.chat.id, 'вводи цифры', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)


def calc_gal(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Длина', 'Масса')
    markup.row('Объем', 'Температура')
    markup.row('Назад')
    try:
        gal = converter.Volume('gal')
        gal = gal.l_in_gal(message.text)
        bot.send_message(message.chat.id, f'{message.text} л - это {gal} г', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать', reply_markup=markup)
        bot.send_message(message.chat.id, 'вводи цифры', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)


def calc_f(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Длина', 'Масса')
    markup.row('Объем', 'Температура')
    markup.row('Назад')
    try:
        f = converter.Temperature('f')
        f = f.c_in_f(message.text)
        bot.send_message(message.chat.id, f'{message.text} °C - это {f} F', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать', reply_markup=markup)
        bot.send_message(message.chat.id, 'вводи цифры', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)


def calc_k(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Длина', 'Масса')
    markup.row('Объем', 'Температура')
    markup.row('Назад')
    try:
        k = converter.Temperature('k')
        k = k.c_in_k(message.text)
        bot.send_message(message.chat.id, f'{message.text} °C - это {k} K', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)
    except ValueError:
        bot.send_message(message.chat.id, 'это нельзя конвертировать', reply_markup=markup)
        bot.send_message(message.chat.id, 'вводи цифры', reply_markup=markup)
        bot.register_next_step_handler(message, converter_value)


bot.polling(none_stop=True)
