def send_email(massage, recipient, sender = 'university.help@gmail.com'):
    if not all(['@' in recipient, '@' in sender, recipient.endswith('.com') or recipient.endswith('.net') or
                recipient.endswith('.ru'), sender.endswith('.com') or sender.endswith('.net') or
                sender.endswith('.ru')]):
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ', sender, 'на адрес ', recipient, '.')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, 'на адрес ', recipient, '.')

send_email('Первое письмо', 'boom@mail.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')