from django.urls.conf import path
from . import views

urlpatterns = [ 
    path('',views.add_employee, name='addEmployee'),
    path('updateEmployee/<id>/',views.update_employee,name='updateEmployee'),

]