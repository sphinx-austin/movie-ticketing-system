from django.db import models

# Create your models here.
class WatchDay(models.Model):
    date =  models.DateField()

    def __str__(self) -> str:
        return f"day-of-movies-{self.id}"

class Movie(models.Model):
    title=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    description=models.TextField()
    duration=models.CharField(max_length=50, default="1hour 30mins")
    release_date=models.DateField()
    rating=models.IntegerField(default=0)
    casts=models.CharField(max_length=500)
    view_price=models.DecimalField(max_digits=7, decimal_places=2)
    movies_art=models.ImageField(upload_to="thumbnail")
    view_date=models.ManyToManyField(WatchDay)

    def __str__(self) -> str:
        return self.title