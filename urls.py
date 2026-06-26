from django.contrib import admin
from django.urls import path
from recruitment.views import home, apply

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('apply/', apply),
]