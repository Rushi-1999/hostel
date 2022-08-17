from django.db import models

# Create your models here.
class Hostel(models.Model) :
    name = models.CharField(max_length = 200)
    add = models.CharField(max_length = 200)

    class Meta:
        db_table = "hostels"

    # def __str__(self) :
    #     return self.__dict__

class Tenant(models.Model) :
    name = models.CharField(max_length = 200)
    room_no = models.IntegerField()
    host = models.ForeignKey(Hostel, on_delete = models.CASCADE, related_name = "tent")

    class Meta:
        db_table = "Tenants"

    # def __str__(self) :
    #     return self.__dict__