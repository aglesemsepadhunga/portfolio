from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/',default='media/images/gsoc.jpeg',blank=True)

    def __str__(self): return self.title
    def summary(self): return self.body[:100]+'...'
    def pub_date_pretty(self): return self.pub_date.strftime('%b %e %Y')
