from django.db import models
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)

    def __str__(self):
        return self.name + ' ' +  self.surname


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    start_address = models.CharField(max_length=100)
    final_address = models.CharField(max_length=100)
    driver_id = models.ForeignKey('Driver', on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client, related_name='order')
    km = models.FloatField()

class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    license_number = models.CharField(max_length=45)
    rating = models.FloatField()

    def __str__(self):
        return self.name + ' ' + self.surname
