from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer, TimingTodoSerializer
from .models import Todo, TimingTodo
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

@api_view()
def home(request):
    return Response({
        'status' : 200,
        'message' : 'Yes! Django rest framework is working!!!!'
    })
    
@api_view(['GET'])   
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many=True)
    return Response({
                'status' : True,
                'message' : 'Todo data fecthed',
                'data' : serializer.data
            })
      
    
    
@api_view(['POST'])   
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status' : True,
                'message' : 'Sucess data',
                'data' : serializer.data
            })
      
        return Response({
            'status' : False,
            'message' : 'Invalid data',
            'data' : serializer.errors
        })
    
    except Exception as e:
        print(e)
    return Response({
        'status' : False,
        'message' : 'Something went wrong!!!!'
    })
    
    
@api_view(['PATCH'])   
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
            'status' : False,
            'message' : 'Id is required!!!!',
            'data' : {}
            }) 
             
        obj = Todo.objects.get(uid = data.get('uid'))
        
        serializer = TodoSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status' : True,
                'message' : 'Sucess data',
                'data' : serializer.data
            })
        return Response({
            'status' : False,
            'message' : 'Invalid data',
            'data' : serializer.errors
        })
    except Exception as e:
        print(e)
        return Response({
            'status' : False,
            'message' : 'Invalid uid',
            'data' : {}
        })
        
        
class TodoviewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    
    @action(detail=False, methods=['GET'])
    def get_timing_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many=True)
        return Response({
            'status' : True,
            'message' : 'Timiing todo fetched',
            'data' : serializer.data
        })
        
    
    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data 
            serializer = TimingTodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                'status' : True,
                'message' : 'Sucess data',
                'data' : serializer.data
                })
            return Response({
            'status' : False,
            'message' : 'Invalid data',
            'data' : serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status' : False,
                'message' : 'Something went wrong',
                'data' : {}
            })