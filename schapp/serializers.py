from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from schapp.models import Student

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        
        if 'is_school' in validated_data:
            user.is_school = True

        user.save()


        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", )


class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ( "id", "username", "email", )


class StudentSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    class Meta:
        model = Student
        fields = ('name', 'age', 'is_adult', 'user')
        read_only_fields = ['is_adult']

    def validate(self, data):
        if data['age'] < 6:
            raise serializers.ValidationError("Minimum age might greater than 5 years")

        if data['age'] < 17 and data['age'] > 5:
            data['is_adult'] = False

        return data

