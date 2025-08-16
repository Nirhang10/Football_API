from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('club/<int:club_id>', views.club_squad, name='Club_detail'),
    path('player/<int:player_id>', views.player_info, name='player_detail'),
    path('livematch/', views.live_match_info, name='livematch'),
    path('plmatch/', views.Pl_match, name='PLmatch'),
]
