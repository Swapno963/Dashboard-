from django.urls import path
from .views import DashbordView

urlpatterns = [
    path('get_data/', DashbordView.as_view(), name='dashbordView'),
]
