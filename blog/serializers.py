from rest_framework import serializers
from .models import blog

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = ('id','title','description','titleProject','img','branch','created_at') 