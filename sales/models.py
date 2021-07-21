from django.db import models

from purchase.models import Dealer_Details,Product,Category,Company

class Sale_Type(models.Model):
    sale_type = models.CharField(max_length=20)

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    
    def __str__(self):
            return '{}'.format(self.customer_name,self.customer_id)
    
class Daily_Sale(models.Model):
    bill_no = models.AutoField(primary_key=True)
    billing_date = models.DateField(auto_now=True, auto_now_add=False)
    type_of_sale = models.ForeignKey(Sale_Type, on_delete=models.CASCADE)
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    Product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    
    def __str__(self):
            return '{}'.format(self.bill_no)
    
    
    

