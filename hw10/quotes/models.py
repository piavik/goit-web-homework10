from django.db import models
# from django.contrib.auth.models import User       # for authentication

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"
        
class Author(models.Model):
    fullname = models.CharField(help_text="Full Name", max_length=50, null=False)
    born_date = models.DateField(help_text="Date of birth", auto_now_add=False, null=False)
    born_location = models.CharField(help_text="Birth location", max_length=100, null=False)
    description = models.TextField(help_text="Description", null=False)

    def __str__(self):
        return f"{self.fullname}"

class Quote(models.Model):
    tags = models.ManyToManyField(Tag)
    quote = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)

    def __str__(self):
         return f'{self.quote[:20]}... - {self.author}'

