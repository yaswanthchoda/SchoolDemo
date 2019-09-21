from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from schapp.models import Student
from schapp.serializers import UserSerializer, StudentSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import filters

User = get_user_model()


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)



@api_view(['POST'])
@permission_classes((AllowAny,))
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.initial_data['email'],
            serialized.initial_data['username'],
            serialized.initial_data['password']
        )
        return Response(serialized.data, status=HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=HTTP_400_BAD_REQUEST)

class SchoolList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def StudentData(request, school_id, page_size=None):
    if request.method == 'GET':
        if page_size:
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            student = Student.objects.filter(user=school_id)
            result_page = paginator.paginate_queryset(student, request)
            serializer = StudentSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

        student = Student.objects.filter(user=school_id)
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=request.data['user'])
            serializer.save(user=user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def StudentPagiantedData(request, page_size):
    if request.method == 'GET':
        if school_id:
            student = Student.objects.filter(user=school_id)
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)

    paginator = PageNumberPagination()
    paginator.page_size = page_size
    person_objects = Person.objects.all()
    result_page = paginator.paginate_queryset(person_objects, request)
    serializer = PersonSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)



class StudentSearchData(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    print(filter_backends,"================")
    search_fields = ['name', 'age']
    ordering_fields = '__all__'







