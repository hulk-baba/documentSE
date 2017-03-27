from tastypie.resources import ModelResource
from .models import Documents


class DocumentResource(ModelResource):
    class Meta:
        queryset = Documents.objects.all()
        resource_name = 'doc'
        allowed_methods = ['get', 'post', 'put']

