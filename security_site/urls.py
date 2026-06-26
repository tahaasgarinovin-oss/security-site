from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("سایت بالا اومد 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # 👈 این خط قرمز رو از بین می‌بره
]