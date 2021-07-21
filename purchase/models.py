from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    
    def __str__(self):
            return '{}'.format(self.company_name)
    
    
class Category(models.Model):
    code = models.AutoField(primary_key=True)
    catagory = models.CharField(max_length=100)
    
    def __str__(self):
            return '{}'.format(self.catagory)
    
    

class Product(models.Model):
    item_code = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_rate = models.BigIntegerField()
    mrp_rate = models.BigIntegerField()
    wholesale_rate = models.BigIntegerField()
    
    def __str__(self):
            return '{}'.format(self.item)
        
    class Meta:  
        db_table = "Product"
    
    
    
class Dealer_Details(models.Model):
    dealer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    product_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    
    def __str__(self):
            return 'Dealer:{}'.format(self.name)
    
    


    