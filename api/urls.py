from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchListDetailsAV.as_view(), name='movie-detail'),
    path('', include(router.urls)),
    # path('', views.StreamPlatformAV.as_view(), name='stream-list'),
    # path('<int:pk>/', views.StreamPlatformDetailsAV.as_view(), name='streamplatform-detail'),
    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetails.as_view(), name='review-details'),
]