from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import  reverse

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - March 21 — April 20',
    'taurus': 'Телець - April 21 — May 22',
    'gemini': 'Близнюки - May 23 — June 21',
    'cancer': 'Рак - June 22 — July 22',
    'leo': 'Лев - July 23 — August 22',
    'virgo': 'Діва - August 23 — September 22',
    'libra': 'Терези - September 23 — October 22 ',
    'scorpio': 'Скорпіон - October 23 — November 21 ',
    'sagittarius': 'Стрілець - November 22 — December 22',
    'capricorn': 'Козоріг - December 23 — January 20',
    'aquarius': 'Водолій - January 21 — February 19',
    'pisces': 'Риби - 	February 20 — March 20',
}


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    # zodiac_dict.get(key, None)
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Невідомий знак зодіака - {sign_zodiac}')

def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Невірний полрядковий номер знака зодіака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))

    # return HttpResponseRedirect(f'/horoscope/{name_zodiac}')
    return HttpResponseRedirect(redirect_url)





