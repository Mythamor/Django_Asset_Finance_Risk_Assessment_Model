from django.urls import path

from . import views



urlpatterns = [
     path('', views.index, name="home"),
     path('<str:username>/<int:question_id>/', views.get_loan, name="get_loan" ),
 
]
