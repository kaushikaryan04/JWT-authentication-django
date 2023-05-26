from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField



#use a set to see each user's liked photos if user have liked a particular photo do not let him like again
# user
class User(AbstractUser):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_IN_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    phoneNumber = models.CharField(max_length=12 , blank = True ,null = True , unique = True )
    gender = models.CharField(choices=GENDER_IN_CHOICES , max_length=6 , null = True , blank = True)

#  posts
class Post(models.Model):
    author = models.ForeignKey(User , on_delete= models.CASCADE)
    caption = models.CharField(max_length= 200)
    image = CloudinaryField('image')
    likes= models.IntegerField(default=0)
    
    def likePost(self):
        self.likes+=1
        self.save()

class Like(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user'  , 'post')
        
        

# for future use https://www.section.io/engineering-education/uploading-images-to-cloudinary-from-django-application/#setting-up-cloudinary