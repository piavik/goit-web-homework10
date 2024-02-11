from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    born_date = models.DateField(auto_now_add=False, null=False)
    born_location = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return f"{self.fullname}"
