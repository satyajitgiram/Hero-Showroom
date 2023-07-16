from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Bike(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    model_year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    make = models.CharField(max_length=50)
    engine_power = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=100)
    engine_power_torque = models.CharField(max_length=50)
    top_speed = models.PositiveIntegerField()
    fuel_economy = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='bikes/')
    mileage = models.DecimalField(max_digits=5, decimal_places=2)
    engine_displacement = models.DecimalField(max_digits=6, decimal_places=2)
    payload_capacity = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    additional_options_features = models.TextField()
    description = models.TextField()
    colors = models.ManyToManyField('Color')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class TestRide(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    vehicle = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.IntegerField(max_length=15)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name



class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    text = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    