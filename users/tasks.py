from datetime import datetime
import pytz
from celery import shared_task
from dateutil.relativedelta import relativedelta

from users.models import User


@shared_task
def check_last_login():
    print('Делаю проверку пользователей на последний вход')

    now = datetime.now(pytz.utc)
    month_ago = now - relativedelta(months=1)
    user = User.objects.filter(is_active=True, last_login__lte=month_ago)
    user.update(is_active=False)

    # users = User.objects.filter(is_active=True)
    # for user in users:
    #     now = datetime.datetime.now()
    #     delta = datetime.timedelta(days=30)
    #     if now - user.last_login > delta:
    #         user.is_active = False
    #         user.save()
    #         print(f'Пользователь {user.email} был заблокирован')
    #     else:
    #         print(f'Пользователь {user.email} входил недавно')
