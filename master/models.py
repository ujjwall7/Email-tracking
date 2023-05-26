from django.db import models


class SentEmail(models.Model):
    subject = models.CharField(max_length=255)
    to_email = models.EmailField()
    message = models.TextField()
    is_opened = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)