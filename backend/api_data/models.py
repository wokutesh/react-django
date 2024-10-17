from django.db import models
from django.utils import timezone
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from .token import account_activation_token
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,Permission,PermissionsMixin,Group

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not name:
            raise ValueError('The Name field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)  # Ensure 'name' is passed
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,name,password):
        user =self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,

        )

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    name= models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField(unique=True,blank=True)
    is_vendor=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.now)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
    
    objects = CustomUserManager()
    


    groups = models.ManyToManyField(
        Group,
        related_name='core_user_set',
        blank=True,
        help_text='the group belongs to this user. A user will get all permissions drantent to each of thier groups',
        verbose_name='group',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='core_user_permission',
        blank=True,
        help_text='Specific permission for this user',
        verbose_name='user permission'
    )
    
    def send_activation_email(self, request):
        uid = urlsafe_base64_encode(force_bytes(self.pk))
        token = account_activation_token.make_token(self)

        activation_link = f'{request.scheme}://{request.get_host()}/api/activate/{uid}/{token}/'

        mail_subject = 'Activate your account'
        message = f'Hi {self.name},\n\nPlease click the link below to activate your account:\n{activation_link}\n\nThank you!'
        send_mail(mail_subject, message, 'wokumateshome13@gmail.com', [self.email])
    def __str__(self):
        return self.email

    def email_user(self,subject,message,from_email =None,**kwargs):
        email =EmailMessage(subject,message,from_email,[self.email],**kwargs)
        email.send()

   
class Vendor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='vendor')
    bio=models.TextField()
    contact_details=models.TextField()
    bank_details=models.TextField()
    shipping_policy = models.TextField()
    return_policy = models.TextField()


class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='subcategories')


    def __str__(self):
        return self.name

class Product(models.Model):
    
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE,related_name='vendor_products')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category_products')
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to='products')
    is_flash_sale=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    products=models.ManyToManyField(Product,through='OrderItem')
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    shipping_address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='Items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

 
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart',null=True,blank=True)
    session_id=models.CharField(max_length=100,null=True,blank=True)
    items=models.ManyToManyField(Product,through='CartItem')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

class Shipping(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    rate=models.DecimalField(max_digits=10,decimal_places=2)

class Payment(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='payments')
    method=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    transaction_id=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

class Coupon(models.Model):
    code=models.CharField(max_length=100,unique=True)
    discount=models.DecimalField(max_digits=10,decimal_places=2)
    valid_from=models.DateTimeField()
    valid_to=models.DateTimeField()

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    rating=models.PositiveIntegerField()
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='wishlist')
    product=models.ManyToManyField(Product,related_name='wishlist')

class Notification(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='notifications')
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    content=models.TextField()
    author= models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class FAQ(models.Model):
    question=models.TextField()
    answer=models.TextField()

class Analytics(models.Model):
    sales=models.DecimalField(max_digits=10,decimal_places=2)
    traffic=models.PositiveIntegerField()
    popular_products=models.ManyToManyField(Product,related_name='analytics')
    created_at=models.DateTimeField(auto_now_add=True)

class Configuration(models.Model):
    site_name=models.CharField(max_length=100)
    site_description=models.TextField()
    site_logo= models.ImageField(upload_to='logos')

class Tax(models.Model):
    name=models.CharField(max_length=100)
    rate=models.DecimalField(max_digits=10,decimal_places=2)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100,null=True,blank=True)

class Subscription(models.Model):
    email=models.EmailField(unique=True)
    subscribed_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
class Refund(models.Model):
    author=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='refunds')
    reason=models.TextField()
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=100)
    requested_at=models.DateTimeField(auto_now_add=True)
    processed_at=models.DateTimeField(null=True,blank=True)


    def __str__(self):
         return f"Refund for Order {self.author.id}"
         






