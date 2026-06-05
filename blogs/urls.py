
from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>/', views.post_list_by_category, name='post_by_category'),
]

