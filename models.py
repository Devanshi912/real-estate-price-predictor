from django.db import models
class Property(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    price = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField(default=3)
    area = models.IntegerField(help_text="Area in square feet")
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    property_type = models.CharField(max_length=100, default="Apartment")

    year_built = models.IntegerField(null=True, blank=True)
    parking = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    property_type = models.CharField(max_length=100)



    def __str__(self):
        return f"{self.title} - {self.location}"