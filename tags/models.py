from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.







class Tag(models.Model):
    label = models.CharField(max_length=255)
    
    
class TaggedItem(models.Model):
    # what tag to applied to what object
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    
    # type(product , video, article ) -> (WE find table by using type)
    # ID (We find record by id)
    
   
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
