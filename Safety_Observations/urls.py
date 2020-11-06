from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view
from .views import *
#from . import view
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.conf.urls import url
from .routers import router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views
schema_view = get_schema_view(
   openapi.Info(
      title="SAFETY_OBSERVATION_API",
      default_version='v1',
      description="Safety Observation",
      terms_of_service="http://promena.in/",
      contact=openapi.Contact(email="Pradeep@promena.in"),
      #license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   
)


urlpatterns = [


    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/',include(router.urls) ),
    path('api/token/obtain/',CustomTokenObtainPairView.as_view() ),
    path('api/token/refresh/',TokenRefreshView.as_view() ),
    path('api/change_password/',ChangePasswordView.as_view() ,name='change-password'),
    #path('login/',Login_view.as_view()),
    #path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path("api/password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path("api/password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path("api/password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path("api/password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
