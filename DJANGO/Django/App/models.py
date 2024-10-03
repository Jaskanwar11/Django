from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class AppVariety(models.Model):

    APPS = [
        ('IG', 'INSTAGRAM'),
        ('SC', 'SNAPCHAT'),
        ('WA', 'WHATSAPP'),
        ('TG', 'TELEGRAM'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'appimages/')
    date_added = models.DateTimeField(default=timezone.now)
    type =  models.CharField(max_length=2, choices=APPS)
    description = models.TextField(default='')
    pricing = models.DecimalField(max_digits=5,decimal_places=2,default=0)

    def __str__(self):
        return self.name

# One to many

class AppReview(models.Model):
    app = models.ForeignKey(AppVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    details = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.app.name}'

# Many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    app_varities = models.ManyToManyField(AppVariety, related_name='store')

    def __str__(self):
        return self.name

# One to one

class AppCertificate(models.Model):
    app = models.OneToOneField(AppVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_num = models.CharField(max_length=100)
    issued_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Certificate for {self.name.app}'