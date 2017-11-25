from django.db.models import Avg
from django.db import models

# Create your models here.

class Reviews(models.Model):
    """A topic the user is learning about"""
    review = models.TextField(max_length=200)
    rating=models.IntegerField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_reviews(self):
        average =  Reviews.objects.all().aggregate(Avg('rating'))
        allreviews=Reviews.objects.all().order_by('date_added')

        return {'average':average,'reviews':allreviews}

    def save_reviews(self,rating,review):
        save=Reviews(rating=rating,review=review)
        save.save()
        if self.pk == None:
            return 'Your Review Has been Save'
        else:
            return 'Your Review Could not be Saved'



