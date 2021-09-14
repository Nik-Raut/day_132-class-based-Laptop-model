from django.urls import path
from .views import *

urlpatterns = [


    path('base/',homeview,name='base'),

    path('list/', LaptopListview.as_view(),name='list'),
    path('create/', LaptopCreateView.as_view(),name='create'),
    path('update/<int:pk>', LaptopUpdateView.as_view(),name='update'),
    path('delete/<int:pk>', LaptopDeleteView.as_view(),name='delete'),
]