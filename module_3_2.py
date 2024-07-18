

def send_email(message, recipient, sender="university.help@gmail.com"):
    if check_email(recipient) and check_email(sender):
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print("Письмо успешно отправлено с адреса {} на адрес {}.".format(sender, recipient))
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {} на адрес {}.".format(sender, recipient))
    else:
        print("Невозможно отправить письмо с адреса {} на адрес {}".format(sender, recipient))
            
def check_email(email):
    message_end = email.split("@")[1].split(".")[1]
    if "@" in email and message_end in ["com", "ru", "net"]:
        return True
    return False

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
