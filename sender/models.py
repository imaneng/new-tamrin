from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related






class Mesage(models.Model):
    title = models.CharField(max_length=100,null=True)
    note = models.TextField(null=True,blank=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name="creator",null=True)
    create_date = models.DateTimeField( auto_now_add=True, auto_now=False,null=True)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True,null=True)
    viewers = models.ManyToManyField(User, related_name="viewers",null=True)
    seen = models.BooleanField(default=False)
    


    


    


