from django.db import models

class Data(models.Model):
    Subjects = models.CharField(max_length=10)
    Entry_type = models.CharField(max_length=10)
    url = models.CharField(max_length=100)
    desc = models.CharField(max_length=150)
    importance = models.IntegerField(default=2)
    status = models.BooleanField(default=False)

class Connections(models.Model):
    full_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=70)
    title = models.CharField(max_length=40)
    desc = models.CharField(max_length=140)
    field = models.CharField(max_length=40)


class NetworkEvents(models.Model):
    event_type = models.CharField(max_length=10)
    website_name = models.CharField(max_length=50)
    website_url = models.CharField(max_length=140)
    importance = models.IntegerField(default=2)


    