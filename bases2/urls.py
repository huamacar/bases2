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
    url(r'^Clientes/bloquear/(?P<id>\d+)/$', 'proyecto1.views.Bloquear_Clientes', name='Bloquear_Cliente'),

   #autorizacion
    url(r'^Autorizacion/index/$', 'proyecto1.views.indexAutorizacion', name='Autorizacion'),
    url(r'^Autorizacion/consumo/$', 'proyecto1.views.consumo', name='Consumo'),
    url(r'^Autorizacion/autorizar/(?P<id>\d+)/$', 'proyecto1.views.autorizar', name='Autorizar'),
    url(r'^Autorizacion/buscar/$','proyecto1.views.BuscarCuenta2',name='Buscar_Cuenta2'),
    url(r'^Autorizacion/busqueda/$','proyecto1.views.BuscarCuentaAjax2',name='Buscar_CuentaA'),
    url(r'^Autorizacion/retiro/(?P<id>\d+)/$', 'proyecto1.views.retiro', name='Retiro'),
    url(r'^Autorizacion/retirar/(?P<id>\d+)/$', 'proyecto1.views.retirar', name='Retirar'),

    #Cuentas
    url(r'^Cuentas/index/$', 'proyecto1.views.indexCuentas', name='Cuentas'),
    url(r'^Cuentas/crear/$', 'proyecto1.views.crearCuenta', name='Crear_Cuenta'),
    url(r'^Cuentas/asignar/$', 'proyecto1.views.asignarCuenta', name='Asignar_Cuenta'),
    url(r'^Cuentas/crearTipo/$', 'proyecto1.views.crearTipoCuenta', name='Tipo_Cuenta'),

    #Tarjetas
    url(r'^Tarjetas/index/$', 'proyecto1.views.indexTarjetas', name='Tarjetas'),
    url(r'^Tarjetas/crear/$', 'proyecto1.views.crearTarjeta', name='Crear_Tarjeta'),
    url(r'^Tarjetas/asignar/$', 'proyecto1.views.asignarTarjeta', name='Asignar_Tarjeta'),
    url(r'^Tarjetas/tipoEstado/$', 'proyecto1.views.crearEstadoTarjeta', name='CrearEstado_Tarjeta'),

    #Notas
    url(r'^Notas/index/$', 'proyecto1.views.indexNotas', name='Notas'),
    url(r'^Notas/crear/$', 'proyecto1.views.crearNota', name='Crear_Nota'),

    #Lotes
    url(r'^Lote/index/$', 'proyecto1.views.indexLotes', name='Lote'),
    url(r'^Lote/crear/$', 'proyecto1.views.crearLote', name='Crear_Lote'),
    url(r'^Lote/asignar/$', 'proyecto1.views.asignarLote', name='Asignar_Lote'),

    #TipoAfiliado
    url(r'^TipoAfiliado/index/$', 'proyecto1.views.indexTipoAfiliado', name='TipoAfiliado'),
    url(r'^TipoAfiliado/insertar/$', 'proyecto1.views.insertarTipoAfiliado', name='Insertar_TipoAfiliado'),
    url(r'^TipoAfiliado/buscar/$', 'proyecto1.views.BuscarTipoAfiliado', name='Buscar_TipoAfiliado'),

    url(r'^TipoAfiliado/editar/(?P<id>\d+)/$', 'proyecto1.views.editarTipoAfiliados', name='Editar_TipoAfiliados'),
    url(r'^TipoAfiliado/eliminar/(?P<id>\d+)/$', 'proyecto1.views.Eliminar_TipoAfiliados', name='Eliminar_TipoAfiliados'),
    url(r'^TipoAfiliado/bloquear/(?P<id>\d+)/$', 'proyecto1.views.Bloquear_TipoAfiliados', name='Bloquear_TipoAfiliados'),

    #Afiliado
    url(r'^Afiliado/index/$', 'proyecto1.views.indexAfiliado', name='Afiliado'),
    url(r'^Afiliado/insertar/$', 'proyecto1.views.insertarAfiliado', name='Insertar_Afiliado'),
    url(r'^Afiliado/buscar/$', 'proyecto1.views.Buscar_Afiliados', name='Buscar_Afiliados'),

    url(r'^Afiliado/editar/(?P<id>\d+)/$', 'proyecto1.views.editarAfiliados', name='Editar_Afiliados'),
    url(r'^Afiliado/eliminar/(?P<id>\d+)/$', 'proyecto1.views.Eliminar_Afiliados', name='Eliminar_Afiliados'),
    url(r'^Afiliado/bloquear/(?P<id>\d+)/$', 'proyecto1.views.Bloquear_Afiliados', name='Bloquear_Afiliados'),

    #usuarios
    url(r'^Clientes/Lista/$','proyecto1.views.Lista_Clientes', name='Lista_Clientes'),
    url(r'^Usuarios/registrar/$','proyecto1.views.RegistrarUsuario', name='Registrar_Usuario'),

    #CAJA
    url(r'^Caja/index/$','proyecto1.views.indexCaja',name='Caja'),
    url(r'^Caja/buscar/$','proyecto1.views.BuscarCuenta',name='Buscar_Cuenta'),
    url(r'^Caja/busqueda/$','proyecto1.views.BuscarCuentaAjax',name='Busqueda_Cuenta'),
    url(r'^Caja/pago/(?P<id>\d+)/$', 'proyecto1.views.PagarCuenta', name='Pagar_Cuenta'),
    url(r'^Caja/transferencia/$','proyecto1.views.TransferenciaCuentas',name='Transferencia_Cuenta'),


    #auth
    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),

)
