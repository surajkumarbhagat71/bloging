from django.db import models
from django.conf import settings


# Create your models here.
class UserDetail(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    users = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    contact = models.IntegerField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Blog(models.Model):
    b_id = models.AutoField(primary_key=True)
    bloger = models.ForeignKey(UserDetail,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/',null=True,blank=True)
    blog = models.TextField()

    def __str__(self):
        return self.title


class BlogView(models.Model):
    bv_id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    ip = models.CharField(max_length=250)
    view = models.IntegerField(default=0)



class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    ip = models.TextField(max_length=200)


class Comments(models.Model):
    com_id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=500)
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    ip = models.TextField(max_length=200)


    def __str__(self):
        return self.comment

    




