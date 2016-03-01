from django.db import models

class UploadFile(models.Model):
    archivo = models.FileField(upload_to='/home/lucho/workspace/cuenta/subida')
