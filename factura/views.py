from django.shortcuts import render
from django.http import HttpResponse
from factura.models import Producto, Factura, LineaFactura
from django.conf import settings

from xhtml2pdf import pisa
from django.template.loader import get_template

# Create your views here.

def homepage(request):
    return render(request, 'factura/home.html')


def render_pdf_view(request,num):
    template_path = 'factura/pdf.html'
    psum=0
    for i in LineaFactura.objects.filter(factura=num):
        psum = psum + i.precio_total()
    ptiva = round(psum*1.21,2)
    
    context = {'factura': Factura.objects.get(pk=num),
        'linea_f': LineaFactura.objects.filter(factura=num),
        'psum': psum,
        'ptiva': ptiva,
        }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="factura.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    return response


def factura(request):
    return render(request, 'factura/factura.html', {
        'factura': Factura.objects.all(),
    })


def factura_detalle(request,num):
    psum=0
    for i in LineaFactura.objects.filter(factura=num):
        psum = psum + i.precio_total()
    ptiva = round(psum*1.21,2)

    contenido = {
        'factura': Factura.objects.get(pk=num),
        'linea_f': LineaFactura.objects.filter(factura=num),
        'psum': psum,
        'ptiva': ptiva,
    }

    return render(request, 'factura/factura_detalle.html', contenido)


def busqueda_productos(request):
    return render(request, 'factura/busqueda_productos.html')


def buscar(request):
    if request.GET['clave']:
        producto = request.GET['clave']
        if len(producto)>20:
            mensaje='Texto de búsqueda demasiado largo'
        else:
            articulos=Producto.objects.filter(nombre_producto__icontains=producto)
            return render(request, 'factura/resultados_busqueda.html', {'articulos': articulos, 'query':producto})
    else:
        mensaje = 'No has introducido nada'

    return HttpResponse(mensaje)

