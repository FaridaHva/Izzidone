from rest_framework import serializers
from .models import Service, Subservice
from .models import Service, Subservice, ChooseService, Professional, MySkills, AllPros, Order


#Services

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ['created_at', 'is_active']

class SubserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subservice
        exclude = ['created_at', 'is_active']

class ChooseServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseService
        exclude = ['created_at', 'is_active']



# Professionals


class MySkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySkills
        fields = '__all__'

class AllProsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllPros
        exclude = ('is_active', 'created_at')

class ProfessionalSerializer(serializers.ModelSerializer):

    my_skills = MySkillsSerializer(many=True, source='myskills_set')
    all_pros = AllProsSerializer(many=True, source='allpros_set')

    class Meta:
        model = Professional
        exclude = ('is_active', 'created_at', 'certificate', 'portfolio')

    def create(self, validated_data):
        my_skills_data = validated_data.pop('myskills_set', [])
        all_pros_data = validated_data.pop('allpros_set', [])

        professional = Professional.objects.create(**validated_data)

        MySkills.objects.bulk_create(
            [MySkills(professional=professional, **skill_data) for skill_data in my_skills_data]
        )

        AllPros.objects.bulk_create(
            [AllPros(professional=professional, **pro_data) for pro_data in all_pros_data]
        )

        return professional
    


#Orders
 
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) 
    
    class Meta:
        model = Order
        exclude = ('created_at', 'is_active')



