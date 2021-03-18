from rest_framework import generics
from .serializer import SearchSerializer, ListSerializer
from .models import TweetModel
from utils.twitter import Tweet
from utils.matplt import CreateChart
from rest_framework.response import Response
from rest_framework import status

class GetDataView(generics.GenericAPIView):
    serializer_class = SearchSerializer

    def post(self, request):
        try:
            req = request.data
            serializer = self.serializer_class(data=req)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            #Get data from user and calling our Tweet processor:
            keys = data['SearchKeys']
            list_of_keys = str(keys).split(" ")
            number = data['TweetNumber']
            twt = Tweet()
            twt.Search(list_of_keys, int(number))
            #Save data to DB:
            visualize = TweetModel(SearchKeys=' '.join(list_of_keys),
            TweetNumber=number)
            visualize.save()
            pic = str(visualize.id)
            #Creating our Chart
            CreateChart(twt.dataset, pic)
            #Updating the last data we saved in DB
            TweetModel.objects.filter(id=visualize.id).update(Chart=pic)
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

             
class ListDataView(generics.ListAPIView):
    serializer_class = ListSerializer
    queryset = TweetModel.objects.all()

class SingleDataView(generics.GenericAPIView):

    serializer_class = ListSerializer
    queryset = TweetModel.objects.all()

    def get(self, request, id):
        try:
            Filter = TweetModel.objects.filter(id=id)
            serializer = self.serializer_class(Filter, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)