
from rest_framework import serializers
from .models import mainsignup,Signup,Fav_list

class MainsignupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = mainsignup
        fields = [

        'id',
        'hid',
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
        'heartc',
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
	'otp',
        
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

