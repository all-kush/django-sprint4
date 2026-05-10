from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.PageAboutView.as_view(), name='about'),
    path('rules/', views.PageRulesView.as_view(), name='rules'),
]
