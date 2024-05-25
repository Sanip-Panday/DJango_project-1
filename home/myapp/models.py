from django.db import models

# Create your models here.

#Index
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

#Contact
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.subject

# About us models
class TitleAbout(models.Model):
    title=models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.title


class AboutBlog(models.Model):
    blog_title=models.ForeignKey(TitleAbout,on_delete=models.CASCADE)
    desc=models.TextField()

    def __str__(self):
        return f"{self.blog_title}"


class TeamMemberName(models.Model):
    name=models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name


class OurTeamName(models.Model):
    member=models.ForeignKey(TeamMemberName,on_delete=models.CASCADE)
    designation=models.CharField(max_length=200)
    desc=models.TextField()

    def __str__(self):
        return f"{self.designation}"
    

# Contact us models
class personal_info(models.Model):

    name=models.CharField(max_length=150)
    address=models.CharField(max_length=200)
    roles=models.CharField(max_length=150)
    desc = models.TextField()
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} + {self.address} + {self.roles}"
    
    