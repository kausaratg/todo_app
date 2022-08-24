from django.db import models
from django.urls import reverse

# Create your models here.
class TodoApp(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title