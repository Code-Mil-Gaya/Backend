from django.urls import path
from . import views as apiViews

urlpatterns = [
    path('', apiViews.api_overview, name='api-overview'),
]