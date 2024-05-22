from . import views
from django.urls import path


app_name = "web"

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('add_user/',views.AddUserView.as_view(),name='add_user'),
    path('user_detail/<str:pk>/',views.UserDetailView.as_view(),name='user_detail_view'),
    path('delete/<int:pk>/',views.DeleteUser.as_view(),name='delete_user'),
]