
from rest_framework import serializers
from .models import mainsignup,Signup,Fav_list

class MainsignupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = mainsignup
        fields = [

        'id',
        'sid',
        'fname',
        'mname',
        'lname',
        'image',
        'gender',
        'dobdate',
        'sd',
        'age',
        'height',
        'education',
        'job',
        'cname',
        'sname',
        'dname',
        'phno1',
        'phno2',
        'religion',
        'rashi',
        'income',
        'image1',
        'image2',
        ]
class SignupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Signup
        fields = [
        'id',
        'fname',
        'lname',
        'gender',
        'date',
        'email',
        'phno1',
        'password',
        
        ]
    
class FavSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Fav_list
        fields = [
        'id',
        'mid',
        'statusid',
        'supid',
        
        ]

