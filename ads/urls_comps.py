from django.urls import path

from ads import views

urlpatterns = [
    path('', views.CompilationListView.as_view()),
    path('create/', views.CompilationCreateView.as_view()),
    path('<int:pk>/', views.CompilationRetrieveView.as_view()),
    path('<int:pk>/update/', views.CompilationUpdateView.as_view()),
    path('<int:pk>/delete/', views.CompilationDeleteView.as_view()),

]
