from django.urls import path
from todo.views import TodoAppCreateView, TodoAppListView, TodoAppDetailView, TodoAppUpdateView, TodoAppDeleteView

urlpatterns = [
    path('', TodoAppCreateView.as_view(), name='home'),
    path('todo/', TodoAppListView.as_view(), name='todo'),
    path('todo_detail/<str:pk>', TodoAppDetailView.as_view(), name="todo_detail"),
    path('todo_update/<str:pk>', TodoAppUpdateView.as_view(), name="todo_update" ),
    path('todo_delete/<str:pk>', TodoAppDeleteView.as_view(), name="todo_delete")
]
