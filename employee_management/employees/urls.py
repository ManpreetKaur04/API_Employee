from django.urls import path
from .views import register, EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView

urlpatterns = [
   path('register/', register, name='register'),
   path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
   path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
]
