from django.urls import path
from myapp import views
urlpatterns=[
    path('multiselect/',views.multiselect,name='multiselect'),
    path('img_upld/',views.img_upld,name="img_upld"),
]