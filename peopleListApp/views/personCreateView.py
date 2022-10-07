from rest_framework                                          import status, views
from rest_framework.response                                 import Response
from peopleListApp.models.person                             import Person
from peopleListApp.serializers.personSerializer              import PersonSerializer
from rest_framework.permissions                              import IsAuthenticated

class PersonCreateView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer= PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        people= Person.objects.all().order_by('id')
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data, status.HTTP_200_OK)