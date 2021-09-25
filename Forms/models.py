from cloudinary.uploader import destroy
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

Question_type_Choices = [('Choices','Choices'),('Multiple Choices','Multiple Choices'),('True/False','True/False'),('Date','Date'),('Short Answer','Short Answer')]


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class SF_Cloudinary_Bin_Model(models.Model):
    Public_Id = models.CharField(max_length=200)

    def delete(self, using=None, keep_parents=False):
        destroy(self.Public_Id)
        super(SF_Cloudinary_Bin_Model, self).delete()



class SF_Forms_Model(models.Model):
    Form_Id = models.BigAutoField(primary_key=True)
    Form_UID = models.TextField(null=True,blank=True)
    Form_Owner = models.ForeignKey(User,on_delete=models.CASCADE)
    Form_Name = models.CharField(max_length=50,default='Untitled')
    Created_Time = models.DateTimeField(auto_now_add=True)
    Last_Opened = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'SF_Forms'


class SF_Question_Model(models.Model):
    Question_Id = models.BigAutoField(primary_key=True)
    Form_Id = models.ForeignKey(SF_Forms_Model,on_delete=models.CASCADE)
    Question = models.TextField()
    Question_Type = models.CharField(choices=Question_type_Choices,max_length=30)
    Mark = models.IntegerField()
    Image = CloudinaryField('image')
    Image_Height = models.CharField(max_length=10)
    Image_Width = models.CharField(max_length=10)

    def delete(self, using=None, keep_parents=False):
        try:
            destroy(self.Image.public_id)
        except:
            SF_Cloudinary_Bin_Model.objects.create(Public_Id=self.Image.public_id)
        super(SF_Question_Model,self).delete()

    class Meta:
        db_table = 'SF_Question'

class SF_Options_Model(models.Model):
    Option_Id = models.BigAutoField(primary_key=True)
    Question_Id = models.ForeignKey(SF_Question_Model,on_delete=models.CASCADE)
    Option = models.CharField(max_length=100)
    Is_Correct = models.BooleanField(default=False)
    Image = CloudinaryField('image')

    def delete(self, using=None, keep_parents=False):
        try:
            destroy(self.Image.public_id)
        except:
            SF_Cloudinary_Bin_Model.objects.create(Public_Id=self.Image.public_id)
        super(SF_Options_Model,self).delete()

    class Meta:
        db_table = 'SF_Options'
