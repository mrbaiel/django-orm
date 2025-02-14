from django.urls import path

from apps.hr.views import homePageView, empPageView

urlpatterns = [
    path("", homePageView, name="home"),
    path("emps/", empPageView, name='emps')
]