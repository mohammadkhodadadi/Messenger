from django.urls import path
from .views import MyObtainTokenPairView, RegisterView\
    , PasswordResetView, PasswordResetConfirmAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('reset-password/', PasswordResetView.as_view(), name='password-reset'),
    path('reset-password/<str:uidb64>/<str:token>/', PasswordResetConfirmAPIView.as_view(), name='confirm-password'),
]

