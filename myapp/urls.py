from django.conf.urls import url,include
from rest_framework import routers
from . import views
from tastypie.api import Api
from myapp.api import DocumentResource


v1_api = Api(api_name='v1')
v1_api.register(DocumentResource())

router = routers.DefaultRouter()
router.register(r'docs',views.DocumentViewSet)

urlpatterns = [
	url(r'^$',views.index , name= 'index'),
	url(r'^search$',views.search , name = 'search'),
	url(r'^',include(router.urls)),
	url(r'^newuser$',views.newUser , name='newuser'),
	url(r'^login$',views.login , name='login'),
	url(r'^logout$',views.logout , name='logout'),
	url(r'^api/', include(v1_api.urls)),
	url(r'^detail$',views.detail , name = 'detail'),
	url(r'^uploads/(.*)$', views.show , name = 'show'),
	url(r'^api-auth/$', include('rest_framework.urls',namespace = 'rest_framework')),
]