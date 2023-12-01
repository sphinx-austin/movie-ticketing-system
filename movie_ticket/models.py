from django.db import models

# Create your models here.
class WatchDay(models.Model):
    date =  models.DateField()

    def __str__(self) -> str:
        return f"day-of-movies-{self.id}"
