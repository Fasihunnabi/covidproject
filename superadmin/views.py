from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from orders.models import Order
from product.models import Message, ProductCategory, Product, ProductImage
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import logout as Logout
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from datetime import date as dt

# Create your views here.


def index1(request):
    import requests
    import json
    try:
        print(request.GET.get('covid_date' or None).split('-'))
        a = request.GET.get('covid_date' or None).split('-')
        print(a[0])
        # url = 'https://api.data.gov.hk/v2/filter?q=%7B%22resource%22%3A%22http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Flatest_situation_of_reported_cases_covid_19_eng.csv%22%2C%22section%22%3A1%2C%22format%22%3A%22json%22%2C%22filters%22%3A%5B%5B1%2C%22eq%22%2C%5B%22{}%2F{}%2F{}%22%5D%5D%5D%7D'.format(
        #     str(a[2]), str(a[1]), str(a[0]))
        # headers = {'Accept':'application/json', 'Content-Type':'application/json'}

        # r = requests.get(url)
        # data = str(r.json())
        # user_list = json.dumps(r)
        # print(r.json())
    except:
        pass
    context = {
        'd_id': ""
    }
    return render(request, "superadmin/index1.html", context)


def datadisplay(request):
    import requests
    import json
    if request.GET.get('covid_date'):
        print(request.GET.get('covid_date' or None).split('-'))
        a = request.GET.get('covid_date' or None).split('-')
        print(a[0])
    else:
        b = str(dt.today())
        a = b.split("-")
    # url = 'https://api.data.gov.hk/v2/filter?q=%7B%22resource%22%3A%22http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Flatest_situation_of_reported_cases_covid_19_eng.csv%22%2C%22section%22%3A1%2C%22format%22%3A%22json%22%2C%22filters%22%3A%5B%5B1%2C%22eq%22%2C%5B%22{}%2F{}%2F{}%22%5D%5D%5D%7D'.format(
    #     str(a[2]), str(a[1]), str(a[0]))
    url = 'https://api.data.gov.hk/v2/filter?q=%7B%22resource%22%3A%22http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Fenhanced_sur_covid_19_eng.csv%22%2C%22section%22%3A1%2C%22format%22%3A%22json%22%2C%22filters%22%3A%5B%5B2%2C%22bw%22%2C%5B%22{}%2F{}%2F{}%22%5D%5D%5D%7D'.format(
        str(a[2]), str(a[1]), str(a[0]))
    # headers = {'Accept':'application/json', 'Content-Type':'application/json'}

    r = requests.get(url)
    # data = str(r.json())
    # user_list = json.dumps
    list_cases = []
    for obj in r.json():
        print(obj['Case no.'])
        list_cases.append({
            'Case_no': obj['Case no.'],
            'Report_date': obj['Report date'],
            'Date_of_onset': obj['Date of onset'],
            'Gender': obj['Gender'],
            'Age': obj['Age'],
            'Name_of_hospital': obj['Name of hospital admitted'],
            'H_D_Deceased': obj['Hospitalised/Discharged/Deceased'],
            'HK_Non_HK_resident': obj['HK/Non-HK resident'],
            'Case_classification': obj['Case classification*'],
            'Confirmed_probable': obj['Confirmed/probable'],
        })
    print(list_cases)
    context = {
        'covid_case_list': list_cases
    }
    return render(request, "superadmin/listcovidcases.html", context)

