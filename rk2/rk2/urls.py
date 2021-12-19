from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('catalog', views.catalog_list),
    path('catalog/create', views.CatalogCreate.as_view()),
    path('catalog/<int:id>/update', views.CatalogUpdate.as_view(), name='catalog_update'),
    path('catalog/<int:id>/delete', views.CatalogDelete.as_view(), name='catalog_delete'),
    path('file', views.file_list),
    path('file/create', views.FileCreate.as_view()),
    path('file/<int:id>/update', views.FileUpdate.as_view(), name='file_update'),
    path('file/<int:id>/delete', views.FileDelete.as_view(), name='file_delete'),
    path('report', views.report)
]
