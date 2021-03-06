"""ajaxcrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('get-suggestions/', views.autocomplete_names,name="autocomplete_names"),
    path('get-suggestions-city/', views.autocomplete_city,name="autocomplete_city"),
    path('export_csv/', views.export_csv,name="csv"),
    path('signin/', views.sign_in,name="login"),
    path('logout/', views.log_out,name="logout"),
    path('<int:id>/', views.home,name="home"),
    path('generatepdf/<int:id>/', views.home,name="generatepdf"),
    path('<int:id>/save/', views.save_data,name="save"),
    path('<int:id>/edit/', views.edit_data,name="edit"),
    path('save/', views.save_data_book,name="save_for_book"),
    path('edit/', views.edit_data_book,name="edit_for_book"),
    path('generatebill/<int:id>', views.generatebill,name="generatebill"),
    path('generatebillold/<int:id>/<int:billno>', views.download_old,name="download_old"),
    # path('generatepdf/<int:id>/', views.Generatepdf.as_view(), name = 'generatepdf'),
]