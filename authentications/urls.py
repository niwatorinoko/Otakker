from django.urls import path, include
from .views import AuthenticationsSignupView, AuthenticationsLoginView, AuthenticationsLogoutView, UserProfileView

app_name = 'authentications'

urlpatterns = [
    path('signup/', AuthenticationsSignupView.as_view(), name='signup'),
    path('login/', AuthenticationsLoginView.as_view(), name='login'),
    path('logout/', AuthenticationsLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
]
