# from keyboard import sender
from interface import *


for event in core.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = str(event.user_id)
        msg = event.text.lower()
        # sender(user_id, msg.lower())
        if request == 'п':
            creating_database()
            core.write_msg(user_id, f'Привет, {core.name(user_id)}')
            core.find_user(user_id)
            core.write_msg(event.user_id, f'Найдено несколько совпадений, нажмите "С" для перехода к следующему человеку')
            core.find_persons(user_id, offset)

        elif request == 'с':
            for i in line:
                offset += 1
                core.find_persons(user_id, offset)
                break

        else:
            core.write_msg(event.user_id, 'Неверная команда. Введите "П" для поиска или "С" для перехода к следующему человеку')
