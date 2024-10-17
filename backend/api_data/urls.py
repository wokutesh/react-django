from django.urls import path, include
from rest_framework import routers
from  .views import(
    UserDetailsViewSet,VendorViewSet,CategoryViewSet,ProductViewSet,
    OrderViewSet,OrderItemViewSet,CartViewSet,CartItemViewSet,
    ShippingViewSet,PaymentViewSet,CouponViewSet,ReviewViewSet,
    WishlistViewSet,BlogViewSet,ContactViewSet,NotificationViewSet,
    FAQViewSet,AnalyticsViewSet, ConfigurationViewSet,TaxViewSet,
    SubscriptionViewSet,RefundViewSet,ProductDetailView,ProductListByCategory,
    LoginView,LogoutView,SignupView,ActivateView,PasswordResetRequestView,PasswordResetConfirmView,
   
)

router=routers.DefaultRouter()

router.register(r'vendor',VendorViewSet)
router.register(r'categories',CategoryViewSet)
router.register(r'products',ProductViewSet)
router.register(r'orders',OrderViewSet)
router.register(r'order-items',OrderItemViewSet)
router.register(r'carts',CartViewSet)
router.register(r'cart-items',CartItemViewSet)
router.register(r'shippings',ShippingViewSet)
router.register(r'payments',PaymentViewSet)
router.register(r'blogs',BlogViewSet)
router.register(r'reviews',ReviewViewSet)
router.register(r'coupons',CouponViewSet)
router.register(r'taxes',TaxViewSet)
router.register(r'wishlists',WishlistViewSet)
router.register(r'refunds',RefundViewSet)
router.register(r'contacts',ContactViewSet)
router.register(r'configurations',ConfigurationViewSet)
router.register(r'faqs',FAQViewSet)
router.register(r'notifications',NotificationViewSet)
router.register(r'analytics',AnalyticsViewSet)
router.register(r'subscriptions',SubscriptionViewSet)


urlpatterns=[

    path('api/',include(router.urls)),
    path('api/products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/products/', ProductListByCategory.as_view(), name='product-list'),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/activate/<str:uidb64>/<str:token>/', ActivateView.as_view(), name='activate'),
    path('api/auth/user/',UserDetailsViewSet.as_view(),name='user-detail'),
    path('api/password-reset/',PasswordResetRequestView.as_view(),name='password_reset'),
    path('api/password-reset-confirm/<str:uidb64>/<str:token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    
]   