from email.policy import default
from django.db import models

class ReviewChoice(models.TextChoices):
    MW = 'Must Watch'
    SW = 'Should Watch'
    AW = 'Avoid Watch'
    NO = 'No Opinion'
    
class Review(models.Model):
    
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50, choices=ReviewChoice.choices, default=ReviewChoice.NO)
    
    accounts = models.ForeignKey('accounts.Account', on_delete = models.CASCADE, related_name = 'account_reviews')
    movies = models.ForeignKey('movies.Movie', on_delete = models.CASCADE, related_name = 'movie_reviews')
    