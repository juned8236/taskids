from django.shortcuts import render
from rest_framework.views import APIView
from app.api.serializers import TableSerializer
from rest_framework.response import Response
from app.models import TestTable
from rest_framework import generics
from django.views.generic import View
import json
# list all 
# http://127.0.0.1:8000/api/table/
class TableListApi(APIView):
    def get(self,request,format=None):
        qs=TestTable.objects.all()
        serializer=TableSerializer(qs,many=True)
        return Response(serializer.data)



# create
# http://127.0.0.1:8000/api/productcreate/ 
class tableCreateAPIView(generics.CreateAPIView):
    qs=TestTable.objects.all()
    serializer_class=TableSerializer

class tablejsonCreateAPIView(View):
    def post(self,request,*args,**kwargs):
        data=request.body()
        print(data)
        # qs=TestTable.objects.all()
        # serializer_class=TableSerializer(qs,data=data,many=True)
        # valid_json=is_json(data)
        # if not valid_json:
        #     return self.render_to_http_response(json.dumps({'msg':'please send valid json only'}),status=400)
        # std_data=json.loads(data)
        # for x in std_data:
        #     print(x)
    

#     # http://127.0.0.1:8002/api/companynupdatendelete/14/ 
# class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Company.objects.all()
#     serializer_class=CompanySerializer
#     lookup_field='id'


# # list all 
# # http://127.0.0.1:8000/api/product/

# class ProductListApi(APIView):
#     def get(self,request,format=None):
#         qs=Product.objects.all()
#         print(qs)
#         serializer=ProductSerializer(qs,many=True)
#         return Response(serializer.data)


# # Search 
# # http://127.0.0.1:8000/api/productsearch/?product_name=sona

# class ProductSearch(generics.ListAPIView):
#     serializer_class=ProductSerializer
#     def get_queryset(self):
#         qs=Product.objects.all()
#         name=self.request.GET.get('product_name')
#         # print(name)
#         if name is not None:
#             qs=qs.filter(product_name__icontains=name)
#         return qs

# # create
# # http://127.0.0.1:8000/api/productcreate/ 
# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer


# # http://127.0.0.1:8000/api/delete/2/ 
# # http://127.0.0.1:8000/api/delete/3/ 
# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
#     lookup_field='id'

# # http://127.0.0.1:8000/api/listncreate/ 
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer


# # http://127.0.0.1:8000/api/listnupdate/2/ 
# class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
#     lookup_field='id'

# # http://127.0.0.1:8000/api/listndelete/3/ 
# class ProductRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
#     lookup_field='id'

# class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
#     lookup_field='id'
