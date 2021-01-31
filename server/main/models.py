from djongo import models
# from djongo import models

# Create your models here.
class Demo(models.Model):
    # _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=256)
