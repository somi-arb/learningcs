from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('somi/', views.somi, name='somi'),
    path('yasser/', views.yesser, name='yasser'),
    path('<str:name>', views.great, name='great'),
]
