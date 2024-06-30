from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


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
