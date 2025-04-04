from django.db import models
from django.contrib.auth.models import User




class Tenant(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tenants')
    name = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return self.name


class BaseTenantClass(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)


class Entity(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
