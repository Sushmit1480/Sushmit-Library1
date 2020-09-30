from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.about.as_view(), name = 'about'),
    path('book_list/', views.Book_list.as_view(), name = 'book_list'),
    path('student_list/', views.Student_list.as_view(), name = 'student_list'),
    path('book_create/', views.Book_create.as_view(), name = 'Create-Book'),
    path('student_create/', views.Student_create.as_view(), name = 'Create-Student'),
    path('book_update/<int:pk>/', views.Book_update.as_view(), name = 'book_update'),
    path('student_update/<int:pk>/', views.Student_update.as_view(), name = 'student_update'),
    path('book_delete/<int:pk>/', views.Book_delete.as_view(), name = 'book_delete'),
    path('student_delete/<int:pk>/', views.Student_delete.as_view(), name = 'student_delete'),
    path('fine_confirmation/<int:pk>/',views.Fine_confirmation, name = 'confirm'),
    path('return_fine/<int:pk>/',views.return_fine, name = 'return_fine'),
    path('show_book/<int:pk>/',views.show_book, name = 'show_book'),
    path('logout/',views.logoutuser,name='logout'),
]