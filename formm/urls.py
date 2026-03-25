
from django.urls import path
from .views import contact_view,student_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('student/', student_view, name='student'),
]
