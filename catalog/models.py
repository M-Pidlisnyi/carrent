from django.db import close_old_connections, models
from django.db.models.deletion import RESTRICT
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.functions.comparison import Coalesce
from django.urls import reverse
import uuid # required for specific instance of a car

# Create your models here.

class BodyStyle(models.Model):
    """model representing car body style"""
    #fields
    name = CharField(max_length=50,verbose_name="Car body style",help_text="e.g. Sedan, Carbriolet, etc.")
    #methods
    def __str__(self) -> str:
        """string based representation of an object"""
        return super().__str__()

class Car(models.Model):
    """model representing car in general"""
    #fields
    carModel = CharField(max_length=50)
    brand = ForeignKey("Brand",on_delete=models.SET_NULL, null=True)
    color = CharField(max_length=20)
    bodyStyle = ManyToManyField(BodyStyle)

    #methods
    def __str__(self) -> str:
        return super().__str__()
    #possible implementation of __str__() if the one above is buggy
    # def __str__(self):
    #     return self.carModel
    def get_absolute_url(self):
        """Returns the url to access a detail record for this car."""
        return reverse("car-detail", args=[str(self.id)])

class CarInstance(models.Model):
    """model representing one particular car that someone may rent
       it contains, among others, information about renter, date of return, unique reg. plate, etc."""
    #fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="unique car ID")
    car = ForeignKey(Car, on_delete=RESTRICT, null=True)
    due_back = models.DateField(null=True, blank=True)
    year = models.IntegerField()
    plate = CharField(max_length=8, 
                      verbose_name="Vehicle registration plate",
                      unique=True,
                      help_text='<a href="https://en.wikipedia.org/wiki/Vehicle_registration_plate">8 characters</a> in form AB1234BC')

    RENT_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On rent'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = CharField(
        max_length=1,
        choices=RENT_STATUS,
        blank=True,
        default='m',
        help_text="Car availability"
    )

    class Meta:
        ordering = ['due_back']
    
    #methods
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.car.carModel})'

class Brand(models.Model):
    """model representing brand car manufacturers go by"""
    name = CharField(max_length=50)
    companyOwner = CharField(max_length=100, null=True, blank=True, 
                            help_text="empty if the same as brand name")
    creationDate = DateField(null=True, blank=True,
                             help_text="the date when the brand was created")

    class Meta:
        ordering = ["name", "-creationDate"]
    
    def get_absolute_url(self):
        """Returns the url to access a particular brand instance."""
        return reverse('brand-detail', args=[str(self.id)])
    
    def __str__(self) -> str:
        return super().__str__()
    