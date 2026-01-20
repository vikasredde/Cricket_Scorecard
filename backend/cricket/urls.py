from .views import AddballAPIVIEW,Innings
from django.urls import path


urlpatterns = [path('api/balls/',AddballAPIVIEW.as_view(),name='add-ball'),
               path('api/innings/<int:innnings_id>/score/',Innings.as_view(),name='innings-score'),
               
               
               ]