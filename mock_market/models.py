from django.db import models

class Vendor(models.Model):
  vendor_name = models.CharField(max_length=100, null=True)
  first_name = models.CharField(max_length=100, null=True)
  last_name = models.CharField(max_length=100, null=True)
  email = models.CharField(max_length=100, null=True)
  password = models.CharField(max_length=55, null=True)

  def __str__(self):
    return self.vendor_name

class Item(models.Model):
  item_name = models.CharField(max_length=50)
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=False)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  size = models.IntegerField(null=True)
  quantity = models.IntegerField(default=1)
  availability = models.BooleanField(default=False)
  description = models.CharField(max_length=50)
  image = models.ImageField(upload_to='files/images', null=True)

  def __str__(self):
    return self.item_name