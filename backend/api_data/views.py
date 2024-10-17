import logging 
import json
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework import viewsets,status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_str 
from django.contrib.auth import get_user_model
from django.views import View
from django.http import JsonResponse
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from .token import account_activation_token
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

User =get_user_model()

from .models import (
    Vendor,Product, Category,Order,OrderItem,Cart,CartItem,
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


logger = logging.getLogger(__name__)
class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        logger.debug('Signup request received: %s', request.data)

        email = request.data.get('email')
        name = request.data.get('name')
        password = request.data.get('password')
        is_vendor = request.data.get('is_vendor', False)

        if not email or not name or not password:
            logger.error('Signup failed: Missing fields')
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            logger.error("Signup failed: Email already exists")
            return Response({'error': 'Email address already registered'}, status=status.HTTP_400_BAD_REQUEST)

        try:
           
            user = User.objects.create_user(email=email, name=name, password=password)
            user.is_vendor = is_vendor 
            user.save()

          
            user.send_activation_email(request)

            logger.debug('User created successfully: %s', user)
            return Response({'message': 'User created successfully. Please confirm your email address to complete registration.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error("Signup failed: %s", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):


    permission_classes = [AllowAny]

    def post(self,request):
        email = request.data.get('email') 
        password = request.data.get('password') 
        user = authenticate(request,email=email,password=password)

        if user is not None and user.is_active:
        
            login(request,user)
            token,created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key,'message':'Login successful'})
        else:
            return Response({'error':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):

    permission_classes = [AllowAny]
    def post(self,request):
        logout(request)
        return Response({'message':'Logout successful'})

class ActivateView(APIView):

    permission_classes = [AllowAny]
    def get(self, request, uidb64, token):
        logger.debug(f'Activation attempt for UID: {uidb64},Token:{token}')
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            logger.debug(f'User found: {user}')
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None  
            logger.debug('User does not exist or decoding failed')

        if user is not None:
            token_valid = account_activation_token.check_token(user, token)
            if token_valid:
                user.is_active = True
                user.save()
                logger.debug('User activated successfully.')
                return Response({'message': 'Thank you for your email confirmation. Now you can log in to your account.'})
            else:
                logger.error('Token is invalid')
                return Response({'message':'Token is invalid'})
        else:
            logger.debug('activation link is invalid')
            return Response({'error': 'Activation link is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        slug = self.request.query_params.get('category')
        return Product.objects.filter(category__slug=slug)
@method_decorator(csrf_exempt, name='dispatch')
class PasswordResetRequestView(View):
    permission_classes = [AllowAny]

    def post(self, request,*args,**kwargs):

        try:
            data = json.loads(request.body)
            email = data.get('email')
        
        except (ValueError,KeyError):
            return JsonResponse({'error':'invalid email'},status=400)
       
        if not User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Invalid email address'}, status=400)

        user = User.objects.get(email=email)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        reset_link = f'http://localhost:3000/reset-password/{uid}/{token}'
        mail_subject = 'Reset your password'
        message = f'Greetings {user.name},\n\nPlease click the link below to reset your password:\n\n{reset_link}\n\nThank you.'

        try:
            send_mail(mail_subject, message, 'wokumateshome13@gmail.com', [user.email])
        except Exception as e:
            return JsonResponse({'error':str(e)},status=500)
        return JsonResponse({'success':'Password reset email sent'},status=200)
@method_decorator(csrf_exempt,name ='dispatch')
class PasswordResetConfirmView(View):

    permission_classes = [AllowAny]
    def post(self,request,uidb64,token,*args,**kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError,ValueError,OverflowError,User,DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user,token):
            try:
                body = json.loads(request.body)
                password = body.get('password') 
                password_confirm = body.get('password_confirm')
            except json.JSONDecodeError:
                return JsonResponse({'error':'Invalid JSON'},status=400)
            if password == password_confirm:
                user.set_password(password)
                user.save()
                return JsonResponse({'message':'Password reset success'})
            else:
                return JsonResponse({'error':'Passwords do not match'},status = 400)
        else:
            return JsonResponse({'error':'Invalid token'},status = 400)
        

    

class UserDetailsViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request):
        logger.debug('UserDetailsViewset accessed')
        logger.debug(f'User:{request.user}')
        user = request.user
        if user.is_active:
            serializer =UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User account is not active'},status = status.HTTP_401_UNAUTHORIZED)
class VendorViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Vendor.objects.all()
    serializer_class=VendorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Category.objects.all()
    serializer_class=CategorySerializer   
class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field ='slug'
    permission_classes =[AllowAny]

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Order.objects.all()
    serializer_class=OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= OrderItem.objects.all()
    serializer_class=OrderItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Cart.objects.all()
    serializer_class=CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= CartItem.objects.all()
    serializer_class=CartItemSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Shipping.objects.all()
    serializer_class=ShippingSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Payment.objects.all()
    serializer_class=PaymentSerializer

class CouponViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Coupon.objects.all()
    serializer_class=CouponSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Review.objects.all()
    serializer_class=ReviewSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Wishlist.objects.all()
    serializer_class=WishlistSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Notification.objects.all()
    serializer_class=NotificationSerializer

class TaxViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Tax.objects.all()
    serializer_class=TaxSerializer

class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Contact.objects.all()
    serializer_class=ContactSerializer

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Blog.objects.all()
    serializer_class=BlogSerializer
class ConfigurationViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Configuration.objects.all()
    serializer_class=ConfigurationSerializer

class FAQViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= FAQ.objects.all()
    serializer_class=FAQSerializer

class AnalyticsViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Analytics.objects.all()
    serializer_class=AnalyticsSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Subscription.objects.all()
    serializer_class=SubscriptionSerializer

class RefundViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset= Refund.objects.all()
    serializer_class=RefundSerializer