from rest_framework import generics,response,status,request
from .models import CategoriaModel
from .serializers import CategoriaSerializer


class CategoriaApiView(generics.ListCreateAPIView):
    #queryset es un atributo para indicarle que informacion quiero obtener
    queryset = CategoriaModel.objects.all() #select * from categorias;
    serializer_class = CategoriaSerializer

class UnaCategoriaApiView(generics.RetrieveAPIView):
    def get(self,request,id):
        #select * from categorias where id = ...
        resultado = CategoriaModel.objects.filter(id = id).first()
        if resultado is None:
            return response.Response(data={
                'message':'La categoria no existe'
            },status=status.HTTP_404_NOT_FOUND)
        
        serializador =  CategoriaSerializer(instance=resultado)
        return response.Response(data={
            'message':serializador.data
        },status=status.HTTP_200_OK)
    
    def put(self,request:request.Request,id):
        #filtrando el id 
        resultado = CategoriaModel.objects.filter(id = id).first()
        if resultado is None:
            return response.Response(data={
                'message':'La categoria no existe'
            },status=status.HTTP_404_NOT_FOUND)
        
        data_serializada = CategoriaSerializer(data=request.data)

        if data_serializada.is_valid():
            resultado.nombre = data_serializada.data.get('nombre')
            resultado.save()

            return response.Response(data={
                'message':'categoria actualizada'
            })
        else:
            return response.Response(data={
                'message':'Error al actualizar',
                'content':data_serializada.errors
            })