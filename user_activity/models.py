from django.db import models

# Create your models here.


from django.db import models
from django.forms import ModelForm

class Upload(models.Model):
    pic = models.FileField(upload_to="images/")    
    desciption = models.CharField(max_length=120)

# FileUpload form class.
class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('pic', 'desciption')


class Permissions(models.Model):
    pass