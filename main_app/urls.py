from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
    , path('query/', views.query, name='query')
    , path('result/', views.result, name='result')
    , path('help/', views.help, name='help')
    , path('detail/<int:wid>/', views.detail, name='worker-detail')
    ]
