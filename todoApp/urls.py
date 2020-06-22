from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('addtask/', views.addtask, name='addtask'),
    path('update/<int:pk>', views.update, name='update'),
    path('updatetask/<int:pk>', views.updatetask, name='update_task'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('deletetask/<int:pk>', views.deletetask, name='delete_task')
]