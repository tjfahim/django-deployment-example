from django.urls import path
from myapp import views

app_name='myapp'

urlpatterns=[
    path('relative',views.relative,name='relative'),
    path('other',views.other,name='other')
]
