from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('notes', views.notes, name='notes'),
  path('delete_note/<int:pk>', views.delete_note, name='delete-note'),
  path('notes_detail/<int:pk>', views.notes_detail.as_view(), name='notes-detail'), 
  
  path('videos', views.videos, name='videos'),
  
  path('todo', views.todo, name='todo'),
  path('delete_todo/<int:pk>', views.delete_todo, name='delete-todo'),
  path('update_todo/<int:pk>', views.update_todo, name='update-todo'),

  path('wikipedia', views.wikipedia, name='wikipedia'),
]