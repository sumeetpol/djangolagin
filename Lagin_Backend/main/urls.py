from django.urls import path,include
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'signuphi', views.SignupViewSet)
router.register(r'fav', views.FavViewSet)
from .views import email_list,main_list,GroupViewSet,signup_list,Signup_detail,Main_detail,Main_image,Fav_detail,fav_list
from django.conf.urls import url
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('main/', main_list),
    path('email_list/', email_list),
    path('signup/', signup_list),
     path('favlist/', fav_list),
    path('cmain/', GroupViewSet),
    path('signup_detail/<int:pk>/', views.Signup_detail),
    path('main_detail/<int:pk>/', views.Main_detail),
     path('main_image/<int:pk>/', views.Main_image),
     path('fav_detail/<int:pk>/', views.Fav_detail),
  
]
