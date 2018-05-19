from __future__ import unicode_literals

from django.db import models
import time
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class CommonFields(models.Model):
    
    created_by = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    recVersion = models.IntegerField(default=1)

    class Meta:
        abstract = True

class Blogs(models.Model):

    blog_body=models.CharField(max_length=2000)
    blog_user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_heading = models.CharField(max_length=200)
    blog_images = models.FileField(upload_to='posts/blogs/%Y/%m/%d')
    blog_date=models.DateTimeField(datetime.datetime.now())

    def __str__(self):
        return self.name



class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    post = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    comment = models.CharField(max_length=240)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment



# class LikeIt(models.Model):

#     user_like=models.ForeignKey(Blogs,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     liked_date= models.DateTimeField(default=timezone.now)

#     def __str__(self):

#         return self.user.email

class Share(models.Model):

    share_user=models.ForeignKey(User,on_delete=models.CASCADE)
    share_blog=models.ForeignKey(Blogs,on_delete=models.CASCADE,blank=True,null=True)
    share_comment=models.CharField(max_length=240,blank=True,null=True)
    share_date= models.DateTimeField(default=timezone.now)

    def __str__(self):

        return self.share_user.username