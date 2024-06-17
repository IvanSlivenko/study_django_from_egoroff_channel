from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.get_info_list_types),#types/''
    path('<str:type_zodiac>', views.get_info_about_type_zodiac, name='types-name'),
    path('<str:type_zodiac>/<str:sign_zodiac>', views.get_info_about_sign_zodiac_Two),#варіант 2
]