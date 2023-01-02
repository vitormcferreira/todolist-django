from django.urls import path

from todolist import views

app_name = 'todolist'

urlpatterns = [
    path('create/', views.ToDoItemCreateView.as_view(), name='create'),
    path('update/<pk>/', views.ToDoItemUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.ToDoItemDeleteView.as_view(), name='delete'),
    path('', views.ToDoItemListView.as_view(), name='home'),
    path('detail/<pk>/', views.ToDoItemDetailView.as_view(), name='detail'),
]
