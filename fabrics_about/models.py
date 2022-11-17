from django.db import models
from ckeditor.fields import RichTextField


# Kompaniya haqida malumotlar modeli
class About(models.Model):
    description = RichTextField(verbose_name="Tavsif")
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Kompaniya malumoti"
