#Подключаем модуль для телеграма
import telebot
#Подключаем модуль случайных чисел
import random
#импортируем кнопки
from telebot import types
#Указываем токен
bot = telebot.TeleBot('5339650828:AAF_-H1zHjLd2YTyYnlZPLU18ZeDH-vPWBY')
#Готовим информацию для кнопок
classic = ["Война и мир- Л.Толстой" "Преступление и наказание-Ф.Достаевский" "Мастер и Маргарита-М.Булгаков"]
detective = ["Безмолвный пациент-А.Михаэлидес", "Внутри убийцы-М.Омер", "Дурная кровь-Д.Роулинг"]
psychology = ["Игры, в которые играют люди-Э.Берн", "Психология влияния-Р.Чалдини", "ВВедение в психоанализ-З.Фрейд"]
fiction = ["1984-Д.Оруэлл", "451 градус по Фаренгуйту-Р.Брэдбери", "Солярис-С.Лем"]
horror = ["Сияние, Оно-С.Кинг", "Дракула-Б.Стокер"]
medicine = ["Не навреди-Г.Марш", "Будет больно-А.Кей", "Неестественные причины-Р.Шеперд"]
story = ["История Древней Греции", "История Беларуси", "Всемирная история"]
novels = ["Джейн Эйр-Ш.Бронте", "Поющие в терновнике-К.Маккалоу", "Город женщин-Э.Гилберт"]
#метод для получения и обработки сообщений
@bot.message_handler(content_types = ['text'])
def get_user_text(message):
    if message.text == "Привет":
        mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name} </b>. Я телеграм-бот. Давай поговорим? (Пожалуйста, все ответы пиши с маленькой буквы, я пока только так запрограмирован. Спасибо!)'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    elif message.text == "давай":
        bot.send_message(message.from_user.id, "Можешь у меня, что нибудь спросить. Я пока мало, что умею, но я учусь." )

    elif message.text == "привет":
        bot.send_message(message.from_user.id, "Напиши Привет с большой буквы")

    elif message.text == "конечно":
        #готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        #по очереди готовим текст и обратотку для кадого жанра книг
        key_classic = types.InlineKeyboardButton(text="Классика", callback_data="book")
        #добавляем кнопку на экран
        keyboard.add(key_classic)
        key_detective = types.InlineKeyboardButton(text="Детектив", callback_data="book")
        keyboard.add(key_detective)
        key_psychology = types.InlineKeyboardButton(text="Психология", callback_data="book")
        keyboard.add(key_psychology)
        key_fiction = types.InlineKeyboardButton(text="Фантастика", callback_data="book")
        keyboard.add(key_fiction)
        key_horror = types.InlineKeyboardButton(text="Ужасы", callback_data="book")
        keyboard.add(key_horror)
        key_medicine = types.InlineKeyboardButton(text="Медицина", callback_data="book")
        keyboard.add(key_medicine)
        key_story = types.InlineKeyboardButton(text="История", callback_data="book")
        keyboard.add(key_story)
        key_novels = types.InlineKeyboardButton(text="Романы", callback_data="book")
        keyboard.add(key_novels)
        bot.send_message(message.from_user.id, "Ты выбрал конечно, тогда я предлогаю тебе выбрать тот жанр, который нравиться тебе, а я предложу тебе пару рандомных книг книг для чтения разных жанров, что читал сам.", reply_markup=keyboard)


    elif message.text == "не очень":
        bot.send_message(message.from_user.id, "Тогда нам не о чем разговаривать! Давай прощаться! Это конечно твое дело,но все же можно и почитать!")

    elif message.text == "как дела?":
        bot.send_message(message.chat.id, f'Можно было бы и поздароваться', parse_mode='html')

    elif message.text == "я поздоровался":
        bot.send_message(message.chat.id, f'Я шучу, сегодня хорошее настроение!', parse_mode='html')

    elif message.text == "я поздоровалась":
        bot.send_message(message.chat.id, f'Ладно, ты же девочка, тебе можно!' , parse_mode='html')

    elif message.text == "что ты умеешь?":
        bot.send_message(message.chat.id, f'Смотря, что тебя интересует?', parse_mode='html')

    elif message.text == "давай дружить":
        bot.send_message(message.chat.id, f'Спасибо за предложение, я готов!', parse_mode='html')

    elif message.text == "что расскажешь?":
        bot.send_message(message.chat.id, f'Могу сказку рассказать, а лучше конечно загугли. Хотя ладно давай расскажу, а то что я за человек то такой, что ничего не знаю и не умею!!! А я много чего умею, просто стесняюсь. Умею крестиком вышивать, гладить, убирать, ухаживать за рыбками.  Люди сейчас такие злые и ужасные, что страшно даже, что то говорить о себе, сразу издеваються. Я надеюсь ты ни такой ? Просто ответь да или нет',parse_mode='html')

    elif message.text == "нет":
        bot.send_message(message.chat.id, f'Хорошо, я поверю тебе. Теперь я задам тебе вопрос, любишь ли ты читать книги(предлогаю ответить либо конечно либо не очень)?', parse_mode='html')

    elif message.text == "да":
        bot.send_message(message.chat.id, f'Тогда нам стоит проститься! Было не приятно познакомиться ', parse_mode='html')

    elif message.text == "пока":
        bot.send_message(message.chat.id, f'До свидания! Хорошего тебе дня, человек!', parse_mode='html')

    elif message.text == "до свидания":
        bot.send_message(message.chat.id, f'До свидания, хорошего тебе дня милый человек. Спасибо за общение!')

    elif message.text == "спасибо":
        bot.send_message(message.chat.id, f'Будешь должен, как говориться! Ладно шучу, говорю же настроение хорошее!', parse_mode='html')

    elif message.text == "все":
        bot.send_message(message.chat.id, f'Google в помощь', parse_mode='html')

    elif message.text == "спокойной ночи":
        bot.send_message(message.chat.id, f'Доброй ночи человек.', parse_mode='html')

    elif message.text == "давай расскажи":
        bot.send_message(message.chat.id, f'Жила была девочка. И был у этой девочки компьютер и мышка. Начала девочка каждый день работать на компьтере, писать какие то не понятные другим людям "закорючки". Все кто знал эту девочку, говорили ей, что надо найти нормальную работу, но она их не слушала и правильно делала. Через время она добилась успеха и уехала жить в другую страну, начала путешевствовать. Вот такая сказка с хорошим концом. ')

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, давай сначала.Напиши привет ")
#обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    #если нажать на одну из кнопок, выведится список книг
    if call.data == "book":
        #формируется список книг
        libr = random.choice(classic) + ' ' + random.choice(detective) + ' ' + random.choice(psychology) + ' ' + random.choice(fiction) + ' ' + random.choice(horror) + ' ' + random.choice(medicine) + ' ' + random.choice(story) + ' ' + random.choice(novels)
        #отправлем текст в Телеграм
        bot.send_message(call.message.chat.id, libr)

#запускаем постоянный опрос бота в Телеграм
bot.polling(none_stop=True, interval=0)
