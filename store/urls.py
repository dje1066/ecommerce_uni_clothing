from django.urls import path
from . import views
from .views import FrontpageView

urlpatterns = [
    path('frontpage-view/', FrontpageView.as_view(), name='frontpage-view'),
    path('', views.frontpage, name='frontpage')
]