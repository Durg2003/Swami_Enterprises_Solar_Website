from django.db import models
class Product(models.Model):
    CATEGORY_CHOICES = [('panel','Solar Panels'),('inverter','Inverters'),('battery','Solar Batteries'),('system','Complete Solar Systems'),('accessory','Accessories')]
    name = models.CharField(max_length=140)
    brand = models.CharField(max_length=100, blank=True, help_text='Enter only a verified brand / supplier')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='panel')
    capacity = models.CharField(max_length=80, blank=True, help_text='Example: 550 W or 5 kW')
    description = models.TextField(blank=True)
    efficiency = models.CharField(max_length=80, blank=True)
    warranty = models.CharField(max_length=120, blank=True)
    price_from = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    datasheet_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.brand} {self.name}'.strip()
class Enquiry(models.Model):
    PROPERTY_CHOICES = [('home','Residential'),('business','Commercial'),('industrial','Industrial'),('other','Other')]
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    property_type = models.CharField(max_length=20, choices=PROPERTY_CHOICES, default='home')
    monthly_bill = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('new','New'),('contacted','Contacted'),('quoted','Quote sent'),('closed','Closed')], default='new')
    def __str__(self): return f'{self.name} — {self.phone}'
