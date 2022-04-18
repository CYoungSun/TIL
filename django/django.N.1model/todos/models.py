from django.db import models
from django.conf import settings
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title