from rest_framework import serializers

from .models import (
    User,Vendor,Category,Product,Order,OrderItem,Cart,CartItem,
    Shipping,Payment,Coupon,Review,Wishlist,Notification,Blog,
    Contact,FAQ,Analytics,Configuration,Tax,Subscription,Refund

)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= '__all__'
    
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vendor
        fields= '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    vendor = serializers.PrimaryKeyRelatedField(queryset=Vendor.objects.all())
    review=serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model= Product
        fields= '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    
    class Meta:
        model= Order
        fields= '__all__'

class OrderItemSerializer(serializers.ModelSerializer):

    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model= OrderItem
        fields= '__all__'

class CartSerializer(serializers.ModelSerializer):
    items= serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)


    class Meta:
        model=Cart
        fields= '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CartItem
        fields= '__all__'

class ShippingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Shipping
        fields= '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Payment
        fields= '__all__'

class CouponSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Coupon
        fields= '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    customer=UserSerializer(read_only=True)

    class Meta:
        model=Review
        fields= '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    product=ProductSerializer(many=True,read_only=True)

    class Meta:
        model=Wishlist
        fields= '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Notification
        fields= '__all__'

class BlogSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)

    class Meta:
        model=Blog
        fields= '__all__'

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Contact
        fields= '__all__'

class FAQSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=FAQ
        fields= '__all__'

class AnalyticsSerializer(serializers.ModelSerializer):
    popular_products=ProductSerializer(many=True,read_only=True)

    class Meta:
        model=Analytics
        fields= '__all__'

class ConfigurationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Configuration
        fields= '__all__'

class TaxSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Tax
        fields= '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Subscription
        fields= '__all__'

class RefundSerializer(serializers.ModelSerializer):
    order=OrderSerializer(read_only=True)
    
    class Meta:
        model=Refund
        fields= '__all__'