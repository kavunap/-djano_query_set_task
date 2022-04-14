from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# class City(models.Model):
#     name= models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

class Shop(models.Model):
    name= models.CharField(max_length=255)
    # city = models.ForeignKey(City,on_delete=models.CASCADE, related_name='shops')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='books',null=True)
    # variations = models.OneToManyField(Variation)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    type = models.CharField(max_length=255)
    shop= models.ForeignKey(Shop,on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return self.name

class Address(models.Model):
    line1=models.CharField(max_length=255)
    line2=models.CharField(max_length=255)
    line3=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    prefecture=models.CharField(max_length=255)
    postalcode=models.CharField(max_length=255)

    # addressable = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,null=True)
    addressable_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'addressable_id')

    def __str__(self):
        return self.line1


class Order(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE, related_name='orders')
    # name = models.CharField(max_length=255)
    foods = models.ManyToManyField(
        Food
        # through='OrderFood',
        # through_fields=('group', 'person'),
    )

    address= models.ForeignKey(Address,on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"mande by {self.customer.name}"

# class OrderFood(models.Model):
#     food= models.ForeignKey(Food,on_delete=models.CASCADE)
#     order= models.ForeignKey(Order,on_delete=models.CASCADE)