from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Пользовтель активирован да=1/нет=0')
    send_massages = models.BooleanField(default=True, verbose_name='Слать оповещение о новых комментариях')

    class Meta(AbstractUser.Meta):
        pass
