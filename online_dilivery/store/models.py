from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

class Product(models.Model):
    CATEGORY = (
        ('Телефон','Телефон'),
        ('Компьютер', 'Компьютер'),
        ('Видеокарта', 'Видеокарта'),
        ('Жесткий диск','Жесткий диск'),
    )
    name = models.CharField(max_length=50,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=50,null=True,choices=CATEGORY)
    description = models.CharField(max_length=50,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tag = models.ManyToManyField(Tag,null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    full_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    telephone = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.full_name

class Order(models.Model):

    STATUS = (
        ('Pending','Pending'),
        ('Delivered', 'Delivered'),
        ('Not Delivered', 'Not Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.product.name

