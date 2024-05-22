from django.db import models

from common.models import nb, ABSModel


class User(models.Model, ABSModel):
    first_name = models.CharField(**nb)
    last_name = models.CharField(**nb)
    middle_name = models.CharField(**nb)
    username = models.CharField(unique=True, db_index=True)
    password = models.TextField()