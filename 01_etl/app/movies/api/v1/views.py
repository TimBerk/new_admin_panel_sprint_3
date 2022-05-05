from movies.api.v1.serializers import MovieSerializer
from movies.mixins import ListRetrieveAPIView
from movies.models import Filmwork


class MovieViewSet(ListRetrieveAPIView):
    queryset = Filmwork.objects.main_queryset()
    serializer_class = MovieSerializer
