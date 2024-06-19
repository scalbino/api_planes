from django.db import models

# Create your models here.
class Token(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    token = models.CharField(max_length=500, unique=True, null=False)
    unique_Id = models.CharField(max_length=500, unique=True, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token

