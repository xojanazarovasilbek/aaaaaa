from django.shortcuts import render
from .models import Sumka
from .serializers import SumkaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination



class SumkaListView(APIView):
    def get(self, request):
        queryset = Sumka.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10  

        result_page = paginator.paginate_queryset(queryset, request)

        serializer = SumkaSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


# @api_view(['GET'])
# def sumka_list(request):
#     search = request.GET.get('search')  
#     sumkalar = Sumka.objects.all()

#     if search:
#         sumkalar = sumkalar.filter(nomi__icontains=search)

#     paginator = PageNumberPagination()
#     paginated_qs = paginator.paginate_queryset(sumkalar, request)
#     serializer = SumkaSerializer(paginated_qs, many=True)

#     res = {
#         'data': serializer.data,
#         'count': sumkalar.count(),
#         'status': status.HTTP_200_OK,
#     }
#     return paginator.get_paginated_response(res)

# @api_view(['GET',])
# def sumka_detail(request, pk):
#     try:
#         sumka = Sumka.objects.get(id=pk)
#     except Sumka.DoesNotExist:
#         return Response({'status': status.HTTP_400_BAD_REQUEST})
#     serializer = SumkaSerializer(sumka)
#     return Response({
#         'book': serializer.data,
#         'status': status.HTTP_200_OK
#     })

# @api_view(['POST',])
# def sumka_create(request):
#     serializer = SumkaSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status': status.HTTP_201_CREATED})
#     return Response({'status': status.HTTP_400_BAD_REQUEST,'error': serializer.errors})

    
# @api_view(['PATCH',])
# def sumka_update(request, pk):
#     try:
#         sumka = Sumka.objects.get(id=pk)
#     except Sumka.DoesNotExist:
#         return Response({'error': 'sumka topilmadi', 'status': status.HTTP_404_NOT_FOUND})
    
#     serializers = SumkaSerializer(sumka, data=request.data, partial= True)
#     if serializers.is_valid():
#         serializers.save()
#         return Response({'status':status.HTTP_200_OK})
#     return Response({'error': serializers.errors, 'status': status.HTTP_400_BAD_REQUEST})

# @api_view(['DELETE',])
# def sumka_delete(request, pk):
#     try:
#         sumka = Sumka.objects.get(id=pk)
#     except Sumka.DoesNotExist:
#         return Response ({'error': 'sumka topilmadi', 'status': status.HTTP_404_NOT_FOUND})
#     sumka.delete()
#     return Response({'info': "o'chirildi", 'status': status.HTTP_200_OK})




# class SumkaApiView(APIView):
#     def get(self, request, pk=None):
#         search = request.GET.get('search')
#         sumkalar = Sumka.objects.all()

#         if search:
#             sumkalar = sumkalar.filter(nomi__icontains=search)

#         paginator = PageNumberPagination()
#         paginated_qs = paginator.paginate_queryset(sumkalar, request)
#         serializer = SumkaSerializer(paginated_qs, many=True)

#         data = {
#             'sumkalar': serializer.data,
#             'count': sumkalar.count(),
#             'status': status.HTTP_200_OK
#         }
#         return paginator.get_paginated_response(data)

#     def post(self, request):
#         serializer = SumkaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'message': "Yangi sumka yaratildi",
#                 'status': status.HTTP_201_CREATED
#             })
#         return Response({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

#     def put(self, request, pk):
#         sumka = get_object_or_404(Sumka, pk=pk)
#         serializer = SumkaSerializer(sumka, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': "O'zgartirildi", 'data': serializer.data})
#         return Response({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

#     def delete(self, request, pk):
#         sumka = get_object_or_404(Sumka, pk=pk)
#         sumka.delete()
#         return Response({'message': "O'chirildi", 'status': status.HTTP_204_NO_CONTENT})

    



# class SumkaView(GenericAPIView):
#     queryset = Sumka.objects.all()
#     serializer_class = SumkaSerializer

#     def get(self, request, pk=None):
#         search = request.GET.get('search')
#         sumkalar = self.get_queryset()

#         if search:
#             sumkalar = sumkalar.filter(nomi__icontains=search)

#         if pk:
#             sumka = get_object_or_404(sumkalar, pk=pk)
#             serializer = self.get_serializer(sumka)
#             return Response(serializer.data)

#         paginator = PageNumberPagination()
#         paginated_qs = paginator.paginate_queryset(sumkalar, request)
#         serializer = self.get_serializer(paginated_qs, many=True)

#         data = {
#             'sumkalar': serializer.data,
#             'count': sumkalar.count(),
#             'status': status.HTTP_200_OK
#         }
#         return paginator.get_paginated_response(data)

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'message': "Sumka yaratildi",
#                 'data': serializer.data,
#                 'status': status.HTTP_201_CREATED
#             })
#         return Response({'errors': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

#     def put(self, request, pk):
#         sumka = get_object_or_404(self.get_queryset(), pk=pk)
#         serializer = self.get_serializer(sumka, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'message': "Yangilandi",
#                 'data': serializer.data
#             })
#         return Response({'errors': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

#     def delete(self, request, pk):
#         sumka = get_object_or_404(self.get_queryset(), pk=pk)
#         sumka.delete()
#         return Response({
#             'message': "O'chirildi",
#             'status': status.HTTP_204_NO_CONTENT
#         })