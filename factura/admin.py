from django.contrib import admin

from factura.models import Factura, LineaFactura, Producto

# Register your models here.


class FacturaAdmin(admin.ModelAdmin):
    list_display = ('num','cliente_nombre','fecha_emision')
    search_fields = ('anio', 'cliente_nombre', 'cliente_telefono')
    list_filter = ('fecha_emision', )
    date_hierarchy = 'fecha_emision' 

admin.site.register(Factura, FacturaAdmin)


class LineaFacturaAdmin(admin.ModelAdmin):
    list_display = ('id_linea',)
    search_fields = ('id_linea',)

admin.site.register(LineaFactura, LineaFacturaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'seccion', 'ref_producto','precio_unitario')
    search_fields = ('nombre_producto','seccion','ref_producto','precio_unitario')
    list_filter = ('seccion', 'nombre_producto', 'ref_producto')

admin.site.register(Producto, ProductoAdmin)