from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summery(self):
        if len(self.body) > 150:
            return self.body[:150] + "...."
        else:
            return self.body

