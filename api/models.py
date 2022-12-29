from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    created_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    like=models.ManyToManyField(User,related_name="like")

    @property
    def post_comment(self):
        qs=self.comment_set.all()
       
        
        return qs


    def __str__(self):
        return self.title


class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.answer

    @property
    def like(self):
        return self.upvote.all().count()

# Create your models here.
