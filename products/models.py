from django.db import models
from django.db.models import Q

CATEGORY = (
    ('N','Without Chillie'),
    ('H',' Hot Chillie'),
    ('M','Mild Chillie'),
    ('SP','Siri ya Pilau'),
    ('SM','Siri ya Mchuzi'),
    ('SC','Siri ya Chai')
)


SIZES = (
    ('10g','10g'),
    ('15g','15g'),
    ('25g','25g'),
    ('35g','35g'),
)

class Product(models.Model):
   
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='images/')
    product_size = models.CharField(max_length=50,choices=SIZES)
    product_qyt = models.PositiveIntegerField()
    product_price = models.FloatField()
    product_category = models.CharField(max_length=50,choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True)

    def save_product(self):
        self.save()

  
    @classmethod
    def update_supplier(cls, id, new_name):
        cls.objects.filter(pk=id).update(p_name=new_name)
        new_name_object = cls.objects.get(p_name=new_name)

        new_name = new_name_object.name
        return new_name


    # @classmethod
    # def search(cls,category):
    #     return cls.objects.filter(Q(product_name__contains='N') & Q(product_name__contains='H') & Q(product_name__contains='M') &
    #     Q(product_name__contains='S'))


    def __str__(self):
        return f'{self.product_name}'

    class Meta:

        ordering = ['-date']

