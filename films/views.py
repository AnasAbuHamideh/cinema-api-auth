from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateAPIView
                                    )

from .models import Film
from .serializers import FilmsSerializer
from rest_framework.permissions import IsAuthenticated

class FilmsListView(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmsSerializer
    permission_classes = (IsAuthenticated, )


class FilmsDetailView(RetrieveUpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmsSerializer
    