from django.urls import path
from . import views


urlpatterns = [
    path('', views.sampleapp_index, name="sampleapp_index"),
    path('<slug>/', views.sampleapp_detail, name="sampleapp_detail"),
    path('<category>', views.sampleapp_category, name="sampleapp_category"),
]





