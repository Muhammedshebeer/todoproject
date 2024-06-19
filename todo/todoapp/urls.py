from django.urls import path
from.import views

urlpatterns = [
    path('',views.home),
    path('home', views.home,name='home'),
    path('todo',views.todo,name='todo'),
    path('del/<int:id>',views.delt,name='del'),
    path('updt/<int:id>',views.update,name='updt')
    
]