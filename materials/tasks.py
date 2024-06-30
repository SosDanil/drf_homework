import datetime

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_mail_to_owner(all_email_list):
    for email in all_email_list:
        send_mail(
            subject='Обновление курса',
            message='Ваш курс был обновлен',
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
        )
        print(f'Письмо было отправлено на адрес {email}')


def check_last_login():
    print('Делаю проверку пользователей на последний вход')
    users = User.objects.all()
    for user in users:
        now = datetime.datetime.now(tz=settings.TIME_ZONE)
        delta = datetime.timedelta(days=30)
        if now - user.last_login > delta:
            user.is_active = False
            user.save()
            print(f'Пользователь {user.email} был заблокирован')
        else:
            print(f'Пользователь {user.email} входил недавно')
