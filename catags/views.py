from rest_framework import generics
from rest_framework import permissions
from catags.models import CaTag
from catags.serializers import CaTagSerializer, CaTagCreateSerializer, CaTagDetailSerializer


class CaTagList(generics.ListAPIView):
    model = CaTag
    serializer_class = CaTagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        This view should return a list of if q, all tags that contain q else, all tags
        """
        queryset = CaTag.objects.all()
        # query = self.request.QUERY_PARAMS.get('q', None)
        # if query is not None:
        #     queryset = queryset.filter(name__icontains=query)
        return queryset

class CatagCreateAPIView(generics.CreateAPIView):
    model = CaTag
    serializer_class = CaTagCreateSerializer

class CaTagDetail(generics.RetrieveAPIView):
    """
    Retrieve, update or delete a tag instance.
    """
    queryset = CaTag.objects.all()
    serializer_class = CaTagDetailSerializer
    lookup_field = 'catag_slug'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)