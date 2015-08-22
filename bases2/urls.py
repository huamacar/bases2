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
    url(r'^Clientes/editar/$', 'proyecto1.views.editarClientes', name='Editar_Clientes'),
   url(r'^Clientes/eliminar/(?P<id>\w{0,50})/$', 'proyecto1.views.Eliminar_Clientes', name='Eliminar_Cliente')
)
