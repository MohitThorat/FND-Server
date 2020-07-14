from django.db import models

# Create your models here.

class FakeText(models.Model):
    
    fake_text = models.TextField()
    feedback_one = models.CharField(max_length=200, blank=True, default='',null = True)
    feedback_two = models.CharField(max_length=200, blank=True, default='', null = True)
    created = models.DateTimeField(auto_now_add=True)

