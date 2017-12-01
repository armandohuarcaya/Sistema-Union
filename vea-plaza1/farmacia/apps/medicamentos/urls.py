from django.conf.urls import patterns, url
from .views import ListaMedicamentos, DetalleView,ActualizarView, CreateMedicamentos, EliminarView, CreatePresentacion

urlpatterns = patterns('',

	url(r'^producto/$', ListaMedicamentos.as_view(), name = 'lista_medicamentos'),
	url(r'^producto/detalle/(?P<pk>\d+)/$', DetalleView.as_view(), name ='detalle_medicamentos'),
	url(r'^producto/actualizar/(?P<pk>\d+)/$', ActualizarView.as_view(), name ="actualizar_medicamentos"),
	url(r'^producto/agregar$', CreateMedicamentos.as_view(), name='create_medicamentos'),
	url(r'^producto/eliminar/(?P<pk>\d+)/$', EliminarView.as_view(), name="eliminar_medicamentos"), 
	#exportar a excel
	#url(r'^expatenciones/$', 'apps.medicamentos.views.CargaAtenciones_ant',name='xds'),
	url(r'^producto/reporte/$', 'apps.medicamentos.views.generar_reporte_medicamentos',name='reporte'),
	#presentacion
	url(r'^producto/presentacion$', CreatePresentacion.as_view(), name='create_presentacion'),
	)
