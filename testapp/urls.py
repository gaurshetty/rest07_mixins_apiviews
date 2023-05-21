from django.urls import path
from . import views


urlpatterns = [
    path('', views.EmployeeCreateMixinListAPIView.as_view()),
    path('<int:pk>/', views.EmployeeUpdateDestroyMixinRetrieveAPIView.as_view()),
]
