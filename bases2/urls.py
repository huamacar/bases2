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
    url(r'^Clientes/busqueda/$', 'proyecto1.views.BuscarClienteAjax', name='Busqueda_Clientes'),


    url(r'^Clientes/editar/(?P<id>\d+)/$', 'proyecto1.views.editarClientes', name='Editar_Clientes'),
    url(r'^Clientes/eliminar/(?P<id>\d+)/$', 'proyecto1.views.Eliminar_Clientes', name='Eliminar_Cliente'),
    url(r'^Clientes/bloquear/(?P<id>\d+)/$', 'proyecto1.views.Bloquear_Clientes', name='Bloquear_Cliente'),

    #autorizacion
    url(r'^Autorizacion/index/$', 'proyecto1.views.indexAutorizacion', name='Autorizacion'),
    url(r'^Autorizacion/consumo/$', 'proyecto1.views.consumo', name='Consumo'),
    url(r'^Autorizacion/autorizar/(?P<id>\d+)/$', 'proyecto1.views.autorizar', name='Autorizar'),
    url(r'^Autorizacion/buscar/$','proyecto1.views.BuscarCuenta2',name='Buscar_Cuenta2'),
    url(r'^Autorizacion/busqueda/$','proyecto1.views.BuscarCuentaAjax2',name='Buscar_CuentaA'),
    url(r'^Autorizacion/retirar/(?P<id>\d+)/$', 'proyecto1.views.retirar', name='Retirar'),

    #senda
    url(r'^Senda/index/$', 'proyecto1.views.indexSenda', name='Senda'),
    url(r'^Senda/senda/$', 'proyecto1.views.senda', name='VerSenda'),
    url(r'^Senda/buscar/$', 'proyecto1.views.buscarSenda', name='BuscarSenda'),

    #listaNegra
    url(r'^ListaNegra/index/$', 'proyecto1.views.indexListaNegra', name='ListaNegra'),
    url(r'^ListaNegra/listanegra/$', 'proyecto1.views.listanegra', name='VerListaNegra'),
    url(r'^ListaNegra/buscar/$','proyecto1.views.BuscarTarjeta',name='Buscar_Tarjeta'),
    url(r'^ListaNegra/busqueda/$','proyecto1.views.BuscarTarjetaAjax',name='Buscar_TarjetaA'),
    url(r'^ListaNegra/agregar/(?P<id>\d+)/$', 'proyecto1.views.agregarTarjeta', name='AgregarTarjeta'),

    #Cuentas
    url(r'^Cuentas/index/$', 'proyecto1.views.indexCuentas', name='Cuentas'),
    url(r'^Cuentas/crear/$', 'proyecto1.views.crearCuenta', name='Crear_Cuenta'),
    url(r'^Cuentas/asignar/$', 'proyecto1.views.asignarCuenta', name='Asignar_Cuenta'),
    url(r'^Cuentas/asignarInteres/$', 'proyecto1.views.asignarInteresCuenta', name='AsignarInteres_Cuenta'),
    url(r'^Cuentas/crearTipo/$', 'proyecto1.views.crearTipoCuenta', name='Tipo_Cuenta'),
    url(r'^Cuentas/consultaSaldo/$', 'proyecto1.views.consultar_Saldo', name='Consultar_Saldo'),
    url(r'^Cuentas/buscarTipoCuenta/$', 'proyecto1.views.buscarTipoCuenta', name='Buscar_TipoCuenta'),
    url(r'^Cuentas/editarTipoCuenta/(?P<id>\d+)/$', 'proyecto1.views.editarTipoCuenta', name='Editar_TipoCuenta'),
    url(r'^Cuentas/eliminarTipoCuenta/(?P<id>\d+)/$', 'proyecto1.views.eliminarTipoCuenta', name='Eliminar_TipoCuenta'),

    #Tarjetas
    url(r'^Tarjetas/index/$', 'proyecto1.views.indexTarjetas', name='Tarjetas'),
    url(r'^Tarjetas/crear/$', 'proyecto1.views.crearTarjeta', name='Crear_Tarjeta'),
    url(r'^Tarjetas/asignar/$', 'proyecto1.views.asignarTarjeta', name='Asignar_Tarjeta'),
    url(r'^Tarjetas/tipoEstado/$', 'proyecto1.views.crearEstadoTarjeta', name='CrearEstado_Tarjeta'),
    url(r'^Tarjetas/declaCambio/$', 'proyecto1.views.declararCambios', name='DeclaCambio_Tarjeta'),
    url(r'^Tarjetas/buscarTipoEstado/$', 'proyecto1.views.buscarTipoEstado', name='Buscar_TipoEstado'),
    url(r'^Tarjetas/editarTipoEstado/(?P<id>\d+)/$', 'proyecto1.views.editarTipoEstado', name='Editar_TipoEstado'),
    url(r'^Tarjetas/eliminarTipoEstado/(?P<id>\d+)/$', 'proyecto1.views.eliminarTipoEstado', name='Eliminar_TipoEstado'),

    #TipoTarjeta
    url(r'^TipoTarjeta/index/$', 'proyecto1.views.indexTipoTarjeta', name='TipoTarjeta'),
    url(r'^TipoTarjeta/crear/$', 'proyecto1.views.crearTipoTarjeta', name='Crear_TipoTarjeta'),
    url(r'^TipoTarjeta/buscar/$', 'proyecto1.views.buscarTipoTarjeta', name='Buscar_TipoTarjeta'),
    url(r'^TipoTarjeta/editar/(?P<id>\d+)/$', 'proyecto1.views.editarTipoTarjeta', name='Editar_TipoTarjeta'),
    url(r'^TipoTarjeta/eliminar/(?P<id>\d+)/$', 'proyecto1.views.eliminarTipoTarjeta', name='Eliminar_TipoTarjeta'),

    #Notas
    url(r'^Notas/index/$', 'proyecto1.views.indexNotas', name='Notas'),
    url(r'^Notas/crear/$', 'proyecto1.views.crearNota', name='Crear_Nota'),

    #Rol
    url(r'^Rol/index/$', 'proyecto1.views.indexRol', name='Rol'),
    url(r'^Rol/crear/$', 'proyecto1.views.crearRol', name='Crear_Rol'),
    url(r'^Rol/autorizar/$', 'proyecto1.views.autorizarRol', name='Autorizar_Rol'),
    url(r'^Rol/privilegio/$', 'proyecto1.views.privilegioRol', name='Privilegio_Rol'),
    url(r'^Rol/buscar/$', 'proyecto1.views.buscarRol', name='Buscar_Rol'),
    url(r'^Rol/editar/(?P<id>\d+)/$', 'proyecto1.views.editarRol', name='Editar_Rol'),
    url(r'^Rol/eliminar/(?P<id>\d+)/$', 'proyecto1.views.eliminarRol', name='Eliminar_Rol'),
    url(r'^Rol/buscarPrivilegio/$', 'proyecto1.views.buscarPrivilegio', name='BuscarPrivilegio_Rol'),
    url(r'^Rol/editarPrivilegio/(?P<id>\d+)/$', 'proyecto1.views.editarPrivilegio', name='EditarPrivilegio_Rol'),
    url(r'^Rol/eliminarPrivilegio/(?P<id>\d+)/$', 'proyecto1.views.eliminarPrivilegio', name='EliminarPrivilegio_Rol'),
    url(r'^Rol/buscarAutorizacion/$', 'proyecto1.views.buscarAutorizacion', name='BuscarAutorizacion_Rol'),
    url(r'^Rol/editarAutorizacion/(?P<id>\d+)/$', 'proyecto1.views.editarAutorizacion', name='EditarAutorizacion_Rol'),
    url(r'^Rol/eliminarAutorizacion/(?P<id>\d+)/$', 'proyecto1.views.eliminarAutorizacion', name='EliminarAutorizacion_Rol'),

    #Emisor
    url(r'^Emisor/index/$', 'proyecto1.views.indexEmisor', name='Emisor'),
    url(r'^Emisor/crear/$', 'proyecto1.views.crearEmisor', name='Crear_Emisor'),
    url(r'^Emisor/asignar/$', 'proyecto1.views.asignarInteresEmisor', name='AsignarInteres_Emisor'),
    url(r'^Emisor/buscar/$', 'proyecto1.views.buscarEmisor', name='Buscar_Emisor'),
    url(r'^Emisor/busqueda/$','proyecto1.views.BuscarEmisorAjax',name='Busqueda_Emisor'),

    url(r'^Emisor/editar/(?P<id>\d+)/$', 'proyecto1.views.editarEmisor', name='Editar_Emisor'),
    url(r'^Emisor/eliminar/(?P<id>\d+)/$', 'proyecto1.views.eliminarEmisor', name='Eliminar_Emisor'),

    #Lotes
    url(r'^Lote/index/$', 'proyecto1.views.indexLotes', name='Lote'),
    url(r'^Lote/crear/$', 'proyecto1.views.crearLote', name='Crear_Lote'),
    url(r'^Lote/asignarUsuario/$', 'proyecto1.views.asignarUsuarioLote', name='AsignarUsuario_Lote'),
    url(r'^Lote/asignarAfiliado/$', 'proyecto1.views.asignarAfiliadoLote', name='AsignarAfiliado_Lote'),

    #TipoAfiliado
    url(r'^TipoAfiliado/index/$', 'proyecto1.views.indexTipoAfiliado', name='TipoAfiliado'),
    url(r'^TipoAfiliado/insertar/$', 'proyecto1.views.insertarTipoAfiliado', name='Insertar_TipoAfiliado'),
    url(r'^TipoAfiliado/buscar/$', 'proyecto1.views.BuscarTipoAfiliado', name='Buscar_TipoAfiliado'),

    url(r'^TipoAfiliado/editar/(?P<id>\d+)/$', 'proyecto1.views.editarTipoAfiliados', name='Editar_TipoAfiliados'),
    url(r'^TipoAfiliado/eliminar/(?P<id>\d+)/$', 'proyecto1.views.Eliminar_TipoAfiliados', name='Eliminar_TipoAfiliados'),

    #Afiliado
    url(r'^Afiliado/index/$', 'proyecto1.views.indexAfiliado', name='Afiliado'),
    url(r'^Afiliado/insertar/$', 'proyecto1.views.insertarAfiliado', name='Insertar_Afiliado'),
    url(r'^Afiliado/buscar/$', 'proyecto1.views.Buscar_Afiliados', name='Buscar_Afiliados'),
    url(r'^Afiliado/busqueda/$','proyecto1.views.BuscarAfiliadoAjax',name='Buscqueda_Afiliados'),

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
