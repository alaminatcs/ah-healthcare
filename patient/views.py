from . import models
from . import serializers
from django.shortcuts import redirect
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, pagination
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# patient pagination
class PatientPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 50

# base patient view
class PatientViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PatientPagination
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# user account creation view
class UserRegistrationApiView(APIView):
    serializer_class = serializers.UserRegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)    
        if serializer.is_valid():
            user = serializer.save()

            # create token and unique id for making verify link
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            verify_link = f"http://127.0.0.1:8000/active/{uid}/{token}/"
            
            # send verification mail
            mail_body = render_to_string('verify_mail.html', {'link': verify_link})
            mail = EmailMultiAlternatives(
                to = [user.email],
                subject = "ah-care's account verification mail",
                body =  '',
            )
            mail.attach_alternative(mail_body, 'text/html')
            mail.send()

            return Response("Check your mail for account confirmation.")
        
        return Response(serializer.errors)

# account activation view
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except User.DoesNotExist:
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    
    return redirect('signup')

# user login class view
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'user_id': user.id, 'token': token.key})
            else:
                return Response('Invalid Credential!')
        
        return Response(serializer.errors)

# user logout class view
class UserLogoutApiView(APIView):
    def get(self, request):
        # request.user.auth_token.delete()
        logout(request)
        return redirect('login')