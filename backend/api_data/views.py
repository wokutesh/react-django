from rest_framework import viewsets
from .models import (
     User,Vendor,Product, Category,Order,OrderItem,Cart,CartItem,
    Shipping,Payment,Coupon,Review,Wishlist,Notification,Blog,
    Contact,FAQ,Analytics,Configuration,Tax,Subscription,Refund
)

from.serializers import (
    UserSerializer,VendorSerializer,CategorySerializer,ProductSerializer,
    OrderSerializer,OrderItemSerializer,CartSerializer,CartItemSerializer,
    ShippingSerializer,PaymentSerializer,CouponSerializer,ReviewSerializer,
    WishlistSerializer,NotificationSerializer,BlogSerializer,ContactSerializer,
    FAQSerializer,AnalyticsSerializer, ConfigurationSerializer,TaxSerializer,
    SubscriptionSerializer,RefundSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class=UserSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset= Vendor.objects.all()
    serializer_class=VendorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer   

class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset= Order.objects.all()
    serializer_class=OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset= OrderItem.objects.all()
    serializer_class=OrderItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset= Cart.objects.all()
    serializer_class=CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset= CartItem.objects.all()
    serializer_class=CartItemSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    queryset= Shipping.objects.all()
    serializer_class=ShippingSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset= Payment.objects.all()
    serializer_class=PaymentSerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset= Coupon.objects.all()
    serializer_class=CouponSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset= Review.objects.all()
    serializer_class=ReviewSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset= Wishlist.objects.all()
    serializer_class=WishlistSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset= Notification.objects.all()
    serializer_class=NotificationSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset= Tax.objects.all()
    serializer_class=TaxSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset= Contact.objects.all()
    serializer_class=ContactSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset= Blog.objects.all()
    serializer_class=BlogSerializer
class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset= Configuration.objects.all()
    serializer_class=ConfigurationSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset= FAQ.objects.all()
    serializer_class=FAQSerializer

class AnalyticsViewSet(viewsets.ModelViewSet):
    queryset= Analytics.objects.all()
    serializer_class=AnalyticsSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset= Subscription.objects.all()
    serializer_class=SubscriptionSerializer

class RefundViewSet(viewsets.ModelViewSet):
    queryset= Refund.objects.all()
    serializer_class=RefundSerializer