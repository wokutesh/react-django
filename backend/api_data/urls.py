from django.urls import path, include
from rest_framework import routers
from  .views import(
    UserViewSet,VendorViewSet,CategoryViewSet,ProductViewSet,
    OrderViewSet,OrderItemViewSet,CartViewSet,CartItemViewSet,
    ShippingViewSet,PaymentSerializer,CouponViewSet,ReviewViewSet,
    WishlistViewSet,BlogViewSet,ContactViewSet,
    FAQSerializer,AnalyticsViewSet, ConfigurationViewSet,TaxViewSet,
    SubscriptionViewSet,RefundViewSet
)

router=routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'vendor',VendorViewSet)
router.register(r'categories',CategoryViewSet)
router.register(r'products',ProductViewSet)
router.register(r'orders',OrderViewSet)
router.register(r'order-items',OrderItemViewSet)
router.register(r'carts',CartViewSet)
router.register(r'cart-items',CartItemsViewSet)
router.register(r'shippings',ShippingViewSet)
router.register(r'payments',PaymentViewSet)
router.register(r'blogs',BlogViewSet)
router.register(r'reviews',ReviewViewSet)
router.register(r'coupons',CouponViewSet)
router.register(r'taxes',TaxViewSet)
router.register(r'wishlists',WishlistViewSet)
router.register(r'refunds',RefundsViewSet)
router.register(r'contacts',ContactViewSet)
router.register(r'configurations',ConfigurationViewSet)
router.register(r'faqs',FAQViewSet)
router.register(r'notifications',NotificationViewSet)
router.register(r'analytics',AnalyticsViewSet)
router.register(r'subscriptions',SubscriptionViewSet)


urlpattern=[

    path('api/',include(router.urls)),
    
]