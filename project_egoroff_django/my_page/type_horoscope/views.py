from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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

types_dict = {
    'fire': ['aries', 'taurus', 'gemini'],
    'earth': ['cancer', 'leo', 'virgo'],
    'air': ['libra', 'scorpio', 'sagittarius'],
    'water': ['capricorn', 'aquarius', 'pisces'],
}

def index(request):
    zodiacs = list(zodiac_dict)#переводимо зі словника в список

    li_elements = ''

    for sign in zodiacs:
        #'horoscope-name' ???
        redirect_patch = reverse('horoscope-name', args=[sign])#horoscope/sign
        # print('redirect_patch', redirect_patch)
        li_elements += f"<li> <a href='{redirect_patch}'>{sign.title()} </a> </li>"
    response = f"""
        <ul>
            {li_elements}
        </ul>
        """
    return HttpResponse(response)

def get_info_about_sign_zodiac(request, sign_zodiac: str):
    # zodiac_dict.get(key, None)
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
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

def get_info_about_sign_zodiac_Two(request, type_zodiac: str, sign_zodiac: int):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f'Невідомий знак зодіака - {sign_zodiac}')

def get_info_by_date(request, month, day):
    return HttpResponse(f'<h2>Місяць - {month} день - {day}</h2>')

def get_info_list_types(request):
    types_list = list(types_dict.keys())#Отримуємо список типів

    li_elements = ''

    for type in types_list:
        li_elements += f"<li> <a href='{type}'>{type.title()} </a> </li>"
    response = f"""
            <ul>
                {li_elements}
            </ul>
            """
    return HttpResponse(response)

def get_info_about_type_zodiac(request, type_zodiac):
    current_type = types_dict.get(type_zodiac)  #отримуємо список знаків для  поточного типу зодіака
    li_elements = ''
    for sign in current_type:
        # test_url = reverse('horoscope-name', args=(sign,))
        # test_url_2 = reverse('types-name', args=(sign,))
        li_elements += f"<li> <a href='{type_zodiac}/{sign}'>{sign.title()}</a> </li>"
    response = f"""
                <ul>
                    {li_elements}
                </ul>
                """
    return HttpResponse(response)













