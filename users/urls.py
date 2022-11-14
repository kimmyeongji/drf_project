"""drf_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from users import views
from rest_framework_simplejwt.views import ( #simplejwt 기본 기능 import, simplejwt 공식문서 참고
    TokenRefreshView,
)
 
urlpatterns = [ 
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('mock/', views.mockView.as_view(), name='mock _view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), #customized Token 사용하기 위해 views.py 클래스 수정    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #simplejwt 기본 기능
]