from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    body = models.CharField(max_length=2000)
    status = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
