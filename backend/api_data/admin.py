from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    User,Vendor,Category,Product,Order,OrderItem,Cart,CartItem,
    Shipping,Payment,Coupon,Review,Wishlist,Notification,Blog,
    Contact,FAQ,Analytics,Configuration,Tax,Subscription,Refund

)

class UserAdmin(BaseUserAdmin):
    list_display =('email','name','is_admin','is_staff','is_active')
    list_filter= ('is_admin',)
    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Personal info',{'fields':('name')}),
        ('Permission',{'fields':('is_admin','is_staff','is_active')}),
    )

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email','name','password','password2'),

        }),
    )

    search_fields =('email','name')
    ordering =('email')
    filter_horizontal =()
admin.site.register(User)
admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Shipping)
admin.site.register(Payment)
admin.site.register(Configuration)
admin.site.register(Coupon)
admin.site.register(Review)
admin.site.register(Refund)
admin.site.register(Notification)
admin.site.register(Contact)
admin.site.register(FAQ)
admin.site.register(Analytics)
admin.site.register(Wishlist)
admin.site.register(Blog)
admin.site.register(Tax)
admin.site.register(Subscription)

