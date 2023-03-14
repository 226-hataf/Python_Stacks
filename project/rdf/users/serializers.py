from django.contrib.auth.models import User
from rest_framework import serializers,validators


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        
        fields = ('username', 'password', 'email','first_name', 'last_name')
        
        extra_kwargs = {
        
        "password":{"Write_only": True},
        "email":{
            "required": True,
            "allow_blank": False,
            "validators":[
                validators.UniqueValidator(
                    User.objects.all(),"Email ALready Exits"
                )
            ] 
            
        }
        
}
        
def create(self,validated_data):
    
    username = validated_data.get("username")
    email = validated_data.get("email")
    password = validated_data.get("password") 
    first_name = validated_data.get("first_name")
    last_name = validated_data.get("last_name")
    
    
    
    
    
    user = User.objects.create(
        username= username,
        email = email,
        password = password,
        first_name = first_name,
        last_name = last_name
        
    )
    
    return user