from django.db import models

class Status(models.Model):
    Name = models.CharField(max_length=50,null=True, help_text="Enter name")
    Shop_Name = models.CharField(max_length=100,null=True, help_text="Enter shop_name")
    Status = models.CharField(max_length=150,null=True, help_text="Enter status")
    Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name