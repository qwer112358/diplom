from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('base/', views.base, name='base'),
    path('questions/<slug:profession_slug>/', views.QuestionList.as_view(), name='questions'),
    path('question/<int:pk>/', views.QuestionDetail.as_view(), name='question_detail'),
    path('mock/', views.Mock.as_view(), name='mock'),

    path('requirements/', views.Requirements.as_view(), name='requirements'),
    #path('requirements/python_developer/', views.requirement_python, name='requirement_python'),
    #path('requirements/1C/', views.requirement_1C, name='requirement_1C'),
    path('requirements/<slug:profession_slug>/', views.requirement_list, name='requirement_list'),

    path('practice/', views.practice, name='practice'),
    path('practice/frontend', views.frontend, name='frontend'),
    path('practice/python', views.python, name='python'),

]
