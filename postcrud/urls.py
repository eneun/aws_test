from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('postnew/', views.postnew, name='postnew'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('postshow/<int:post_id>', views.postshow, name='postshow'),
    path('scrap/<int:post_id>', views.scrap, name='scrap'), # 스크랩
]