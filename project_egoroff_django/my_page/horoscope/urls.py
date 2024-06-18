from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),#horoscope
    path('menu', views.index_render),#horoscope/menu
    path('study', views.index_study_render),#horoscope/study
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number), #варіант 1
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),#/horoscope

]

# path('<int:month>/<int:day>', views.get_info_by_date),
# path('', views.get_info_list_types),#types/''
# path('<str:type_zodiac>', views.get_info_about_type_zodiac, name='types-name'),
# path('<str:type_zodiac>/<str:sign_zodiac>', views.get_info_about_sign_zodiac_Two),#варіант 2