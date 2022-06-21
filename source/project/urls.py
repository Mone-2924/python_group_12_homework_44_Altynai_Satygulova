from django.urls import path

from project.views import index_view

urlpatterns = [
    path('', index_view),
]

