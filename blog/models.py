from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title= models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE,)
    body = models.TextField()
    pub_date =  models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    stars = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    def get_stars(self):
        string = ""
        for i in stars:
            string += i
        return string
    
    # def pub_date_short(self):
    #     return self.pub_date.strftime('%b %e %Y')