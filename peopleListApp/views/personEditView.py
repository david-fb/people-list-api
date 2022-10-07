from rest_framework                                           import generics
from peopleListApp.models.person                              import Person
from peopleListApp.serializers.personSerializer               import PersonSerializer
from rest_framework.permissions                               import IsAuthenticated

class PersonEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]