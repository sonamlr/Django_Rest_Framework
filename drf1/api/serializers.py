from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']
        # fields = '__all__'
        # exclude = 'name'



# Validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name should be start with R')
    
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators=[start_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.name)
#         instance.save()
#         return instance
    
#     # Field Level Validation
#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError('Seat Full')
#         return value
#     # object Level Validation
#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'sonam' and ct.lower() != 'shivpuri':
#             raise serializers.ValidationError('City must be Shivpuri')
#         return data 