import shutil
from rest_framework import serializers
from .models import *

class FileSerializer(serializers.Serializer):
    files=serializers.ListField(
        child=serializers.FileField(max_length=100000,allow_empty_file=False,use_url=False)
        
    )
    
    def zip_File(self,folder):
        shutil.make_archive(f'media/{folder}', 'zip',f'media/{folder}' )
    
    
    def create(self,valide_data):
        folder=Folder.objects.create()
        files=valide_data.pop('files')
         
         
         
        files_objs=[]
        for filee in files:
            files_obj=file.objects.create(folder=folder,file=filee)
            files_objs.append(files_obj)
            
            self.zip_File(folder.uid)
            print(folder.uid)
        # print(uid)
        return{'files':{},'folder':{},'name':{}}