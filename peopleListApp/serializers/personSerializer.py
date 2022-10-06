from rest_framework import serializers
from peopleListApp.models.person import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'document_type', 'document', 'names', 'surnames', 'hobbie']