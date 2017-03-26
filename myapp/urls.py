from django.conf.urls import url,include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'docs',views.DocumentViewSet)

urlpatterns = [
	url(r'^$',views.index , name= 'index'),
	url(r'^',include(router.urls)),
	url(r'^detail$',views.detail , name = 'detail'),
	url(r'^uploads/(.*)$', views.show , name = 'show'),
	url(r'^api-auth/$', include('rest_framework.urls',namespace = 'rest_framework')),
]