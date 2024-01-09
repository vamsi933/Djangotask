from django.urls import path
from .views import *

urlpatterns = [
    path('', ListEl),
    path('post/',PostEl),
    path('update/<int:id>/',PutEl),
    path('delete/<int:id>/',DeleteEl)


]
