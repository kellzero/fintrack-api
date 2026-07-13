from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Transaction
from .serializers import TransactionSerializer

# Create your views here.

class TransactionViewSet(viewsets.ModelViewSet):
  serializer_class = TransactionSerializer

  def get_queryset(self):
    return Transaction.objects.filter(user=self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

@api_view(['POST'])
@permission_classes([AllowAny])

def register(request):
  username= request.data.get('username')
  password= request.data.get('password')

  if not username or not password:
    return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
  
  if User.objects.filter(username=username).exists():
    return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST) 
  
  User.objects.create_user(username=username, password=password)
  return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)