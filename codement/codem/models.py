from django.db import models

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=70, default="")
    message = models.TextField(max_length=700,default="")

    def __str__(self):
        return self.name


class Hackathon(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    by = models.CharField(max_length=100)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    link = models.URLField(max_length=200, default="")

    def __str__(self):
        return self.name


