from rest_framework import serializers
from .models import Todo, TimingTodo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):
    
    slug = serializers.SerializerMethodField()
    
    class Meta:
        model = Todo
        fields = ['todo_title', 'slug', 'todo_description', 'is_done', 'uid']
        #exclude = ['created_at']
        
    def get_slug(self, obj):
        return slugify(obj.todo_title)
        
    def validate_todo_title(self, data):
        if data:
            todo_title = data
            
            if len(todo_title) < 3:
                raise serializers.ValidationError('todo tilte must be greater than 3 character')
            
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('todo tilte cannot contain special character')
        return data   

    #def validate(self, validated_data):
    
class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()
    class Meta:
        model = TimingTodo
        exclude = ['created_at', 'updated_at']
        #depth = 1
        
            