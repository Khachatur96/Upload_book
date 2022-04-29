from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("upload/", views.upload, name="upload"),
    path("books/", views.book_list, name="book_list"),
    path("books/upload/", views.upload_book, name="upload_book"),
    path("books/<int:pk>/", views.delete_book, name="delete"),

]
