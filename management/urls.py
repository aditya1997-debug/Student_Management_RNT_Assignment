from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("get_all_students", views.get_all_students),
    path('get_student/<int:pk>', views.get_single_student),
    path('delete_student/<int:pk>', views.delete_student)
]