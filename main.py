import threading

# Открываем файл для записи переписки
with open('chat_log.txt', 'w') as f:
    f.write('Чат начат\n')


# Функция обработки сообщений
def handle_message(number):
    while True:
        # Запрашиваем сообщение у пользователя
        message = input(f'Введите сообщение {number}: ')

        # Определяем поток записи: 1-ый или 2-ой
        if number % 2 == 0:
            thread_name = 'Пользователь 1'
        else:
            thread_name = 'Пользователь 2'

        # Записываем сообщение в файл
        with open('chat_log.txt', 'a') as f:
            f.write(f'{thread_name}: {message}\n')


# Создаем и запускаем потоки
thread1 = threading.Thread(target=handle_message, args=(2,))
thread1.start()

thread2 = threading.Thread(target=handle_message, args=(1,))
thread2.start()
