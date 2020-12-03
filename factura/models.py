from django.db import models

# Create your models here.

class Factura(models.Model):

    num = models.AutoField(primary_key=True)
    anio = models.IntegerField(verbose_name='Año')
    fecha_emision = models.DateField()
    cliente_nombre = models.CharField(max_length=30)
    cliente_direccion = models.CharField(max_length=50)
    cliente_telefono = models.IntegerField()

    def precio_final(self):
        psum=0
        for i in LineaFactura.objects.filter(factura=num):
            psum = psum + i.precio_total()
    
        return psum



class Producto(models.Model):

    ref_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    descripcion_producto = models.CharField(max_length=250, blank=True, null=True)
    precio_unitario = models.IntegerField()
    seccion = models.CharField(max_length=30)


class LineaFactura(models.Model):

    id_linea = models.AutoField(primary_key=True)
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.PROTECT,
        )
    unidades = models.IntegerField()
    factura = models.ForeignKey(
        Factura, 
        on_delete=models.PROTECT,
        )
    def precio_total(self):
        pt = self.unidades * self.producto.precio_unitario
        return pt



