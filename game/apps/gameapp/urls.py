from django.urls import path

from . import views

app_name = 'gameapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>/', views.detail, name='detail'),
    path('<int:game_id>/leave_comment', views.leave_comment, name='leave_comment'),
]
