from django.db import models

nb = {'null': True, 'blank': True}

class ABSModel:
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(auto_now=True)