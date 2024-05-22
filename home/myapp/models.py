from django.db import models




# Create your models here.
class SliderItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='slider_images/')
    url = models.URLField()

    def __str__(self):
        return self.title
        
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='assets/img/')
    caption = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.caption


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.subject

# About us models
class Title_about(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title
    


class About_Blog(models.Model):
    blog_title=models.ForeignKey(Title_about,on_delete=models.CASCADE)
    desc=models.TextField()

    def __str__(self):
        return f"{self.blog_title}"
    
