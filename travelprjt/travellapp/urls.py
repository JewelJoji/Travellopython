from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.demo,name='demo'),
    path('credentials/',include('credentials.urls'))
]