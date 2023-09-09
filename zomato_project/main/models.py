from django.db import models



# Create your models here.
class Category(models.Model):
    slug=models.CharField(max_length=100,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to="images",null=False,blank=False) 
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")  
    
    
    def __str__(self):
        return self.name
    
class Foods(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=100,null=False,blank=False)
    name=models.CharField(max_length=100,null=False,blank=False)
    food_image=models.ImageField(upload_to="images",null=False,blank=False) 
    quantity=models.IntegerField(null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    
    
    def __str__(self):
        return self.name
        
