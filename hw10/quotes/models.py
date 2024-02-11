from django.db import models
# from django.contrib.auth.models import User       # for authentication
from authors.models import Author

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

class Quote(models.Model):
    tags = models.ManyToManyField(Tag)
    quote = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)

    def __str__(self):
         return f'{self.quote[:20]}... - {self.author}'

