from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.notes, name='notes'),
    path('todo', views.todo, name='todo'),
    path('books', views.books, name='books'),
    path('dictionary', views.dictionary, name='dictionary'),
    path('wikipedia', views.wiki, name='wikipedia'),
    path('homework', views.homework, name='homework'),
    path('youtube', views.youtube, name="youtube"),
    path('conversion', views.conversion, name="conversion"),
    path('delete_notes/<int:pk>', views.delete_note, name='delete_note'),
    path('delete_todos/<int:pk>', views.delete_todo, name='delete_todo'),
    path('delete_homework/<int:pk>', views.delete_homework, name='delete_homework'),
    path('notes_detail/<int:pk>', views.notes_detail.as_view(), name='notes_detail'),
    path('update_homework/<int:pk>', views.update_homework, name='update_homework'),
    path('update_todos/<int:pk>', views.update_todos, name='update_todos'),
]