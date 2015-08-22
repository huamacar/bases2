from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bases2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'proyecto1.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),

    #clientes
    url(r'^Clientes/index/$', 'proyecto1.views.indexClientes', name='Clientes'),
    url(r'^Clientes/insertar/$', 'proyecto1.views.insertarClientes', name='Insertar_Clientes'),
    url(r'^Clientes/buscar/$', 'proyecto1.views.Buscar_Clientes', name='Buscar_Clientes'),

    url(r'^Clientes/editar/(?P<id>\d+)/$', 'proyecto1.views.editarClientes', name='Editar_Clientes'),
    url(r'^Clientes/eliminar/(?P<id>\d+)/$', 'proyecto1.views.Eliminar_Clientes', name='Eliminar_Cliente'),

    url(r'^Cuentas/index/$', 'proyecto1.views.indexCuentas', name='Cuentas'),
    url(r'^Cuentas/crear/$', 'proyecto1.views.crearCuenta', name='Crear_Cuenta'),
    url(r'^Cuentas/asignar/$', 'proyecto1.views.asignarCuenta', name='Asignar_Cuenta'),
    url(r'^Tarjetas/index/$', 'proyecto1.views.indexTarjetas', name='Tarjetas'),
    url(r'^Tarjetas/crear/$', 'proyecto1.views.crearTarjeta', name='Crear_Tarjeta'),
    url(r'^Tarjetas/asignar/$', 'proyecto1.views.asignarTarjeta', name='Asignar_Tarjeta'),
    url(r'^TipoAfiliado/index/$', 'proyecto1.views.indexTipoAfiliado', name='TipoAfiliado'),
    url(r'^TipoAfiliado/insertar/$', 'proyecto1.views.insertarTipoAfiliado', name='Insertar_TipoAfiliado'),
    url(r'^Afiliado/index/$', 'proyecto1.views.indexAfiliado', name='Afiliado'),
    url(r'^Afiliado/insertar/$', 'proyecto1.views.insertarAfiliado', name='Insertar_Afiliado'),
    url(r'^Afiliado/buscar/$', 'proyecto1.views.Buscar_Afiliados', name='Buscar_Afiliados'),

    url(r'^Afiliado/editar/(?P<id>\d+)/$', 'proyecto1.views.editarAfiliados', name='Editar_Afiliados'),
    url(r'^Afiliado/eliminar/(?P<id>\d+)/$', 'proyecto1.views.Eliminar_Afiliados', name='Eliminar_Afiliados')
)
