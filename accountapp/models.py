from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False) # null은 없어도 되는 정보인지 설정해주는 것임 => 있어야 되니까 False



