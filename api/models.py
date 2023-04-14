from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email,name,tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email,name,tc, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length=200)
    tc=models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    
class Electric_Product(models.Model):
    mobile=models.CharField(max_length=23)
    tv=models.CharField(max_length=23)
    fan=models.CharField(max_length=23)
    
    def __str__(self):
        return self.mobile
    class Meta():
        db_table='ele_tbl'
        
        
class Home_Kitchen_Product(models.Model):
    name=models.CharField(max_length=23)
    def __str__(self):
        return self.name
    class Meta():
        db_table='kit_product'
    
class Role(models.Model):
    role_name=models.CharField(max_length=100)
    assigned_devices=models.ManyToManyField(Electric_Product,blank=True)
    created_role_date=models.DateTimeField(default=timezone.now)
    updated_role_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.role_name
    class Meta():
        db_table='role_tbl'    
