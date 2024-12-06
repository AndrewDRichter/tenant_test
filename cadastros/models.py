from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=200)

class BaseModel(models.Model):
    ...
