from django.db import models

# Create your models here.

class CategoriaModel(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    nombre = models.CharField(max_length=100,unique=True,null=False)
    #campos de auditoria
    #campos creados automaticamente por la BD 
    createdAt = models.DateTimeField(auto_now_add=True,db_column='created_at')
    updatedAt = models.DateTimeField(auto_now=True,db_column='updated_at')

    class Meta:
        db_table = 'categorias'


class ProductoModel(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True,db_column='created_at')

    #relaciones
    categoria = models.ForeignKey(to=CategoriaModel,null=True,blank=True,on_delete=models.CASCADE,db_column="categoria_id")

    class Meta: 
        db_table = 'productos'