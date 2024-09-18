from django.db import models


# Many To Many (Product and Promotion)


class Promotion(models.Model):

    description = models.CharField(max_length=255)
    discount = models.FloatField()
    

# collection model

class Collection(models.Model):

    title = models.CharField(max_length=255)

    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')
    




# Product Model 

class Product(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField() 
    description = models.TextField()

    # 9999.99
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

    inventory=models.IntegerField()

    last_update= models.DateTimeField(auto_now=True)

    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)

    promotions = models.ManyToManyField(Promotion)
    




# Customer Model 

class Customer(models.Model):

    MEMBERSHIP_BRONZE ='B'

    MEMBERSHIP_SILVER ='B'

    MEMBERSHIP_GOLD ='G'
    

    MEMBERSHIP_CHOICES = [

        (MEMBERSHIP_BRONZE,'Bronze'),

        (MEMBERSHIP_SILVER,'Silver'),

        (MEMBERSHIP_GOLD,'Gold'),

    ]
        

    first_name= models.CharField(max_length=255)

    last_name= models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=255)

    birth_date = models.DateField(null=True)

    membership= models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)
    
    class Meta:
        indexes=[
            models.Index(fields=['last_name',])
        ]
    
    
    

# Order Model 


class Order(models.Model):

    PAYMENT_STATUS_PENDING ='P'

    PAYMENT_STATUS_COMPLETE ='C'

    PAYMENT_STATUS_FAILED ='F'
    

    PAYMENT_STATUS_CHOICES = [

        (PAYMENT_STATUS_PENDING,'Pending'),

        (PAYMENT_STATUS_COMPLETE,'Complete'),

        (PAYMENT_STATUS_FAILED,'Fail'),

    ]


    placed_at = models.DateTimeField(auto_now_add=True)
    

    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)
    

    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

    # PROTECT -: DELETE THE CUSTOMER NOT THE ORDER 
    
    
    
   
   
   


class OrderItem(models.Model):

    order = models.ForeignKey(Order,on_delete=models.PROTECT)

    product = models.ForeignKey(Product,on_delete=models.PROTECT) 

    quantity = models.PositiveIntegerField()

    unit_price=models.DecimalField(max_digits=6,decimal_places=2)




# Address Model (Parent came before child)

# if you not given pk then it is one to many 

class Address(models.Model):

    city = models.CharField(max_length=255)

    street = models.CharField(max_length=255)

    # Each customer has one address

    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    
    

    # # Each customer has many address

    # customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    


# CArt model 

class Cart(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    
    


class CartItem(models.Model):

    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)

    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    quantity = models.PositiveSmallIntegerField()



 


