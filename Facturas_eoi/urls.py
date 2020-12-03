
from django.contrib import admin
from django.urls import path
from factura import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('busqueda_productos/', views.busqueda_productos),
    path('buscar/', views.buscar),
    path('factura/', views.factura),
    path('factura/<int:num>', views.factura_detalle),
    path('factura/<int:num>/pdf', views.render_pdf_view, name='test-view'),
]
