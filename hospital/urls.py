
from django.urls import path
from .views import About, Add_Doctor, Add_Patient, Delete_Appointment, Delete_Patient,  Home, Contact, Login, Take_Appointment, View_Appointment, View_Doctor, View_Patient, logout_admin, Index, Delete_Doctor

urlpatterns = [
    path('about/', About, name='about'),
    path('', Home, name='home'),    
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('delete_doctor(?P<int:pid>)/', Delete_Doctor, name='delete_doctor'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('delete_patient(?P<int:pid>)/', Delete_Patient, name='delete_patient'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('delete_patient(?P<int:pid>)/', Delete_Appointment, name='delete_appointment'),
    path('take_appointment/', Take_Appointment, name='take_appointment'),
]