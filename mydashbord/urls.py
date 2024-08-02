from django.urls import path
from .views import DashbordView,basic_summary,count_by_sector_topic_region_country,co_relaton,top_data

urlpatterns = [
    path('get_data/', DashbordView.as_view(), name='dashbordView'),
    path('basic_summary/', basic_summary, name='basic_summary'),
    path('count_summary/', count_by_sector_topic_region_country, name='count_summary'),
    path('co_relaton/', co_relaton, name='co_relaton'),
    path('top_data/', top_data, name='top_data'),
]
