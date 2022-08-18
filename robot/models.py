from django.db import models


class Robot_Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Robot_Quotes(models.Model):
    text = models.TextField(unique=True)
    authors = models.ForeignKey(Robot_Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.authors
