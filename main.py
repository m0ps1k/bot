import telebot
from telebot import types
bot = telebot.TeleBot('6685009085:AAFtRp79-NvCizU7UjeMai03suftSkPu73w')
from XI_vek import *
score = 0

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Конечно')
    markup.row_width = 1
    markup.row(btn1)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, готов ли ты пройти тест на знание архитектуры?', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Конечно':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)

def vek(message):
    if message.text == 'XI век':
        bot.send_message(message.chat.id, 'Начинаем!')
        file = open('./1.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Боголюбово')
        btn2 = types.KeyboardButton('Десятинная церковь')
        btn3 = types.KeyboardButton('Церковь Покрова Богородице на реке Нерли')
        btn4 = types.KeyboardButton('Дворец Алексея Михайловича в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XI_vek2)

    elif message.text == 'XII век':
        bot.send_message(message.chat.id, 'Начинаем!')
        file = open('./5.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Боголюбово')
        btn2 = types.KeyboardButton('Георгиевский собор Юрьева монастыря ')
        btn3 = types.KeyboardButton('Церковь Покрова Богородице на реке Нерли')
        btn4 = types.KeyboardButton('Архангельский собор Московского кремля')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek2)

    elif message.text == 'XIII-XIV века':
        bot.send_message(message.chat.id, 'Начинаем!')
        file = open('./16.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Боголюбово')
        btn2 = types.KeyboardButton('Московский кремль при Иване Калите ')
        btn3 = types.KeyboardButton('Церковь Покрова Богородице на реке Нерли')
        btn4 = types.KeyboardButton('Церковь Николы на Липне')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek2)

    elif message.text == 'XV век':
        bot.send_message(message.chat.id, 'Начинаем!')
        file = open('./23.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Собор Покрова на Рву (Храм Василия Блаженного)')
        btn2 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn3 = types.KeyboardButton('Церковь Покрова Богородице на реке Нерли')
        btn4 = types.KeyboardButton('Троицкий собор в Троицко-Сергеевом монастыре')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek2)

    elif message.text == 'XVI век':
        bot.send_message(message.chat.id, 'Начинаем!')
        file = open('./33.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Боголюбово')
        btn2 = types.KeyboardButton('Нижегородский кремль')
        btn3 = types.KeyboardButton('Смоленский кремль')
        btn4 = types.KeyboardButton('Дворец Алексея Михайловича в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek2)


    elif message.text == 'XVII века':
        bot.send_message(message.chat.id, 'Начинаем!')
        file = open('./1.1.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Боголюбово')
        btn2 = types.KeyboardButton('Нижегородский кремль')
        btn3 = types.KeyboardButton('Теремной дворец в Московском кремле')
        btn4 = types.KeyboardButton('Дворец Алексея Михайловича в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek2)
        









def XI_vek2(message):
    if message.text == 'Десятинная церковь':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./2.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Десятинная церковь')
        btn4 = types.KeyboardButton('Софийский собор в Киеве 1037 г., перестройка и современный вид')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XI_vek3)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./2.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Десятинная церковь')
        btn4 = types.KeyboardButton('Софийский собор в Киеве 1037 г., перестройка и современный вид')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XI_vek3)
        
def XI_vek3(message):
    if message.text == 'Софийский собор в Киеве 1037 г., перестройка и современный вид':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./3.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn3 = types.KeyboardButton('Золотые ворота в Киеве')
        btn4 = types.KeyboardButton('Теремной дворец в Московском кремле')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XI_vek4)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./3.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn3 = types.KeyboardButton('Золотые ворота в Киеве')
        btn4 = types.KeyboardButton('Теремной дворец в Московском кремле')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XI_vek4)

def XI_vek4(message):
    if message.text == 'Золотые ворота в Киеве':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./4.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Десятинная церковь')
        btn3 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XI_vek5)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./4.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Десятинная церковь')
        btn3 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XI_vek5)

def XI_vek5(message):

    if message.text =='Софийский собор в Новгороде Великом':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0 
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)
    else:
        bot.reply_to(message, "Это неправильный ответ")
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)

        


    
    
    












def XII_vek2(message):
    if message.text == 'Георгиевский собор Юрьева монастыря':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./6.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Спаса Преображения на реке Нередице')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Нижегородский кремль')
        btn4 = types.KeyboardButton('Софийский собор в Киеве 1037 г., перестройка и современный вид')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek3)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./6.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Спаса Преображения на реке Нередице')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Нижегородский кремль')
        btn4 = types.KeyboardButton('Софийский собор в Киеве 1037 г., перестройка и современный вид')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek3)
        
def XII_vek3(message):
    if message.text == 'Церковь Спаса Преображения на реке Нередице':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./7.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn3 = types.KeyboardButton('Спасо-Преоброженский собор Мирожского монастыря в Пскове')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek4)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./7.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn3 = types.KeyboardButton('Спасо-Преоброженский собор Мирожского монастыря в Пскове')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek4)

def XII_vek4(message):
    if message.text == 'Спасо-Преоброженский собор Мирожского монастыря в Пскове':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./8.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Собор Спасо-Преображенский в Переяславль-Залесском')
        btn3 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn4 = types.KeyboardButton('Новодевичий монастырь')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek5)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./8.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Собор Спасо-Преображенский в Переяславль-Залесском')
        btn3 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn4 = types.KeyboardButton('Новодевичий монастырь')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek5)

def XII_vek5(message):
    if message.text == 'Собор Спасо-Преображенский в Переяславль-Залесском':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./9.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше')
        btn2 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn3 = types.KeyboardButton('Десятинная церковь')
        btn4 = types.KeyboardButton('Успенский собор Троице-Сергиевой Лавры')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek6)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./9.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше')
        btn2 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn3 = types.KeyboardButton('Десятинная церковь')
        btn4 = types.KeyboardButton('Успенский собор Троице-Сергиевой Лавры')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek6)
        
def XII_vek6(message):
    if message.text == 'Церковь Бориса и Глеба в Кидекше':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./10.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn2 = types.KeyboardButton('Церковь Ильи Пророка в Ярославле')
        btn3 = types.KeyboardButton('Благовещенский собор Московского кремля')
        btn4 = types.KeyboardButton('Теремной дворец в Московском кремле')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek7)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./10.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn2 = types.KeyboardButton('Церковь Ильи Пророка в Ярославле')
        btn3 = types.KeyboardButton('Благовещенский собор Московского кремля')
        btn4 = types.KeyboardButton('Теремной дворец в Московском кремле')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek7)

def XII_vek7(message):
    if message.text == 'Храм Пятницы на Торгу в Чернигове':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./11.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Золотые ворота во Владимире')
        btn2 = types.KeyboardButton('Золотые ворота в Киеве')
        btn3 = types.KeyboardButton('Успенский собор во Владимире')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek8)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./11.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Золотые ворота во Владимире')
        btn2 = types.KeyboardButton('Золотые ворота в Киеве')
        btn3 = types.KeyboardButton('Успенский собор во Владимире')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek8)

def XII_vek8(message):
    if message.text == 'Золотые ворота во Владимире':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./12.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Вологде')
        btn2 = types.KeyboardButton('Троицкий собор в Троицко-Сергеевом монастыре')
        btn3 = types.KeyboardButton('Церковь Покрова Богородице на реке Нерли')
        btn4 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek9)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./12.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Вологде')
        btn2 = types.KeyboardButton('Троицкий собор в Троицко-Сергеевом монастыре')
        btn3 = types.KeyboardButton('Церковь Покрова Богородице на реке Нерли')
        btn4 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek9)
        
def XII_vek9(message):
    if message.text == 'Церковь Покрова Богородице на реке Нерли':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./13.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Боголюбово')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn4 = types.KeyboardButton('Церковь Покрова в Филях')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek10)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./13.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Боголюбово')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn4 = types.KeyboardButton('Церковь Покрова в Филях')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek10)

def XII_vek10(message):
    if message.text == 'Боголюбово':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./14.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Успенский собор во Владимире')
        btn3 = types.KeyboardButton('Архангельский собор Московского кремля')
        btn4 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше ')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek11)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./14.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Успенский собор во Владимире')
        btn3 = types.KeyboardButton('Архангельский собор Московского кремля')
        btn4 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше ')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek11)

def XII_vek11(message):
    if message.text == 'Успенский собор во Владимире':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./15.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Собор Спасо-Преображенский в Переяславль-Залесском')
        btn3 = types.KeyboardButton('Спасо-Преоброженский собор Мирожского монастыря в Пскове')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek12)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./15.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Собор Спасо-Преображенский в Переяславль-Залесском')
        btn3 = types.KeyboardButton('Спасо-Преоброженский собор Мирожского монастыря в Пскове')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XII_vek12)

def XII_vek12(message):
    if message.text =='Дмитриевский собор во Владимире':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0 
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)
    else:
        bot.reply_to(message, "Это неправильный ответ")
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)


    if message.text == 'Да, я бы с удовольствием прошёл ещё':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)










def XIII_XIV_vek2(message):
    if message.text == 'Церковь Николы на Липне':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./17.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Храм Фёдора Стратилата на Ручью')
        btn4 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek3)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./17.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Храм Фёдора Стратилата на Ручью')
        btn4 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek3)
        
def XIII_XIV_vek3(message):
    if message.text == 'Храм Фёдора Стратилата на Ручью':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./18.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn3 = types.KeyboardButton('Спасо-Преоброженский собор Мирожского монастыря в Пскове')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek4)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./18.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn3 = types.KeyboardButton('Спасо-Преоброженский собор Мирожского монастыря в Пскове')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek4)

def XIII_XIV_vek4(message):
    if message.text == 'Церковь Спаса Преображения на Ильине улице':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./19.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Смоленский кремль')
        btn3 = types.KeyboardButton('Крепость Орешек')
        btn4 = types.KeyboardButton('Крепость в Копорье')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek5)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./19.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Смоленский кремль')
        btn3 = types.KeyboardButton('Крепость Орешек')
        btn4 = types.KeyboardButton('Крепость в Копорье')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek5)

def XIII_XIV_vek5(message):
    if message.text == 'Крепость в Копорье':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./20.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Золотые ворота во Владимире')
        btn2 = types.KeyboardButton('Башни Московского Кремля')
        btn3 = types.KeyboardButton('Крепость Орешек')
        btn4 = types.KeyboardButton('Крепость в Копорье')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek6)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./20.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Золотые ворота во Владимире')
        btn2 = types.KeyboardButton('Башни Московского Кремля')
        btn3 = types.KeyboardButton('Крепость Орешек')
        btn4 = types.KeyboardButton('Крепость в Копорье')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek6)
        
def XIII_XIV_vek6(message):
    if message.text == 'Крепость Орешек':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./21.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Московский кремль при Дмитрии Донском')
        btn2 = types.KeyboardButton('Московский кремль при Иване Калите')
        btn3 = types.KeyboardButton('Благовещенский собор Московского кремля')
        btn4 = types.KeyboardButton('Теремной дворец в Московском кремле')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek7)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./21.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Московский кремль при Дмитрии Донском')
        btn2 = types.KeyboardButton('Московский кремль при Иване Калите')
        btn3 = types.KeyboardButton('Благовещенский собор Московского кремля')
        btn4 = types.KeyboardButton('Теремной дворец в Московском кремле')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek7)

def XIII_XIV_vek7(message):
    if message.text == 'Московский кремль при Иване Калите':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./22.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Московский кремль при Дмитрии Донском')
        btn2 = types.KeyboardButton('Нижегородский кремль')
        btn3 = types.KeyboardButton('Смоленский кремль')
        btn4 = types.KeyboardButton('Московский кремль при Иване Калите')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek8)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./22.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Московский кремль при Дмитрии Донском')
        btn2 = types.KeyboardButton('Нижегородский кремль')
        btn3 = types.KeyboardButton('Смоленский кремль')
        btn4 = types.KeyboardButton('Московский кремль при Иване Калите')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XIII_XIV_vek8)

def XIII_XIV_vek8(message):
    if message.text =='Московский кремль при Дмитрии Донском':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0 
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)
    else:
        bot.reply_to(message, "Это неправильный ответ")
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, 'Как на счёт ещё одного теста?', reply_markup=markup)










def XV_vek2(message):
    if message.text == 'Троицкий собор в Троицко-Сергеевом монастыре':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./24.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Соловецкий монастырь')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Нижегородский кремль')
        btn4 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek3)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./24.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Соловецкий монастырь')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Нижегородский кремль')
        btn4 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek3)

def XV_vek3(message):
    if message.text == 'Соловецкий монастырь':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./25.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn2 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn3 = types.KeyboardButton('Спасо-Преоброженский собор Мирожского монастыря в Пскове')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek4)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./25.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn2 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn3 = types.KeyboardButton('Спасо-Преоброженский собор Мирожского монастыря в Пскове')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek4)

def XV_vek4(message):
    if message.text == 'Спасский собор Андронникова монастыря':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./26.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Успенский собор во Владимире')
        btn2 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn3 = types.KeyboardButton('Успенский собор Московского Кремля')
        btn4 = types.KeyboardButton('Новодевичий монастырь')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek5)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./26.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Успенский собор во Владимире')
        btn2 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn3 = types.KeyboardButton('Успенский собор Московского Кремля')
        btn4 = types.KeyboardButton('Новодевичий монастырь')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek5)

def XV_vek5(message):
    if message.text == 'Успенский собор Московского Кремля':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./27.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Архангельский собор Московского кремля')
        btn2 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn3 = types.KeyboardButton('Собор Спасо-Преображенский в Переяславль-Залесском')
        btn4 = types.KeyboardButton('Успенский собор Троице-Сергиевой Лавры')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek6)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./27.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Архангельский собор Московского кремля')
        btn2 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn3 = types.KeyboardButton('Собор Спасо-Преображенский в Переяславль-Залесском')
        btn4 = types.KeyboardButton('Успенский собор Троице-Сергиевой Лавры')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek6)
        
def XV_vek6(message):
    if message.text == 'Архангельский собор Московского кремля':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./28.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Знамения Пресвятой Богородицы в Дубровицах')
        btn2 = types.KeyboardButton('Церковь Ильи Пророка в Ярославле')
        btn3 = types.KeyboardButton('Благовещенский собор Московского кремля')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek7)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./28.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Знамения Пресвятой Богородицы в Дубровицах')
        btn2 = types.KeyboardButton('Церковь Ильи Пророка в Ярославле')
        btn3 = types.KeyboardButton('Благовещенский собор Московского кремля')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek7)

def XV_vek7(message):
    if message.text == 'Благовещенский собор Московского кремля':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./29.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Золотые ворота во Владимире')
        btn2 = types.KeyboardButton('Колокольня Ивана Великого')
        btn3 = types.KeyboardButton('Успенский собор во Владимире')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek8)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./29.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Золотые ворота во Владимире')
        btn2 = types.KeyboardButton('Колокольня Ивана Великого')
        btn3 = types.KeyboardButton('Успенский собор во Владимире')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek8)
        
def XV_vek8(message):
    if message.text == 'Колокольня Ивана Великого':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./30.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Грановитая плата')
        btn2 = types.KeyboardButton('Троицкий собор в Троицко-Сергеевом монастыре')
        btn3 = types.KeyboardButton('Смоленский кремль')
        btn4 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek9)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./30.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Грановитая плата')
        btn2 = types.KeyboardButton('Троицкий собор в Троицко-Сергеевом монастыре')
        btn3 = types.KeyboardButton('Смоленский кремль')
        btn4 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek9)
        
def XV_vek9(message):
    if message.text == 'Грановитая плата':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./31.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek10)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./31.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek10)

def XV_vek10(message):
    if message.text == 'Церковь Ризоположения МК':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./32.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Башни Московского Кремля')
        btn2 = types.KeyboardButton('Московский кремль при Иване Калите')
        btn3 = types.KeyboardButton('Московский кремль при Дмитрии Донском')
        btn4 = types.KeyboardButton('Церковь Покрова в Филях')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek11)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./32.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Башни Московского Кремля')
        btn2 = types.KeyboardButton('Московский кремль при Иване Калите')
        btn3 = types.KeyboardButton('Московский кремль при Дмитрии Донском')
        btn4 = types.KeyboardButton('Церковь Покрова в Филях')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XV_vek11)
        
def XV_vek11(message):
    if message.text =='Башни Московского Кремля':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0 
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)
    else:
        bot.reply_to(message, "Это неправильный ответ")
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)


    if message.text == 'Да, я бы с удовольствием прошёл ещё':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)










def XVI_vek2(message):
    if message.text == 'Нижегородский кремль':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./34.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Нижегородский кремль')
        btn2 = types.KeyboardButton('Московский кремль при Иване Калите')
        btn3 = types.KeyboardButton('Смоленский кремль')
        btn4 = types.KeyboardButton('Московский кремль при Дмитрии Донском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek3)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./34.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Нижегородский кремль')
        btn2 = types.KeyboardButton('Московский кремль при Иване Калите')
        btn3 = types.KeyboardButton('Смоленский кремль')
        btn4 = types.KeyboardButton('Московский кремль при Дмитрии Донском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek3)
        
def XVI_vek3(message):
    if message.text == 'Смоленский кремль':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./35.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn3 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше ')
        btn4 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek4)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./35.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn3 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше ')
        btn4 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek4)

def XVI_vek4(message):
    if message.text == 'Церковь Вознесения в Коломенском':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./36.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn3 = types.KeyboardButton('Храм Иоанна Предтечи в селе Дьяково')
        btn4 = types.KeyboardButton('Храм Фёдора Стратилата на Ручью')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek5)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./36.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn3 = types.KeyboardButton('Храм Иоанна Предтечи в селе Дьяково')
        btn4 = types.KeyboardButton('Храм Фёдора Стратилата на Ручью')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek5)

def XVI_vek5(message):
    if message.text == 'Храм Иоанна Предтечи в селе Дьяково':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./37.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Собор Покрова на Рву (Храм Василия Блаженного)')
        btn2 = types.KeyboardButton('Башни Московского Кремля')
        btn3 = types.KeyboardButton('Успенский собор Троице-Сергиевой Лавры')
        btn4 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek6)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./37.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Собор Покрова на Рву (Храм Василия Блаженного)')
        btn2 = types.KeyboardButton('Башни Московского Кремля')
        btn3 = types.KeyboardButton('Успенский собор Троице-Сергиевой Лавры')
        btn4 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek6)
        
def XVI_vek6(message):
    if message.text == 'Собор Покрова на Рву (Храм Василия Блаженного)':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./38.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Успенский собор во Владимире')
        btn2 = types.KeyboardButton('Церковь Архангела Гавриила (Меншикова башня)')
        btn3 = types.KeyboardButton('Благовещенский собор Московского кремля')
        btn4 = types.KeyboardButton('Софийский собор в Вологде')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek7)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./38.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Успенский собор во Владимире')
        btn2 = types.KeyboardButton('Церковь Архангела Гавриила (Меншикова башня)')
        btn3 = types.KeyboardButton('Благовещенский собор Московского кремля')
        btn4 = types.KeyboardButton('Софийский собор в Вологде')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek7)

def XVI_vek7(message):
    if message.text == 'Софийский собор в Вологде':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./39.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Успенский собор Троице-Сергиевой Лавры')
        btn2 = types.KeyboardButton('Успенский собор во Владимире')
        btn3 = types.KeyboardButton('Успенский собор Московского Кремля')
        btn4 = types.KeyboardButton('Московский кремль при Иване Калите')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek8)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./39.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Успенский собор Троице-Сергиевой Лавры')
        btn2 = types.KeyboardButton('Успенский собор во Владимире')
        btn3 = types.KeyboardButton('Успенский собор Московского Кремля')
        btn4 = types.KeyboardButton('Московский кремль при Иване Калите')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek8)

def XVI_vek8(message):
    if message.text == 'Успенский собор Троице-Сергиевой Лавры':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./40.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Новодевичий монастырь')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Храм Фёдора Стратилата на Ручью')
        btn4 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek9)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./40.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Новодевичий монастырь')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Храм Фёдора Стратилата на Ручью')
        btn4 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVI_vek9)

def XVI_vek9(message):
    if message.text =='Новодевичий монастырь':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0 
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)
    else:
        bot.reply_to(message, "Это неправильный ответ")
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)


    if message.text == 'Да, я бы с удовольствием прошёл ещё':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)










def XVII_vek2(message):
    if message.text == 'Теремной дворец в Московском кремле':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.2.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Спаса Преображения на реке Нередице')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn4 = types.KeyboardButton('Верхнеспасский собор МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek3)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.2.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Спаса Преображения на реке Нередице')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn4 = types.KeyboardButton('Верхнеспасский собор МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek3)
        
def XVII_vek3(message):
    if message.text == 'Верхнеспасский собор МК':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.3.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Спасо-Преоброженский собор Мирожского монастыря в Пскове')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek4)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.3.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спасский собор Андронникова монастыря')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Спасо-Преоброженский собор Мирожского монастыря в Пскове')
        btn4 = types.KeyboardButton('Дмитриевский собор во Владимире')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek4)

def XVII_vek4(message):
    if message.text == 'Церковь Рождества Богородицы в Путинках':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.4.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Дворец Алексея Михайловича в Коломенском')
        btn2 = types.KeyboardButton('Крепость в Копорье')
        btn3 = types.KeyboardButton('Нижегородский кремль')
        btn4 = types.KeyboardButton('Новодевичий монастырь')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek5)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.4.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Дворец Алексея Михайловича в Коломенском')
        btn2 = types.KeyboardButton('Крепость в Копорье')
        btn3 = types.KeyboardButton('Нижегородский кремль')
        btn4 = types.KeyboardButton('Новодевичий монастырь')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek5)

def XVII_vek5(message):
    if message.text == 'Дворец Алексея Михайловича в Коломенском':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.5.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше ')
        btn2 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn3 = types.KeyboardButton('Церковь Знамения Пресвятой Богородицы в Дубровицах')
        btn4 = types.KeyboardButton('Успенский собор Троице-Сергиевой Лавры')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek6)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.5.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше ')
        btn2 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn3 = types.KeyboardButton('Церковь Знамения Пресвятой Богородицы в Дубровицах')
        btn4 = types.KeyboardButton('Успенский собор Троице-Сергиевой Лавры')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek6)
        
def XVII_vek6(message):
    if message.text == 'Церковь Знамения Пресвятой Богородицы в Дубровицах':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.6.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn2 = types.KeyboardButton('Церковь Ильи Пророка в Ярославле')
        btn3 = types.KeyboardButton('Храм Фёдора Стратилата на Ручью')
        btn4 = types.KeyboardButton('Церковь Покрова в Филях')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek7)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.6.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn2 = types.KeyboardButton('Церковь Ильи Пророка в Ярославле')
        btn3 = types.KeyboardButton('Храм Фёдора Стратилата на Ручью')
        btn4 = types.KeyboardButton('Церковь Покрова в Филях')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek7)

def XVII_vek7(message):
    if message.text == 'Церковь Покрова в Филях':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.7.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Сухарева башня')
        btn2 = types.KeyboardButton('Башни Московского Кремля')
        btn3 = types.KeyboardButton('Боголюбово ')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek8)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.7.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Сухарева башня')
        btn2 = types.KeyboardButton('Башни Московского Кремля')
        btn3 = types.KeyboardButton('Боголюбово ')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek8)

def XVII_vek8(message):
    if message.text == 'Сухарева башня':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.8.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Теремной дворец в Московском кремле')
        btn2 = types.KeyboardButton('Крутицкий теремок')
        btn3 = types.KeyboardButton('Церковь Покрова Богородице на реке Нерли')
        btn4 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek9)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.8.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Теремной дворец в Московском кремле')
        btn2 = types.KeyboardButton('Крутицкий теремок')
        btn3 = types.KeyboardButton('Церковь Покрова Богородице на реке Нерли')
        btn4 = types.KeyboardButton('Церковь Вознесения в Коломенском')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek9)
        
def XVII_vek9(message):
    if message.text == 'Крутицкий теремок':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.9.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Архангела Гавриила (Меншикова башня)')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn4 = types.KeyboardButton('Сухарева башня')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek10)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.9.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Архангела Гавриила (Меншикова башня)')
        btn2 = types.KeyboardButton('Церковь Рождества Богородицы в Путинках')
        btn3 = types.KeyboardButton('Церковь Спаса Преображения на Ильине улице')
        btn4 = types.KeyboardButton('Сухарева башня')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek10)

def XVII_vek10(message):
    if message.text == 'Церковь Архангела Гавриила (Меншикова башня)':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.10.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Церковь Ильи Пророка в Ярославле')
        btn3 = types.KeyboardButton('Десятинная церковь')
        btn4 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше ')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek11)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.10.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn2 = types.KeyboardButton('Церковь Ильи Пророка в Ярославле')
        btn3 = types.KeyboardButton('Десятинная церковь')
        btn4 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше ')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek11)

def XVII_vek11(message):
    if message.text == 'Церковь Ильи Пророка в Ярославле':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.11.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Знамения Пресвятой Богородицы в Дубровицах')
        btn2 = types.KeyboardButton('Собор Спасо-Преображенский в Переяславль-Залесском')
        btn3 = types.KeyboardButton('Церковь Николая Чудотворца в Хамовниках')
        btn4 = types.KeyboardButton('Церковь Николы на Липне')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek12)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.11.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Знамения Пресвятой Богородицы в Дубровицах')
        btn2 = types.KeyboardButton('Собор Спасо-Преображенский в Переяславль-Залесском')
        btn3 = types.KeyboardButton('Церковь Николая Чудотворца в Хамовниках')
        btn4 = types.KeyboardButton('Церковь Николы на Липне')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek12)

def XVII_vek12(message):
    if message.text == 'Церковь Николая Чудотворца в Хамовниках':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.12.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше ')
        btn2 = types.KeyboardButton('Троицкий собор в Троицко-Сергеевом монастыре')
        btn3 = types.KeyboardButton('Успенский собор Московского Кремля')
        btn4 = types.KeyboardButton('Храм 12 апостолов и Патриаршие палаты МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek13)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.12.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Церковь Бориса и Глеба в Кидекше ')
        btn2 = types.KeyboardButton('Троицкий собор в Троицко-Сергеевом монастыре')
        btn3 = types.KeyboardButton('Успенский собор Московского Кремля')
        btn4 = types.KeyboardButton('Храм 12 апостолов и Патриаршие палаты МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek13)

def XVII_vek13(message):
    if message.text == 'Храм 12 апостолов и Патриаршие палаты МК':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.13.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Георгиевский собор Юрьева монастыря ')
        btn2 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn3 = types.KeyboardButton('Новоиерусалимский монастырь')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek14)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.13.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Георгиевский собор Юрьева монастыря ')
        btn2 = types.KeyboardButton('Храм Пятницы на Торгу в Чернигове')
        btn3 = types.KeyboardButton('Новоиерусалимский монастырь')
        btn4 = types.KeyboardButton('Церковь Ризоположения МК')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek14)

def XVII_vek14(message):
    if message.text == 'Новоиерусалимский монастырь':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        file = open('./1.14.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Деревянное зодчество на о. Кижи')
        btn2 = types.KeyboardButton('Боголюбово ')
        btn3 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn4 = types.KeyboardButton('Собор Покрова на Рву (Храм Василия Блаженного)')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek15)

    elif message.text == 'Вернуться в начало':
        score = 0
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(message, vek)
        
    else:
        bot.reply_to(message, "Это неправильный ответ")
        file = open('./1.14.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Деревянное зодчество на о. Кижи')
        btn2 = types.KeyboardButton('Боголюбово ')
        btn3 = types.KeyboardButton('Софийский собор в Новгороде Великом')
        btn4 = types.KeyboardButton('Собор Покрова на Рву (Храм Василия Блаженного)')
        btn_back = types.KeyboardButton('Вернуться в начало')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn_back)
        bot.send_message(message.chat.id, 'Что изображено на фото?', reply_markup=markup)
        bot.register_next_step_handler(message, XVII_vek15)

def XVII_vek15(message):
    if message.text =='Деревянное зодчество на о. Кижи':
        bot.reply_to(message, "Это правильный ответ")
        global score
        score += 1
        print('score +1')
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0 
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)
    else:
        bot.reply_to(message, "Это неправильный ответ")
        if (score == 1):
            bot.send_message(message.chat.id, f'Ты дал {score} правильный ответ!')
        elif (score == 2 or score == 3 or score == 4):
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответа!') 
        else:
            bot.send_message(message.chat.id, f'Ты дал {score} правильных ответов!')
        score = 0
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Да, я бы с удовольствием прошёл ещё!', callback_data='click'))
        bot.send_message(message.chat.id, f'Как на счёт ещё одного теста?', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback)
def callback_message(callback):
    if callback.data == 'click':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('XI век')
        btn2 = types.KeyboardButton('XII век')
        btn3 = types.KeyboardButton('XIII-XIV века')
        btn5 = types.KeyboardButton('XV век')
        btn6 = types.KeyboardButton('XVI век')
        btn7 = types.KeyboardButton('XVII века')
        markup.row(btn1, btn2, btn3)
        markup.row(btn5, btn6, btn7)
        bot.send_message(callback.message.chat.id, 'Выбирай век!' , reply_markup=markup)
        bot.register_next_step_handler(callback.message, vek)


        








        
        
    
    

  

    


bot.infinity_polling()