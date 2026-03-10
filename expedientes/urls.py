from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    path('crear/', views.crear_estudiante, name='crear_estudiante'),
    path('eliminar/<int:pk>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    # Expediente
    path('expediente/<int:pk>/', views.expediente, name='expediente'),
    path('expediente/<int:pk>/guardar/', views.guardar_estudiante, name='guardar_estudiante'),

    # Archivos
    path('expediente/<int:pk>/subir/', views.subir_archivo, name='subir_archivo'),
    path('expediente/<int:pk>/eliminar-archivo/', views.eliminar_archivo, name='eliminar_archivo'),

    # Descargas
    path('expediente/<int:pk>/descargar-exp1/', views.descargar_expediente1, name='descargar_exp1'),
    path('expediente/<int:pk>/descargar-exp2/', views.descargar_expediente2_unido, name='descargar_exp2'),
    path('expediente/<int:pk>/informe-word/', views.generar_informe_word, name='informe_word'),

    # Resoluciones
    path('expediente/<int:pk>/resolucion/subir/', views.subir_resolucion, name='subir_resolucion'),
    path('resolucion/<int:pk>/eliminar/', views.eliminar_resolucion, name='eliminar_resolucion'),

    # API
    path('api/estudiante/<int:pk>/estado/', views.api_estado_estudiante, name='api_estado'),
]
