from rest_framework import generics
from .models import dashbordModel
from .serializers import MyModelSerializer
from django.db.models import Count, Sum,Avg,Max,Min
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.pagination import PageNumberPagination

# for pagenation
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

# Getting 10 data
class DashbordView(generics.ListAPIView):
    queryset = dashbordModel.objects.all()
    serializer_class = MyModelSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('end_year','country', 'topic','region','sector','pestle','source',)
    pagination_class = LargeResultsSetPagination

# Basic summary like : total data, average-min-max likelihood, intensity, relevance
def basic_summary(request):
    summary = dashbordModel.objects.aggregate(
        total=Count('id'), 
        average_likeliHood=Avg('likelihood'),
        max_likelihood=Max('likelihood'), 
        min_likelihood=Min('likelihood'),
        average_intensity=Avg('intensity'),
        max_intensity=Max('intensity'), 
        min_intensity=Min('intensity'),
        average_relevance=Avg('relevance'),
        max_relevance=Max('relevance'), 
        min_relevance=Min('relevance'),
                                              )                                          
    formatted_summary = {
        "total": summary["total"],
        "average_likeliHood": round(summary["average_likeliHood"], 2),
        "max_likelihood": summary["max_likelihood"],
        "min_likelihood": summary["min_likelihood"],
        "average_intensity": round(summary["average_intensity"], 2),
        "max_intensity": summary["max_intensity"],
        "min_intensity": summary["min_intensity"],
        "average_relevance": round(summary["average_relevance"], 2),
        "max_relevance": summary["max_relevance"],
        "min_relevance": summary["min_relevance"],
    }
    return JsonResponse(formatted_summary)

# group by sector, topic, region and country
def count_by_sector_topic_region_country(request):
    # count by sector
    sector_id = dashbordModel.objects.values('sector').annotate(total=Count('id'))
    topic_id = dashbordModel.objects.values('topic').annotate(total=Count('id'))
    region_id = dashbordModel.objects.values('region').annotate(total=Count('id'))
    country_id = dashbordModel.objects.values('country').annotate(total=Count('id'))
    
    return JsonResponse({
        "sector_id":list(sector_id),
        "topic_id":list(topic_id),
        "region_id":list(region_id),
        "country_id":list(country_id),
        
        })

# co-relation between all
def co_relaton(request):
    # count by sector
    sector_intensity = dashbordModel.objects.values('sector').annotate(average_intensity=Avg('intensity'))
    sector_impact = dashbordModel.objects.values('sector').annotate(average_intensity=Avg('impact'))
    sector_relevance = dashbordModel.objects.values('sector').annotate(average_intensity=Avg('relevance'))
    sector_likelihood = dashbordModel.objects.values('sector').annotate(average_intensity=Avg('likelihood'))
    
    topic_intensity = dashbordModel.objects.values('topic').annotate(average_intensity=Avg('intensity'))
    topic_impact = dashbordModel.objects.values('topic').annotate(average_intensity=Avg('impact'))
    topic_relevance = dashbordModel.objects.values('topic').annotate(average_intensity=Avg('relevance'))
    topic_likelihood = dashbordModel.objects.values('topic').annotate(average_intensity=Avg('likelihood'))
    
    

    return JsonResponse({
        "sector_intensity":list(sector_intensity)[:20],
        "sector_impact":list(sector_impact)[:20],
        "sector_relevance":list(sector_relevance)[:20],
        "sector_likelihood":list(sector_likelihood)[:20],
        # list(quantities),
        "topic_intensity":list(topic_intensity)[:20],
        "topic_impact":list(topic_impact)[:20],
        "topic_relevance":list(topic_relevance)[:20],
        "topic_likelihood":list(topic_likelihood)[:20],
        
        })

# top 5 data
def top_data(request):
    # Get top 5 records for each field
    top_intensity = dashbordModel.objects.order_by('-intensity')[:5]
    top_impact = dashbordModel.objects.order_by('-impact')[:5]
    top_relevance = dashbordModel.objects.order_by('-relevance')[:5]
    top_likelihood = dashbordModel.objects.order_by('-likelihood')[:5]
    
    # Serialize each queryset individually
    top_intensity_data = MyModelSerializer(top_intensity, many=True).data
    top_impact_data = MyModelSerializer(top_impact, many=True).data
    top_relevance_data = MyModelSerializer(top_relevance, many=True).data
    top_likelihood_data = MyModelSerializer(top_likelihood, many=True).data

    # Return a JSON response with serialized data
    return JsonResponse({
        "top_intensity": top_intensity_data,
        "top_impact": top_impact_data,
        "top_relevance": top_relevance_data,
        "top_likelihood": top_likelihood_data,
    })