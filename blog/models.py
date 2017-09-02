from django.contrib.auth.models import User
from django.db import models

SHORT_TEXT = 2;

class Arcticle(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return  self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT:
            return self.text[:SHORT_TEXT]
        else:
            return self.text

