from rest_framework import generics, status
from rest_framework.response import Response
from .models import Market, MarketFileDemo, MarketFileDone
from .serializers import MarketFileDoneSerializer, MarketFileDemoSerializer, MarketSerializer, MarketListSerializer


class MarketListAPIView(generics.ListAPIView):
    serializer_class = MarketListSerializer

    def get_queryset(self):
        queryset = Market.objects.all()
        is_top = self.request.GET.get('is_top')
        views = self.request.GET.get('popular')
        if is_top:
            queryset = queryset.filter(is_top=True)
        if views:
            queryset = queryset.order_by('-views')
        return queryset


class MarketCreateAPIView(generics.CreateAPIView):
    serializer_class = MarketSerializer
    queryset = Market.objects.all()


class MarketFileDemoCreateAPIView(generics.CreateAPIView):
    serializer_class = MarketFileDemoSerializer
    queryset = MarketFileDemo.objects.all()


class MarketFileDoneCreateAPIView(generics.CreateAPIView):
    serializer_class = MarketFileDoneSerializer
    queryset = MarketFileDone.objects.all()


class MarketCreateView(generics.CreateAPIView):
    serializer_class = MarketListSerializer
    queryset = Market.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        # try:
        #     demo = self.request.data['demo']
        #     done = self.request.data['done']
        #     for i in demo:
        #         file = MarketFileDemo.objects.create(market=obj, file=i)
        #         file.save()
        #     for i in done:
        #         filee = MarketFileDone.objects.create(market=obj, file=i)
        #         filee.save()
        #     return Response({'message': 'Successfully saved'}, status=status.HTTP_201_CREATED, )
        # except:
        #     pass
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MarketRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketListSerializer
