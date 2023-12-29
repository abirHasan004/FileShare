import os
import uuid
from django.db import models

# Create your models here.


class Folder(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    create_at=models.DateField(auto_now=True)
     
    
    
    
def get_upload_data(instance,filename):
    return os.path.join(str(instance.folder.uid),filename)

class file(models.Model):
     folder=models.ForeignKey(Folder,on_delete=models.CASCADE,null=True)
     file=models.FileField(upload_to=get_upload_data)
     create_at=models.DateField(auto_now=True)