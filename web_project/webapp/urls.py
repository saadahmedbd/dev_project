from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name=''),

    path('register', views.register, name="register"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # crud
    path ('dashboard', views.dashboard, name='dashboard'),
    path('create_record', views.createUserRecord, name="create_record"),
    path('update_record/<int:pk>' ,views.updateUserRecord, name="update_record"),
    path('record/<int:pk>', views.singularRecord, name="record"),
    path('delete_record<int:pk>', views.deleteRecord, name="delete_record")
]
