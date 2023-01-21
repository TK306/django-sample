from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("setting/", views.setting_view, name="setting"),
    path("feature1/", views.feature1_view, name="feature1"),
    path("feature2/", views.feature2_view, name="feature2"),
]
