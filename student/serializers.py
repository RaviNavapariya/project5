from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower() !='r':
            raise serializers.ValidationError('You may start with r!!1')
        return value
    
    name = serializers.CharField(validators = [start_with_r])
    # roll = serializers.IntegerField(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['city']
        # extra_kwars = {'name':{'read_only':True}}

    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full!!')
        return value

    def validate(self,value):
        nm = value.get('name')
        ct = value.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'pok':
            raise serializers.ValidationError('City is poka')
        return value
    