from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    company = models.BooleanField(default=False, verbose_name='Company',
                                  help_text='Check this box if you are a company.')
    groups = models.ManyToManyField(Group, related_name='user_set_custom',
                                    blank=True, verbose_name='User Groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_set_custom',
                                              blank=True, verbose_name='User Permissions')
