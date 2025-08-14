from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('football/<int:club_id>', views.club_squad, name='football_detail'),
    path('livematch/', views.match_info, name='match'),
    path('plmatch/', views.Pl_match, name='PLmatch'),
]
