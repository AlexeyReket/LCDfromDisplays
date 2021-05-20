from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AllPixelsInfo, name='main'),
    path('<int:PrimaryKey>/', views.CurrentPixel),
    path('reg/', views.Reg, name="reg")
]
