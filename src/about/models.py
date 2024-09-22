from django.db import models

from ckeditor.fields import RichTextField


class About(models.Model):
    body = RichTextField()

    def __str__(self):
        return str(self.id)
