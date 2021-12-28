from django.db import models
from django.contrib.auth.models import User








class Mesage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="senderr")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    date_message = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Message')
    seen = models.BooleanField(default=False)


    def __str__(self) -> str:
        return  'Message from ' + self.sender.first_name + ' for ' + self.receiver.first_name


    


