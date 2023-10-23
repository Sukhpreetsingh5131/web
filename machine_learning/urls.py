from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('user_info/',views.user_entry),
    path('submit-form/',views.last_result),  # Example path for the index view
]
