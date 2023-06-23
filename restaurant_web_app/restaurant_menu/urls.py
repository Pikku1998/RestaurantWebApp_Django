from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='index'),
    path('item/<int:pk>', views.ItemDetail.as_view(), name='details')
]
