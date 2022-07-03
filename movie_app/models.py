from django.db import models



class Director(models.Model):
    name = models.CharField(max_length=12)

    @property
    def count_movies(self):
        return self.movies.all().count()

    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(default=0)
    directory1 = models.ForeignKey(Director, on_delete=models.CASCADE,
                         related_name='movies', null=True, blank=True)
    def __str__(self):
        return self.title

    @property
    def rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0
        average = 0
        for i in reviews:
            average += i.stars
        return average / reviews.count()




STAR_CHOICES = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *'),
)

class Review(models.Model):
    author = models.CharField(max_length=100, default='', blank=True)
    text = models.TextField(null=True)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='reviews')
    stars = models.IntegerField(default=1, choices=STAR_CHOICES)

    def __str__(self):
        return self.text


