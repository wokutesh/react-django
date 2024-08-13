from rest_framework import viewsets
from .models import (
     User,Vendor,Category,Order,OrderItem,Cart,CartItem,
    Shipping,Payment,Coupon,Review,Wishlist,Notification,Blog,
    Contact,FAQ,Analytics,Configuration,Tax,Subscription,Refund
)

from.serializer import (
    UserSerializer,VendorSerializer,CategorySerializer,ProductSerializer,
    OrderSerializer,OrderItemSerializer,CartSerializer,CartItemSerializer,
    ShippingSerializer,PaymentSerializer,CouponSerializer,ReviewSerializer,
    WishlistSerializer,NotificationSerializer,BlogSerializer,ContactSerializer,
    FAQSerializer,AnalyticsSerializer, ConfigurationSerializer,TaxSerializer,
    SubscriptionSerializer,RefundSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.object.all()
    serializer_class=UserSerializer

 class VendorViewSet(viewsets.ModelViewSet):
    queryset= Vendor.object.all()
    serializer_class=VendorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.object.all()
    serializer_class=CategorySerializer   

class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.object.all()
    serializer_class=ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset= Order.object.all()
    serializer_class=OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset= OrderItem.object.all()
    serializer_class=OrderItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset= Cart.object.all()
    serializer_class=CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset= CartItem.object.all()
    serializer_class=CartItemSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    queryset= Shipping.object.all()
    serializer_class=ShippingSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset= Payment.object.all()
    serializer_class=PaymentSerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset= Coupon.object.all()
    serializer_class=CouponSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset= Review.object.all()
    serializer_class=ReviewSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset= Wishlist.object.all()
    serializer_class=WishlistSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset= Notification.object.all()
    serializer_class=NotificationSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset= Tax.object.all()
    serializer_class=TaxSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset= Contact.object.all()
    serializer_class=ContactSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset= Blog.object.all()
    serializer_class=BlogSerializer
class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset= Configuration.object.all()
    serializer_class=ConfigurationSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset= FAQ.object.all()
    serializer_class=FAQSerializer

class AnalyticsViewSet(viewsets.ModelViewSet):
    queryset= Analytics.object.all()
    serializer_class=AnalyticsSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset= Subscription.object.all()
    serializer_class=SubscriptionSerializer

class RefundViewSet(viewsets.ModelViewSet):
    queryset= Refund.object.all()
    serializer_class=RefundSerializer