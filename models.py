from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#custom model
class User(AbstractUser) :
    class Role(models.TextChoices):
        ADMIN="ADMIN", 'Admin'
        CUSTOMER="CUSTOMER",'Customer'
        MANAGER="MANAGER", 'Manager'
    Base_role= Role.MANAGER
    role=models.CharField(max_length=50,choices=Role.choices)    

    def save(self,*args,**kwargs) :
        if not self.pk :
            self.role=self.Base_role
            return super().save(*args,**kwargs)
        
#manager class
class CustomerManager(BaseUserManager) :
     def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTOMER)

#proxy calss
class Customer(User) :
    Base_role=User.Role.CUSTOMER
    customer = CustomerManager()
    class Meta : 
        proxy=True
    def welcome(slef) :
        return "Only for customer"
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Customer_id = models.IntegerField(null=True, blank=True)

@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)

class managerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.MANAGER)


class Manager(User):

    base_role = User.Role.MANAGER

    manager= managerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for manager"


class managerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manager_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Manager)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "MANAGER":
        managerProfile.objects.create(user=instance)
        

class product1(models.Model):
    username = models.CharField(max_length=122)
    taste = models.IntegerField()
    freshness = models.IntegerField()
    h_cnt = models.IntegerField()
    flv = models.IntegerField()
    delivery = models.IntegerField()
    pname = models.CharField(max_length=122,default="orange")
    
    def __str__(self):
        return self.username

class sales(models.Model):
    pname2 = models.CharField(max_length=122,default="orange")
    month = models.CharField(max_length=122)
    year = models.IntegerField()
    total_sal=models.IntegerField()
    total_pro = models.IntegerField()
    cst = models.IntegerField()
    sel = models.IntegerField()
    





